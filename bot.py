import os
import time
import signal
import sys
import requests
import threading
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

# ================== CONFIG ==================
BOT_TOKEN = os.getenv("BOT_TOKEN")   # REQUIRED
CHAT_ID   = os.getenv("CHAT_ID")     # REQUIRED
# ============================================

app = Flask(__name__)

def ensure_env_or_die():
    if not BOT_TOKEN or not CHAT_ID:
        print("[BOOT] Missing BOT_TOKEN or CHAT_ID in environment.")
        sys.exit(1)

def send_message(text: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        r = requests.post(url, json=payload, timeout=10)
        print(f"[TG] {r.status_code}: {r.text[:200]}")
    except Exception as e:
        print(f"[TG ERROR] {e}")

def get_suvichar():
    try:
        # ✅ ZenQuotes API
        resp = requests.get("https://zenquotes.io/api/random", timeout=10)
        if resp.status_code == 200:
            data = resp.json()[0]
            return f"🌞 Aaj ka Suvichar:\n\n{data['q']}\n— {data['a']}"
        else:
            return "🙏 Aaj ka suvichar uplabdh nahi hai."
    except Exception as e:
        print(f"[API ERROR] {e}")
        return "🙏 Aaj ka suvichar uplabdh nahi hai."

def job_send_suvichar():
    suvichar = get_suvichar()
    send_message(suvichar)

def start_scheduler():
    scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
    scheduler.add_job(job_send_suvichar, "cron", hour=10, minute=0)  # Daily 10:00 AM
    scheduler.start()
    print("[SCHEDULER] Started - Suvichar job set at 10:00 AM IST")

@app.route("/")
def home():
    return "OK", 200

def handle_shutdown(sig, frame):
    print(f"[SHUTDOWN] Signal {sig}, exiting...")
    sys.exit(0)

signal.signal(signal.SIGTERM, handle_shutdown)
signal.signal(signal.SIGINT, handle_shutdown)

if __name__ == "__main__":
    ensure_env_or_die()
    t = threading.Thread(target=start_scheduler, daemon=True)
    t.start()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, threaded=True)