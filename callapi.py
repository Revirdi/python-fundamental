import requests
# def get_data(self, api):
#     response = requests.get(f"{api}")
#     if response.status_code == 200:
#         self.formatted_print(response.json())
#     else:
#         print(f"{response.status_code} error")
    
# get_data("https://reqres.in/api/users?page=1")

api_url = "https://reqres.in/api/users?page=1"
response = requests.get(api_url)
response.json()
print(response.json())