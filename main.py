from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from booking import book_slot, available_slots
from telegram_bot import send_telegram_message

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API is working ✅"}

@app.post("/book")
async def book(request: Request):
    data = await request.json()
    name = data.get("name")
    phone = data.get("phone")
    address = data.get("address")
    time = data.get("time")

    success, message = book_slot(time, name)
    if success:
        send_telegram_message(name, phone, address, time)
    return {"success": success, "message": message}

@app.get("/available")
def get_available_slots():
    return {"available": available_slots}
