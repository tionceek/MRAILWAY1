import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_telegram_message(name, phone, address, time):
    message = (
        f"🧖‍♀️ Yangi bron:\n"
        f"👤 Ism: {name}\n"
        f"📞 Tel: {phone}\n"
        f"📍 Manzil: {address}\n"
        f"🕐 Vaqt: {time}"
    )
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.post(url, data={"chat_id": CHAT_ID, "text": message})
    if response.status_code != 200:
        print("Telegram xabari yuborishda xatolik:", response.text)
