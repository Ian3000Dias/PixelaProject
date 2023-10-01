import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "iandias"
TOKEN = "hibyegoodbye"
GRAPH_ID = "graph1"
today = datetime.now()
print()

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id":,
#     "name":"Cycling Graph",
#     "unit":"Km",
#     "type":"float",
#     "color":"momiji",
#     "timezone":"Asia/Kolkata"
# }
#
headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_details = {
    "date":f"{today.strftime('%Y%m%d')}",
    "quantity":input("How many kilometers did you cycle today? ")
}
pixel_url = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

response = requests.post(url=pixel_url, json=pixel_details, headers=headers)
print(response.text)
