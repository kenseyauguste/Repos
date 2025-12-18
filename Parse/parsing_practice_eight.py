import json

json_string = ''' {
  "city": "Boston",
  "forecast": [
    {"day": "Mon", "temp": 72, "condition": "Sunny"},
    {"day": "Tue", "temp": 68, "condition": "Cloudy"},
    {"day": "Wed", "temp": 65, "condition": "Rain"}
  ]
} '''

data = json.loads(json_string)
forecast_file = 'rainy_days.txt'

with open(forecast_file, "w", newline='') as f: 
    for day in data["forecast"]:
        if day["condition"] == "Rain":
            f.write(f'{day["day"]}: {day["temp"]}F\n')

