
key_to_modify = "name"
index_to_pop = 1

employees = [ {
    "name": "Kensey Andrew Auguste",
    "accessLevel": "staging, Production"
}
]


for item in employees:
    if len(item["name"]) > 1:
         new_item = item["name"][:1] + item["name"][2:]
         item["name"] = new_item

print(item) 