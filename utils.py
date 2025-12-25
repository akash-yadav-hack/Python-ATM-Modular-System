import random
import datetime

def generate_otp():
    return random.randint(1111,9999)

def get_current_time():
    return datetime.datetime.now().strftime("%I:%M:%S:%p")