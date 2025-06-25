import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(name, phone, address, time):
    if not TOKEN or not CHAT_ID:
        print("❌ Telegram token yoki chat ID mavjud emas.")
        return

    message = (
        f"🧖‍♀️ Yangi bron:\n"
        f"👤 Ism: {name}\n"
        f"📞 Tel: {phone}\n"
        f"📍 Manzil: {address}\n"
        f"🕐 Vaqt: {time}"
    )
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        response = requests.post(url, data={"chat_id": CHAT_ID, "text": message})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Telegramga yuborishda xatolik: {e}")
