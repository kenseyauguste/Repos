import json

json_data = ''' [
  {"id": 1, "type": "error", "message": "disk full"},
  {"id": 2, "type": "info", "message": "system rebooted"},
  {"id": 3, "type": "error", "message": "cpu overload"}
] '''

data = json.loads(json_data)

with open("log.txt", "w", newline='') as f:
    for item in data:
        if item[type] == "error":
            f.write(f"Printing out message: {item['message']}\n")


 