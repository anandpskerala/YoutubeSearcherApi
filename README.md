##  Youtube Searcher Api [Unofficial]

### Show some :heart: and :star: the repo to support the project

[![GitHub stars](https://img.shields.io/github/stars/Anandpskerala/youtubesearcherapi.svg?style=social&label=Star)](https://github.com/cyberboysumanjay/JioSaavnAPI) ![GitHub followers](https://img.shields.io/github/followers/Anandpskerala.svg?style=social&label=Follow)
[![Telegram Channel](https://img.shields.io/badge/Telegram-Channel-orange)](https://t.me/Keralabotsnews)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

#### Youtube Searcher Api written in Python using Flask  

## Usage

Make a get request specifying the name of the video you want
```
https://youtubesearcher.vercel.app/search?q={name}
```
Example - https://youtubesearcher.vercel.app/search?q=flask

---

## Response Format

The response JSON Object looks something like this - 

```JSON
{

    "query": "flask",
    "total results": 17,
    "videos": [
        {
            "channel": "freeCodeCamp.org",
            "description": "Flask",
            "duration": "46:59",
            "id": "Z1RJmh_OqeA",
            "thumbnails": [
                "https://i.ytimg.com/vi/Z1RJmh_OqeA/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAuToT2WhtYyxoNenChum3vaPINkA",
                "https://i.ytimg.com/vi/Z1RJmh_OqeA/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLD2_JIwPHoglSsUNAukZpYjypohRQ"
            ],
            "title": "Learn Flask for Python - Full Tutorial",
            "url": "https://youtube.com/watch?v=Z1RJmh_OqeA",
            "views": "395,156 views"
        }
     ]
}
```
---
## Setup

Install all dependencies listed in *requirements.txt* file. 

1. To install all dependencies run - 

    ```bash
    $ sudo -H pip3 install -r requirements.txt
    ```

2. Start the server

    ```bash 
    $ python app.py
    ```

### You can fork the repo and deploy on VPS, Heroku or Vercel :)  
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Anandpskerala/YoutubeSearcherApi/tree/master)

[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/Anandpskerala/YoutubeSearcherApi/tree/master)

---
#### Star the Repo in case you liked it :)

# © [Anand PS Kerala](https://github.com/Anandpskerala)
