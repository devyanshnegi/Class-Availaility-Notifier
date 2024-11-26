import requests

def msg_telegram(msg):
    token = "7139507360:AAFGf8j6d09qtqduceXn0bIpXE45C-pc0VY"
    url = f"https://api.telegram.org/bot{token}"
    params = {"chat_id": "7076324337", "text": msg}
    r = requests.get(url + "/sendMessage", params=params)
    return r