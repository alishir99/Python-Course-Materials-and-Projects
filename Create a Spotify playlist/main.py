from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import pprint
Client_ID = "bdb7894c8ded44d6842ddbcfd8a6569b"
Client_Secret = "4ef4d9428dc4445bbccfb3f1ea3f0fa1"


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
billboard_web= response.text
soup = BeautifulSoup(billboard_web, "html.parser")
songs_list=soup.findAll("h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-"
                                     "18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis"
                                     " u-max-width-330 u-max-width-230@tablet-only")
songs_names = [song.getText().strip() for song in songs_list]
print(songs_names)


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://alishirzad99.github.io/My-website/",
        client_id=Client_ID,
        client_secret=Client_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
# print(user_id)
# year = date.strip("-")[0]
#
# #Get Spotify song URIs for each song in the list
# song_uris = []
# for song in songs_names:
#
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")
#
# # Print the list of Spotify song URIs
# print(song_uris)
#
# #Creating a new private playlist in Spotify
# playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)
#
# #Adding songs found into the new playlist
# sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)