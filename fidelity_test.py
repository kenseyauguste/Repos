import json
import requests 

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)
data = response.json()

#data is now a json object now
with open("filename.txt", "w", newline='') as f: 
    f.write(json.dumps(data, indent=2))
