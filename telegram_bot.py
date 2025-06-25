import os
import requests
from dotenv import load_dotenv  # .env fayldan o‘qish uchun

# .env fayldagi o‘zgaruvchilarni yuklash
load_dotenv()

# Token va chat ID ni olish
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

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

    # Xatolikni tekshirish (agar kerak bo‘lsa log chiqarish)
    if response.status_code != 200:
        print("Telegram xabari
