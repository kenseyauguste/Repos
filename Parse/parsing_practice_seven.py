import json
import csv

json_string = ''' [
  {"name": "Alice", "email": "alice@example.com"},
  {"name": "Bob", "email": "bob@example.com"},
  {"name": "Charlie", "email": "charlie@example.com"}
] '''

data = json.loads(json_string)
csv_file = 'file.csv'
fieldnames = ['name', 'email']

with open(csv_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for item in data:
        writer.writerow(item)

