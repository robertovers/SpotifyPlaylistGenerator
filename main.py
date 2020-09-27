import requests
import json

endpoint_url = "https://api.spotify.com/v1/recommendations?"
access_token = "ACCESS TOKEN HERE"
uris = []


# SONG FILTERS
limit = 10
market = "AU"
seed_genres = "rnb"
target_danceability = 0.2
seed_artists = '7daSp9zXk1dmqNxwKFkL35'


# QUERY
query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres} \
        &target_danceability={target_danceability}&seed_artists={seed_artists}'

response = requests.get(query,
    headers={"Content-Type":"application/json",
    "Authorization":f"Bearer {access_token}"})

json_response = response.json()
for i, j in enumerate(json_response['tracks']):
    uris.append(j['uri'])
    print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")


# CREATE PLAYLIST
user_id = "USER ID HERE"
endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

request_body = json.dumps({
          "name": "",
          "description": "",
          "public": False
        })

response = requests.post(url=endpoint_url, data=request_body, headers={"Content-Type":"application/json", "Authorization":"Bearer " + access_token})
print(response.status_code)


# ADD TRACKS
playlist_id = response.json()['id']
endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_body = json.dumps({
          "uris":uris
        })

response = requests.post(url=endpoint_url, data=request_body, headers={"Content-Type":"application/json", "Authorization":f"Bearer {access_token}"})
print(response.status_code)
