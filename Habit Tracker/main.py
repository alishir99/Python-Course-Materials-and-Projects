import requests
from datetime import date
TOKEN = "asdljfasdfksldghaklfhaf"
USERNAME= "pykobra"
pixela_endpoint = "https://pixe.la/v1/users"

user_params= {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Gym",
    "unit": "hour",
    "type": "float",
    "color": "shibafu",
}
headers = {
   "X-USER-TOKEN": TOKEN
}

reponse= requests.post(url= graph_endpoint, json = graph_config, headers= headers)
print(reponse.text)

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
today = date.today()
date = today.strftime('%Y%m%d')

graph_post = {
    "date": date,
    "quantity": input("How many hours did you work out today?> "),
}

response = requests.post(url=post_endpoint, json=graph_post, headers=headers)
print(response.text)

# put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{graph_post['date']}"
#
# put_body= {
#     "quantity": "1",
# }
#
# # response = requests.put(url=put_endpoint, json=put_body, headers=headers)
# # print(response.text)
#
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
# #
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)