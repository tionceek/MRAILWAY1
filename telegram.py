import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(name, phone, address, time):
    message = f"🧖‍♀️ Yangi bron:\n👤 Ism: {name}\n📞 Tel: {phone}\n📍 Manzil: {address}\n🕐 Vaqt: {time}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})