from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# YouTube Data API Key
YOUTUBE_API_KEY = "AIzaSyCdOxKAx_lZdyo2k96Gv5mj-qJlCg3ALfQ"

@app.get("/search")
def search_songs(query: str):
    """Search for songs using YouTube API."""
    url = f"https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query + " song",
        "type": "video",
        "key": YOUTUBE_API_KEY,
        "maxResults": 10,
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="YouTube API Error")
    
    data = response.json()
    results = [
        {
            "id": item["id"]["videoId"],
            "title": item["snippet"]["title"],
            "thumbnail": item["snippet"]["thumbnails"]["default"]["url"],
            "channel": item["snippet"]["channelTitle"],
        }
        for item in data.get("items", [])
    ]
    return results

@app.get("/stream/{video_id}")
def stream_song(video_id: str):
    """Provide the direct YouTube link for streaming."""
    return {"url": f"https://www.youtube.com/watch?v={video_id}"}
