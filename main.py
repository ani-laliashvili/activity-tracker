import requests
import datetime

# user input
USERNAME = "habit-tracker-user"
TOKEN = "sdfsdkdkfj2355sgd34535sfs"
GRAPH = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

#create user
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

# securely authenticate via header
headers = {
    "X-USER-TOKEN":TOKEN
}

# create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id":GRAPH,
    "name":"Coding Graph",
    "unit":"Hr",
    "type":"float",
    "color":"ajisai"
}
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)'


# add today's data to graph
date = datetime.date.today()
#date = datetime.datetime(year=2022, month=4, day=24)
date = date.strftime("%Y%m%d")


pixel_data = {
    "date":date,
    "quantity":input("How many hours did you code today? ")
}
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
response = requests.post(url=post_pixel_endpoint, json=pixel_data, headers=headers)


# add today's data to graph
date = datetime.date.today()
#date = datetime.datetime(year=2022, month=4, day=24)
date = date.strftime("%Y%m%d")

# update pixel
updated_pixel_data = {
    "date":date,
    "quantity":"7.72"
}
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date}"
#response = requests.put(url=update_pixel_endpoint, json=updated_pixel_data, headers=headers)


# delete pixel
date = datetime.date.today()
#date = datetime.datetime(year=2022, month=4, day=24)
date = date.strftime("%Y%m%d")

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date}"
#response = requests.delete(url=delete_pixel_endpoint, headers=headers)


# view graph
#graph_view_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}.html"
#response = requests.get(url=graph_endpoint, json=graph_config, headers=headers)
#visit:https://pixe.la/v1/users/habit-tracker-user/graphs/graph1.html

