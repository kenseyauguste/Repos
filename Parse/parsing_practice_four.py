import json 

json_info = ''' {
  "services": {
    "auth": {"status": "ok", "port": 8080},
    "db": {"status": "failed", "port": 5432},
    "cache": {"status": "ok", "port": 6379}
  }
} '''

data = json.loads(json_info)
log = 'log.txt'

with open(log, "w", newline='') as f:
    for service, details in data["services"].items():
        if details["status"] == "ok":
            f.write(f'{service} is running on port: {details["port"]}\n')
     