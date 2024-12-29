from flask import Flask, Response
import requests

app = Flask(__name__)

# URL of the raw HTML file in your GitHub repository
HTML_URL = "https://raw.githubusercontent.com/username/aeroplane-company-website/main/index.html"

@app.route('/')
def home():
    # Fetch the HTML file from GitHub
    response = requests.get(HTML_URL)
    if response.status_code == 200:
        return Response(response.content, content_type="text/html")
    else:
        return "Failed to load the page. Please try again later.", 500

if __name__ == '__main__':
    app.run(debug=True)
