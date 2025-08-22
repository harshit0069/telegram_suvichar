# 🌞 Daily Suvichar Telegram Bot

A simple Telegram bot that sends a **daily Suvichar (quote)** at **10:00 AM IST**.  
Built with **Python, Flask, APScheduler**, and deployed on **Render**.  
UptimeRobot can be used to keep the bot always alive by pinging the `/` endpoint.

---

## ✨ Features
- Sends a random Suvichar from an API every day at **10:00 AM IST**.
- Minimal Flask server for Render deployment.
- Easy to configure with environment variables.

---

## 🛠️ Setup

### 1. Clone this repo
```
git clone https://github.com/harshit0069/telegram_suvichar.git
cd telegram_suvichar
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Setup environment variables

Create a .env file (see .env.example):
```
BOT_TOKEN=your-telegram-bot-token
CHAT_ID=your-chat-id
```

4. Run locally

python bot.py


---

🚀 Deploy on Render

1. Push your code to GitHub.


2. Create a Web Service on Render.


3. Add environment variables:
```
BOT_TOKEN = your Telegram bot token
CHAT_ID = your chat/group ID
```

4. Start Command:
```
python bot.py
```

5. After deploy, add your Render URL (https://yourapp.onrender.com/) in UptimeRobot (ping every 5 mins).