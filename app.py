import os
from flask import Flask, render_template, request
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import requests

load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Load environment variables
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
ticketmaster_api_key = os.getenv("TICKETMASTER_API_KEY")

# Set the scope to access top artists
scope = "user-top-read"

# Authenticate and create a Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))


# Function to search for live events in the UK for an artist using Ticketmaster API
def search_live_events(artist_name):
    url = f"https://app.ticketmaster.com/discovery/v2/events.json"
    params = {
        "apikey": ticketmaster_api_key,
        "keyword": artist_name,
        "countryCode": "GB",
        "sort": "date,asc"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "_embedded" in data:
            events = [
                {
                    "name": event["name"],
                    "date": event["dates"]["start"]["localDate"],
                    "url": event["url"],
                    "venue": event["_embedded"]["venues"][0]["name"]
                }
                for event in data["_embedded"]["events"]
            ]
            return events
    return []


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/top_artists/<time_range>')
def top_artists(time_range):
    if time_range not in ['short_term', 'medium_term', 'long_term']:
        time_range = 'short_term'

    title = {
        'short_term': 'My Top Artists This Week',
        'medium_term': 'My Top Artists This Month',
        'long_term': 'My Top Artists All Time'
    }[time_range]

    top_artists = sp.current_user_top_artists(time_range=time_range, limit=10)["items"]
    return render_template('artists.html', artists=top_artists, title=title, time_range=time_range)


@app.route('/live_events/<artist_name>')
def live_events(artist_name):
    events = search_live_events(artist_name)
    return render_template('events.html', artist_name=artist_name, events=events)


if __name__ == '__main__':
    app.run(debug=True)
