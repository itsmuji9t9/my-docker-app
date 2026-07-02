import random
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Funny roasts for your computer science/engineering friends
ROASTS = [
    "Error 404: Your tech-career motivation not found. 💀",
    "Tu sirf code likhta hai, ya bugs khud chal kar tere paas aate hain? 🐛",
    "Writing code without comments is like driving at night with headlights off. Good luck!",
    "Git push direct to main? Lagta hai sidha fire brigade ko call karni paregi! 🔥",
    "Local machine par chal raha hai? Toh server par kya laptop rakh kar aayen? 💻",
    "Your code is so clean that even the compiler refuses to look at it. 🤖",
    "Aapka logic aur Pakistan ka mausam... dono hi unpredictable hain! ☀️🌧️"
]

@app.route("/", methods=["GET", "POST"])
def home():
    selected_roast = random.choice(ROASTS)
    click_count = request.form.get("click_count", 0, type=int)
    alert_message = ""

    if request.method == "POST":
        click_count += 1
        # Funny response triggers based on how many times they click
        if click_count == 1:
            alert_message = "Chalo, shuruat toh hui! 😂"
        elif click_count == 5:
            alert_message = "Bas kar bhai, mouse toot jayega! 🖱️💥"
        elif click_count >= 10:
            alert_message = "Lagta hai free ho bilkul... Coding seekh lo isse behtar hai! 🧠"

    # Attractive Dark Hacker Theme HTML
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mujahid's Automated App 🚀</title>
        <style>
            body {
                background-color: #0d1117;
                color: #c9d1d9;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                padding: 20px;
                text-align: center;
            }
            .container {
                background-color: #161b22;
                border: 2px solid #58a6ff;
                border-radius: 12px;
                padding: 30px;
                box-shadow: 0 8px 24px rgba(88, 166, 255, 0.2);
                max-width: 500px;
                width: 100%;
            }
            h1 {
                color: #58a6ff;
                margin-bottom: 5px;
            }
            .badge {
                background-color: #238636;
                color: white;
                padding: 4px 10px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: bold;
                display: inline-block;
                margin-bottom: 20px;
            }
            .roast-box {
                background-color: #21262d;
                border-left: 5px solid #ff7b72;
                padding: 15px;
                margin: 20px 0;
                border-radius: 4px;
                font-style: italic;
                font-size: 18px;
            }
            button {
                background-color: #238636;
                color: white;
                border: none;
                padding: 12px 24px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 6px;
                cursor: pointer;
                transition: background-color 0.2s;
            }
            button:hover {
                background-color: #2ea043;
            }
            .alert-msg {
                color: #ff7b72;
                font-weight: bold;
                margin-top: 15px;
                height: 20px;
            }
            .footer {
                margin-top: 30px;
                font-size: 12px;
                color: #8b949e;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Mujahid's Cloud App 🚀</h1>
            <div class="badge">CI/CD Pipeline: Active 🟢</div>
            
            <p style="color: #8b949e;">Refresh the page to get a fresh DevOps Roast!</p>
            
            <div class="roast-box">
                "{{ roast }}"
            </div>

            <form method="POST">
                <input type="hidden" name="click_count" value="{{ count }}">
                <button type="submit">Don't Click This Button ⛔ (Clicks: {{ count }})</button>
            </form>

            <div class="alert-msg">{{ alert }}</div>

            <div class="footer">
                Deployed instantly via GitHub Actions to AWS EC2
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, roast=selected_roast, count=click_count, alert=alert_message)

if __name__ == "__main__":
    # Runs on port 8080 locally
    app.run(host="0.0.0.0", port=80)
