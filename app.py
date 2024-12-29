from flask import Flask, render_template_string, redirect, url_for, jsonify

app = Flask(__name__)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Aeroplane Company</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            font-family: 'Inter', sans-serif;
            background: linear-gradient(to bottom, #1e1e1e, #000000);
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
            color: #00aaff;
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
            color: #00aaff;
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
            background-color: #00aaff;
            color: white;
            text-transform: uppercase;
            font-weight: 600;
            border-radius: 50px;
            text-decoration: none;
            transition: background 0.3s;
            animation: popIn 2s ease-in-out;
        }
        .cta:hover {
            background-color: #0088cc;
        }
        .features {
            padding: 50px 10%;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }
        .feature {
            background-color: #2a2a2a;
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
        .feature .btn {
            margin-top: 15px;
            padding: 10px 20px;
            background-color: #00aaff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .feature .btn:hover {
            background-color: #0088cc;
        }
        .widgets {
            padding: 50px 10%;
            background: #121212;
            text-align: center;
        }
        .widget {
            display: inline-block;
            margin: 10px;
            padding: 20px;
            border: 2px solid #00aaff;
            border-radius: 10px;
            color: white;
            background-color: #1e1e1e;
            cursor: pointer;
            transition: transform 0.3s, background-color 0.3s;
        }
        .widget:hover {
            transform: scale(1.1);
            background-color: #0088cc;
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
    <script>
        function showInfo(section) {
            alert("You clicked on " + section + "!");
        }

        function widgetClick(widgetName) {
            fetch('/widget-action', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ widget: widgetName })
            }).then(response => response.json())
              .then(data => alert(data.message))
              .catch(error => alert("Error: " + error));
        }
    </script>
</head>
<body>
    <header>
        <div class="logo">✈️ The<span>Aeroplane Company</span></div>
        <nav>
            <a href="#">Home</a>
            <a href="#features">Features</a>
            <a href="https://discord.gg/bqqupx7yNu" target="_blank">Invite</a>
            <a href="https://github.com/applxcake/Discord-Bot-Class-12-Cs-project" target="_blank">GitHub</a>
        </nav>
    </header>

    <section class="hero">
        <h1>Revolutionize Your Discord Experience</h1>
        <p>The Aeroplane Company: Flight Booking and Beyond!</p>
        <a href="https://discord.gg/bqqupx7yNu" class="cta" target="_blank">Join Us</a>
    </section>

    <section class="features" id="features">
        <div class="feature">
            <h3>📅 Flight Booking</h3>
            <p>Seamlessly book flights directly within your Discord server.</p>
            <button class="btn" onclick="showInfo('Flight Booking')">Learn More</button>
        </div>
        <div class="feature">
            <h3>🌎 Dynamic Pricing</h3>
            <p>Experience real-time ticket pricing based on distance calculations.</p>
            <button class="btn" onclick="showInfo('Dynamic Pricing')">Learn More</button>
        </div>
        <div class="feature">
            <h3>🔒 Reliable and Secure</h3>
            <p>Trust our bot to keep your data and bookings safe.</p>
            <button class="btn" onclick="showInfo('Reliable and Secure')">Learn More</button>
        </div>
        <div class="feature">
            <h3>💬 Intuitive Interactions</h3>
            <p>Interact with modals and embeds designed for ease of use.</p>
            <button class="btn" onclick="showInfo('Intuitive Interactions')">Learn More</button>
        </div>
    </section>

    <section class="widgets">
        <div class="widget" onclick="widgetClick('Widget 1')">Widget 1</div>
        <div class="widget" onclick="widgetClick('Widget 2')">Widget 2</div>
        <div class="widget" onclick="widgetClick('Widget 3')">Widget 3</div>
    </section>

    <footer>
        <p>&copy; 2024 The Aeroplane Company. All rights reserved. <span>✈️</span></p>
    </footer>
</body>
</html>"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/widget-action', methods=['POST'])
def widget_action():
    from flask import request
    data = request.json
    widget_name = data.get('widget', 'Unknown')
    return jsonify(message=f"You interacted with {widget_name}!")

if __name__ == '__main__':
    app.run(debug=True)
