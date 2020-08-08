import requests
import urllib.parse
import json


class YoutubeSearch:
    def __init__(self, text: str, limit=None):
        self.text = text
        self.limit = limit
        self.videos = self.search()

    def search(self):
        search = urllib.parse.quote(self.text)
        BASE_URL = "https://youtube.com"
        url = f"{BASE_URL}/results?search_query={search}"
        response = requests.get(url).text
        while 'window["ytInitialData"]' not in response:
            response = requests.get(url).text
        results = self.parse_html(response)
        if self.limit is not None and len(results) > self.limit:
            return results[: self.limit]
        return results

    def parse_html(self, response):
        results = []
        start = (
            response.index('window["ytInitialData"]')
            + len('window["ytInitialData"]')
            + 3
        )
        end = response.index("};", start) + 1
        json_str = response[start:end]
        data = json.loads(json_str)

        videos = data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"][
            "sectionListRenderer"
        ]["contents"][0]["itemSectionRenderer"]["contents"]

        for video in videos:
            res = {}
            if "videoRenderer" in video.keys():
                video_data = video.get("videoRenderer", {})
                res["title"] = video_data.get("title", {}).get("runs", [[{}]])[0].get("text", None)
                res["id"] = video_data.get("videoId", None)
                res["thumbnails"] = [thumb.get("url", None) for thumb in video_data.get("thumbnail", {}).get("thumbnails", [{}]) ]
                res["description"] = video_data.get("descriptionSnippet", {}).get("runs", [{}])[0].get("text", None)
                res["channel"] = video_data.get("longBylineText", {}).get("runs", [[{}]])[0].get("text", None)
                res["duration"] = video_data.get("lengthText", {}).get("simpleText", 0)
                res["views"] = video_data.get("viewCountText", {}).get("simpleText", 0) 
                res["url"] = "https://youtube.com" + video_data.get("navigationEndpoint", {}).get("commandMetadata", {}).get("webCommandMetadata", {}).get("url", None)
                results.append(res)
        return results

    def get_it(self):
        query = self.text
        num = len(self.videos)
        return {"query": query, "total results": num, "videos": self.videos}