import datetime

def clean_amount(value):
    """Convert input to float, removing commas"""
    return float(value.replace(",", "").strip())

def now_str():
    """Return current date-time as string"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def green(text):
    return f"\033[92m{text}\033[0m"
