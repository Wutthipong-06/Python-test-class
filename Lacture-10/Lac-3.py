import json

data = {
    "name": "Alice", 
    "age": 26
    }
json_str = json.dumps(data)
print(json_str)

paread_data = json.loads(json_str)
print(paread_data)
print(paread_data['name'])
print(paread_data['age'])