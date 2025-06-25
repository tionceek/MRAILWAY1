from datetime import datetime, timedelta

available_slots = [f"{hour:02}:00" for hour in range(10, 19)]
booked = {}

def book_slot(time, name):
    if time not in available_slots:
        return False, "Bunday vaqt mavjud emas."
    if time in booked:
        return False, "Bu vaqt band qilingan."
    booked[time] = name
    return True, "Band qilindi ✅"
