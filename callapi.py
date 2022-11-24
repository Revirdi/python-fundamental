import requests
import re

api_url = "https://reqres.in/api/users?page=1"
response = requests.get(api_url).json()
data = response["data"]

print(data) 

print([element for element in response["data"] if element["id"] == 5]) 

for data in data:
    img = re.split("[/]", data["avatar"])
    id = data["id"]
    print(f"User {id} = {img[-1]}")
