const backendUrl = "https://cors-anywhere.herokuapp.com/https://www.googleapis.com/youtube/v3/search"; // Using CORS proxy for local development
const apiKey = "AIzaSyCdOxKAx_lZdyo2k96Gv5mj-qJlCg3ALfQ"; // Replace with your actual YouTube API key

async function searchSongs() {
  const query = document.getElementById("search-input").value;
  if (!query) return; // Prevent empty search

  const songList = document.getElementById("song-list");
  songList.innerHTML = ""; // Clear previous results

  try {
    // Make the API request to search for songs
    const response = await axios.get(backendUrl, {
      params: {
        part: "snippet",
        q: query,
        type: "video", // Only search for videos
        key: apiKey,   // Your YouTube API key
      },
    });

    const videos = response.data.items;

    if (videos.length === 0) {
      songList.innerHTML = "<p>No results found</p>";
      return;
    }

    // Loop through the results and display them
    videos.forEach((video) => {
      const songCard = document.createElement("div");
      songCard.className = "song-card";
      songCard.innerHTML = `
        <div class="flex">
          <img src="${video.snippet.thumbnails.default.url}" alt="${video.snippet.title}" class="thumbnail">
          <div class="song-details">
            <h3>${video.snippet.title}</h3>
            <p>${video.snippet.channelTitle}</p>
          </div>
        </div>
        <button class="play-button" onclick="playSong('${video.id.videoId}')">Play</button>
      `;
      songList.appendChild(songCard);
    });
  } catch (error) {
    console.error("Error fetching songs:", error);
  }
}

function playSong(videoId) {
  const player = document.getElementById("player");
  player.innerHTML = `
    <iframe
      width="100%"
      height="315"
      src="https://www.youtube.com/embed/${videoId}?autoplay=1"
      frameborder="0"
      allow="autoplay; encrypted-media"
      allowfullscreen
    ></iframe>
  `;
}
