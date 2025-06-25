from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from telegram_bot import send_telegram_message
from booking import book_slot, available_slots

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"message": "Dr. Mushtariy API is running"}

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
