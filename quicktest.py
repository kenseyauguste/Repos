import json

data_string = ''' {
  "cluster": {
    "nodes": [
      {"name": "node1", "status": "ready"},
      {"name": "node2", "status": "not ready"},
      {"name": "node3", "status": "ready"}
    ]
  }
} '''

data = json.loads(data_string)

for node in data["cluster"]["nodes"]:
    print(f'{node["name"]}: {node["status"]}')
