# Spotify Top Artists with Live Events

This Flask application allows users to view their top artists on Spotify over different time periods (short-term, medium-term, and long-term). It also provides a feature to search for live events in the UK for each artist using the Ticketmaster API.

## Features

- Display your top Spotify artists for short-term (last 4 weeks), medium-term (last 6 months), and long-term (years).
- View live events in the UK for each artist via the Ticketmaster API.
- Navigate between different time ranges and view relevant live event details.

## Prerequisites

To run this project, you'll need:

- Python 3.7+
- A Spotify Developer account
- A Ticketmaster Developer account
- Flask and other dependencies

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/spotify-top-artists-live-events.git
cd spotify-top-artists-live-events
```

### 2. Install Dependencies
Make sure you have pip installed. Then, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
You'll need to create a .env file in the root directory of the project to store your API keys. This file should include your Spotify API credentials and your Ticketmaster API key.

Create a .env File
Create a file named .env in the root directory and add the following lines:

```bash
Copy code
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
REDIRECT_URI=http://127.0.0.1:5000/callback
TICKETMASTER_API_KEY=your_ticketmaster_api_key
```
Replace your_spotify_client_id, your_spotify_client_secret, your_ticketmaster_api_key with your actual API keys.

Spotify API Credentials:

- Go to the Spotify Developer Dashboard.
- Create a new application and get the Client ID and Client Secret.
- Set the Redirect URI to http://127.0.0.1:5000/callback in the Spotify Dashboard.

Ticketmaster API Key:

Go to the Ticketmaster Developer Portal.
Sign up or log in and create an application to get your API Key.

### 4. Run the Application
Start the Flask application by running:

```bash
python app.py
```
The application will be accessible at http://127.0.0.1:5000/.

### 5. Using the Application
- Visit the home page to see options for viewing your top artists over different time periods.
- Click on any artist's name to view their live events in the UK.
- Use the "Back to Artists" button to navigate back to your list of top artists.

- Change the Time Range: Modify the /top_artists/<time_range> route in app.py to customize the time ranges for viewing your top artists.
- Update Styles: Modify static/style.css to change the look and feel of the website.


Troubleshooting
- API Key Issues: Ensure that your API keys are correctly entered in the .env file.
- Redirect URI Mismatch: Make sure the Redirect URI in the Spotify Developer Dashboard matches http://127.0.0.1:5000/callback.
- Missing Events: The Ticketmaster API might not return events if no events are scheduled or if the search keyword is too specific.
