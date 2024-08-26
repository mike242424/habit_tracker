import os
import datetime as dt
import requests
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

today = dt.date.today()
formatted_date = today.strftime(format="%Y%m%d")

# create user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": TOKEN,
    "notMinor": "yes"
}

pixela_endpoint = 'https://pixe.la/v1/users'

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# create a graph for user specific user
headers = {
    'X-USER-TOKEN': TOKEN
}
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_params = {"id": "graph1", "name": "Python Coding Graph", "unit": "Hr", "type": "int", "color": "sora"}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())

# response = requests.get(f'https://pixe.la/@{USERNAME}')
# print(response.text)

# post value to graph
my_graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_params["id"]}'
data = {f"date": formatted_date, "quantity": input('How many hours did you code today? ')}
# response = requests.post(url=my_graph_endpoint, json=data, headers=headers)
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())

# update a value on graph by date
my_graph_value_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_params["id"]}/20240824'
updated_data = {"quantity": "15"}
# response = requests.put(url=my_graph_value_endpoint, json=updated_data, headers=headers)
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())

# delete a value on graph by date
# response = requests.delete(url=my_graph_value_endpoint, headers=headers)
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())
