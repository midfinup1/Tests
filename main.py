from yandex import Yandex
import requests


data = {'path': 'test_folder'}
HEADERS = {"Authorization": f"OAuth {'AgAAAAAa6zIQAADLW7XGfiL5V03inKkQ2URzD6o'}"}
response = requests.put('https://cloud-api.yadex.net/v1/disk/resources', headers=HEADERS, params=data)

print(response.status_code)
print(response.json())
