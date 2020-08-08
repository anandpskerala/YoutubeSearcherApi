import json

from flask import Flask, jsonify, request
from yt import YoutubeSearch

app = Flask(__name__)
app.url_map.strict_slashes = True

@app.route("/")
def home():
    return jsonify({"status":"Youtube Scrapper Api is Up and Running."})

@app.route("/search",  methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        text = request.form.get("q")
        result = YoutubeSearch(text).get_it()
        return jsonify(result)
    text = request.args.get('q')
    result = YoutubeSearch(text).get_it()
    return jsonify(result)


@app.errorhandler(404)
def notfound(e):
    return jsonify({"status" : 404, "message" : "Requested url not found"}), 404


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port="5000")
