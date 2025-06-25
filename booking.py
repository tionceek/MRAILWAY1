from datetime import datetime

available_slots = [
    f"{hour:02d}:00" for hour in range(10, 18)
]

booked = {}

def book_slot(time, name):
    if time not in available_slots:
        return False, "Noto‘g‘ri vaqt"
    if time in booked:
        return False, "Bu vaqt allaqachon band qilingan"
    booked[time] = name
    return True, "Band qilindi"