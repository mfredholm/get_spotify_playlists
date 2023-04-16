import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

def save_playlist(sp, playlist):
    fname = 'SP_' + playlist["name"] + '.json'
    pl_json = {}
    pl_json["name"] = playlist["name"]
    pl_json["spotify_id"] = playlist["id"]
    pl_json["tracks"] = []
    tracks = playlist["tracks"]
    for item in tracks["items"]:
        track = item["track"]
        tmp_track = {
            "artists": [a['name'] for a in track['artists']],
            "album": track["album"]["name"],
            "name": track["name"]
        }
        pl_json["tracks"].append(tmp_track)
        artists = str([a['name'] for a in track['artists']])
        name = track["name"]
        album = track["album"]["name"]
        if not name:
            continue
    with open(fname, 'w') as f:
        json.dump(pl_json, f, indent=4)
    print(fname)

# PLAYLIST:
# {'collaborative': False, 
#  'description': '', 
#  'external_urls': {'spotify': 'https://open.spotify.com/playlist/6Qb5iNT3WtaXKWheXbbpYm'}, 
#  'href': 'https://api.spotify.com/v1/playlists/6Qb5iNT3WtaXKWheXbbpYm', 
#  'id': '6Qb5iNT3WtaXKWheXbbpYm', 
#  'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2737f3030c0d675f3eb416ac255', 'width': 640}], 
#  'name': 'Jannok', 
#  'owner': {'display_name': 'b658216', 'external_urls': {'spotify': 'https://open.spotify.com/user/b658216'}, 'href': 'https://api.spotify.com/v1/users/b658216', 'id': 'b658216', 'type': 'user', 'uri': 'spotify:user:b658216'}, 
#  'primary_color': None, 
#  'public': False, 
#  'snapshot_id': 'MTAsNWFjZmVlNjE3ODM3OTRiYjVmNzMzYzhkMmE0YzgyMzM4ZjM2ODgwNQ==', 
#  'tracks': {'href': 'https://api.spotify.com/v1/playlists/6Qb5iNT3WtaXKWheXbbpYm/tracks', 'total': 15}, 
#  'type': 'playlist', 
#  'uri': 'spotify:playlist:6Qb5iNT3WtaXKWheXbbpYm'}

with open("config.json", "r") as f:
    config = json.load(f)

client_id = config["spotify_client_id"]
client_secret = config["spotify_client_secret"]
scope = config["spotify_scope"]
redirect_uri = config["spotify_redirect_uri"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, scope=scope, redirect_uri=redirect_uri))

#auth_url = sp.auth_manager.get_authorize_url()
#print(f"Please visit this URL to authorize the app: {auth_url}")
# Open the authorization URL in the user's default web browser
#import webbrowser
#webbrowser.open(auth_url)
# Wait for the user to complete the authorization flow
#input("Press enter to continue...")

playlists = sp.current_user_playlists()

for p in playlists["items"]:
    playlist = sp.playlist(p["id"])
    save_playlist(sp, playlist)
