from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def dashboard():
    bot_name = "ChatGPT AI Bot"
    commands = [
        {
            "name": "/ping",
            "description": "Check bot latency",
            "type": "utility"
        },
        {
            "name": "/hello",
            "description": "Get a greeting from the bot",
            "type": "utility"
        },
        {
            "name": "/echo",
            "description": "Echo your message",
            "type": "utility"
        },
        {
            "name": "/info",
            "description": "Get bot information",
            "type": "utility"
        },
        {
            "name": "/ask",
            "description": "Ask AI a question",
            "type": "ai"
        },
        {
            "name": "/imagine",
            "description": "Generate creative text",
            "type": "ai"
        }
    ]
    
    return render_template('index.html', bot_name=bot_name, commands=commands)

@app.route('/api/status')
def get_status():
    return {
        "status": "online",
        "bot_name": "ChatGPT AI Bot",
        "features": ["Slash Commands", "AI Chat", "Web Dashboard"]
    }

if __name__ == '__main__':
    app.run(debug=True, port=5000)
