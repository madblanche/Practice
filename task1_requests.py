import requests
import json

r = requests.post('http://ip-api.com/json/54.34.12.10', data={'key': 'value'})
print(r.text)

parsed_json = json.loads(r.text)

city = parsed_json['city']
country = parsed_json['country']

print(city, country)

