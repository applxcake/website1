from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Discord Bot Showcase</title>
    <link href=\"https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap\" rel=\"stylesheet\">
    <style>
        body {
            margin: 0;
            font-family: 'Inter', sans-serif;
            background: linear-gradient(to bottom, #000000, #1a1a1a);
            color: white;
            overflow-x: hidden;
        }
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 10%;
            background-color: rgba(0, 0, 0, 0.8);
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        .logo {
            font-size: 1.5rem;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .logo span {
            color: #5865F2;
        }
        nav {
            display: flex;
            gap: 20px;
        }
        nav a {
            color: white;
            text-decoration: none;
            font-weight: 600;
            transition: color 0.3s;
        }
        nav a:hover {
            color: #5865F2;
        }
        .hero {
            text-align: center;
            padding: 100px 10%;
            background: url('https://via.placeholder.com/1920x1080') no-repeat center/cover;
            animation: fadeIn 2s ease-in-out;
        }
        .hero h1 {
            font-size: 3rem;
            animation: slideUp 1.5s ease-out;
        }
        .hero p {
            font-size: 1.25rem;
            margin-top: 10px;
            animation: slideUp 1.8s ease-out;
        }
        .cta {
            margin-top: 20px;
            display: inline-block;
            padding: 15px 30px;
            background-color: #5865F2;
            color: white;
            text-transform: uppercase;
            font-weight: 600;
            border-radius: 50px;
            text-decoration: none;
            transition: background 0.3s;
            animation: popIn 2s ease-in-out;
        }
        .cta:hover {
            background-color: #4752C4;
        }
        .features {
            padding: 50px 10%;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }
        .feature {
            background-color: #1e1e1e;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
            text-align: center;
            animation: popIn 1.5s ease-in-out;
        }
        .feature h3 {
            font-size: 1.5rem;
            margin-bottom: 10px;
        }
        .feature p {
            font-size: 1rem;
            line-height: 1.5;
        }
        footer {
            text-align: center;
            padding: 20px 10%;
            background-color: #111111;
            color: #888;
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        @keyframes slideUp {
            0% { transform: translateY(50px); opacity: 0; }
            100% { transform: translateY(0); opacity: 1; }
        }
        @keyframes popIn {
            0% { transform: scale(0.8); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }
    </style>
</head>
<body>
    <header>
        <div class=\"logo\">⚡ My<span>Bot</span></div>
        <nav>
            <a href=\"#\">Home</a>
            <a href=\"#features\">Features</a>
            <a href=\"#contact\">Contact</a>
        </nav>
    </header>

    <section class=\"hero\">
        <h1>Meet Your Ultimate Discord Companion 🤖</h1>
        <p>The most advanced, user-friendly, and customizable bot for your server!</p>
        <a href=\"#\" class=\"cta\">Get Started</a>
    </section>

    <section class=\"features\" id=\"features\">
        <div class=\"feature\">
            <h3>✨ Sleek Design</h3>
            <p>Experience a modern interface that's easy to use and visually appealing.</p>
        </div>
        <div class=\"feature\">
            <h3>⚙️ Powerful Features</h3>
            <p>From moderation to games, our bot has it all to keep your server lively.</p>
        </div>
        <div class=\"feature\">
            <h3>🔒 Secure & Reliable</h3>
            <p>Your data is safe with us, and our bot is built to perform 24/7.</p>
        </div>
    </section>

    <footer>
        <p>&copy; 2024 MyBot. All rights reserved. <span>&#x1F916;</span></p>
    </footer>
</body>
</html>"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)
