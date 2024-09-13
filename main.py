from bs4 import BeautifulSoup
from datetime import *
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"
request = requests.get(URL)
soup = BeautifulSoup(request.text, "html.parser")
spotify_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_url = os.getenv("SPOTIFY_REDIRECT_URI")
scope = "playlist-modify-public playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=spotify_id,
    client_secret=spotify_secret,
    redirect_uri=redirect_url,
    scope=scope
))
song_elements = soup.select("li.lrv-u-width-100p h3#title-of-a-story")
song_names = [song.get_text().strip() for song in song_elements]
user_id = sp.current_user()['id']
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
if song_uris:
    # Create the playlist and get the playlist ID
    playlist = sp.user_playlist_create(
        user=user_id,
        name=f"Songs from {date}",
        public=False,
        description="Playlist from specified date time, created using Spotify API and Spotipy"
    )
    playlist_id = playlist['id']

    # Add items to the playlist
    sp.playlist_add_items(playlist_id, song_uris)
    print("Songs added to the playlist successfully!")
else:
    print("No songs were added to the playlist because no URIs were found.")