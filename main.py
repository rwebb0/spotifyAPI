"""
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")

# Set the scope to access top artists
scope = "user-top-read"

# Authenticate and create a Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

def get_top_artists(sp, time_range="long_term", limit=50):
    results = sp.current_user_top_artists(time_range=time_range, limit=limit)
    return results["items"]

# Get the user's top artists for the past 4 weeks (short_term)
top_artists = get_top_artists(sp, time_range="long_term")

# Print the top artists
for idx, artist in enumerate(top_artists):
    print(f"{idx + 1}: {artist['name']}")
"""