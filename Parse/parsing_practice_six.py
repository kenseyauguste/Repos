import json
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

data = response.json()

with open("healthy.json", "w", newline='') as f:
    for item in data:
        if item['userId'] == 1:
            json.dump(item, f, indent=2)