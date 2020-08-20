import requests
import json

endpoint_url = 'https://api.spotify.com/v1/recommendations?'
access_token = "ACCESS_TOKEN"
uris = []

# SONG FILTERS
limit = 10
market = "AU"
seed_genres = "rnb"
target_danceability = 0.2
seed_artists = '5dCvSnVduaFleCnyy98JMo'

# QUERY
query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}&seed_artists={seed_artists}'

response = requests.get(query,
    headers={"Content-Type":"application/json",
    "Authorization":f"Bearer {access_token}"})

json_response = response.json()
for i, j in enumerate(json_response['tracks']):
    uris.append(j['uri'])
    print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")