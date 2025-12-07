import requests

url = "redacted"

payload = {
    "data":{
    "natural_gas_binary": 1,
    "LargestPropertyUseTypeGFA": 12000,
    "PropertyGFATotal": 50000,
    "electricity_binary": 1,
    "PropertyGFABuilding": 48000,
    "ENERGYSTARScore": 75,
    "building_age": 45,
    "NumberofFloors": 10
}}

response = requests.post(url, json=payload)

print("Status code:", response.status_code)
print("Response:", response.json())
