
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year would you like to travel to? Input the date in this format: yyyy-mm-dd format ")
year = date.split("-")[0]
response = requests.get("https://www.billboard.com/charts/hot-100/" + date + "/")
soup = BeautifulSoup(response.text, "html.parser")
list_of_songs = []
songs = soup.select("li ul li h3")

for song in songs:
    list_of_songs.append(song.text.strip())


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="ca1a99148b824768b3b397f80cf75ad6",
        client_secret="7061ce500b5f4e3fb1be95f76fd4e4ed",
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        cache_path="token.txt",
        username="Saurav"
    ))
user = sp.current_user()["id"]
print(user)
song_uris = []

for song in list_of_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f" The song:{song} doesn't exist")

playlist = sp.user_playlist_create(user=user,name="billboard-2023-07-05",public=False)
sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)


