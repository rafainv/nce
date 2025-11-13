import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("URL")
token = os.getenv("TOKEN")

payload = {"task_id":5153,"reward":5000}

headers = {
    #'User-Agent': "Dart/3.7 (dart:io)",
    'Content-Type': "application/json",
    'os-version': "13_33"
    'app-version': "1.0.2"
    'lang': "pt",
    'authorization': token,
    'platform': "Android"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)



