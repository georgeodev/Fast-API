import requests
import json
#URL for the Games API
url = "http://127.0.0.1:8000/api/v1/games"
response_get_api = requests.get(url)
print(response_get_api.json())
input()
#Data to be updated in a specified game ID
data = {'game_size': '500 GB'}
#Updating the data in a specified game ID
response_update_api = requests.put(
  f"{url}/8d7b25c5-508c-43b1-bf12-71001c4ce9f8", data=json.dumps(data))
print(response_update_api)
input()
#Deleting a specified game from the list using the game ID
response_delete_api = requests.delete(
  f"{url}/0f76ab39-b08e-423d-9ffe-426f9a50d095")
print(response_delete_api)
input()
#getting the new list of games
response_get_api = requests.get(url)
print(response_get_api.json())
