import requests
import time

def send_command():
    url = "http://127.0.0.1:1242/Api/Command"
    headers = {"password": "your_ipc_password"}
    data = {"Command": "your_command"}
    response = requests.post(url, headers=headers, json=data)
    print(response.json())

while True:
    send_command()
    time.sleep(20 * 60 * 60)  # 20 hours (change it)
