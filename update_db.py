import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config.secrets import client_id, client_secret
from db.connection import DBConnection


# 1. Setup authentication
# User-level client (listening history)
sp_user = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri="http://127.0.0.1:5000/callback",
        scope="user-read-recently-played"
    )
)
with DBConnection() as cursor:
    cursor.execute("SELECT MAX(played_at) AS last_played FROM recently_played_tracks")
    result = cursor.fetchone()
    last_timestamp_ms = 0
    if result and result['last_played']:
        # Convert to milliseconds since epoch
        import datetime
        last_played = str(result['last_played'])
        dt = datetime.datetime.strptime(last_played, "%Y-%m-%d %H:%M:%S")
        last_timestamp_ms = int(dt.timestamp() * 1000)
# 2. Call the endpoint
results = sp_user.current_user_recently_played(limit=50,after=last_timestamp_ms)

# Check if items exist
if not results['items']:
    print("No recently played tracks found. Try playing a song on Spotify first!")
else:
    for item in results['items']:
        track = item['track']

        data = (
            track['id'],
            track['name'],
            track['artists'][0]['name'],
            track['album']['name'],
            track['popularity'],
            track['duration_ms'],
            track['explicit'],
            track['album']['release_date'][:10],  # safe date
            item['played_at'].replace("T", " ").replace("Z", "") 
        )

        insert_query = """
            INSERT IGNORE INTO recently_played_tracks
            (track_id, track_name, artist_name, album_name, popularity,
            duration_ms, explicit, release_date, played_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        with DBConnection() as cursor:
            cursor.execute(insert_query, data)
            cursor.connection.commit()
            if cursor.rowcount > 0:
                print(f"Inserted track: {track['name']} by {track['artists'][0]['name']} played at {item['played_at']}")
            else:
                print(f"Track already exists: {track['name']} by {track['artists'][0]['name']} played at {item['played_at']}")

