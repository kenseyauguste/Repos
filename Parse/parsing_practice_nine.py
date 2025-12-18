import json
import requests

data_string = ''' {
  "departments": [
    {"name": "Engineering", "employees": ["Alice", "Bob"]},
    {"name": "HR", "employees": ["Charlie"]},
    {"name": "Sales", "employees": ["David", "Eva"]}
  ]
} '''

data = json.loads(data_string)

with open("log.txt", "w", newline='') as f:
    for dept in data["departments"]:
      f.write(f'{dept['name']}: {dept['employees']}\n')  
