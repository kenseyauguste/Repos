import json 
import csv

json_string = ''' [
  {"id": 1, "status": "ok"},
  {"id": 2, "status": "failed"},
  {"id": 3, "status": "ok"}
] '''

data = json.loads(json_string)

with open("healthy.json", "w", newline='') as f:
   for item in data:
     if item["status"] == "ok":
        json.dump(item, f, indent=3)

