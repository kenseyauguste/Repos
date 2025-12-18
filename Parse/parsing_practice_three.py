import json
import csv

json_string = ''' [
  {"user": "alice", "email": "alice@example.com"},
  {"user": "bob", "email": "bob@example.com"}
]
'''

data = json.loads(json_string)
fieldnames = ["user","email"]

with open("file.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for row in data:
        f.write(f"{row['user']},{row['email']}\n")



