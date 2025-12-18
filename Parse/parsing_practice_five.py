import json
import requests

url = 'https://api.github.com/users/octocat'
response = requests.get(url)
data = response.json()

json_string = json.dumps(data, indent=2)

print(f"{json_string}\n")

print(f"User is: {data['login']}, ID is: {data['id']}, Public Repos is: {data['public_repos']}\n")
 

