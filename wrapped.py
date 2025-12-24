import os
from db.connection import DBConnection
import datetime
def musical_age(birth_year,cursor):
    query = """
        SELECT CAST(SUBSTRING(release_date, 1, 4) AS UNSIGNED) AS release_year,
                COUNT(*) AS plays
        FROM recently_played_tracks
        WHERE release_date IS NOT NULL
        GROUP BY release_year
        ORDER BY plays DESC
        LIMIT 1
    """
    cursor.execute(query)
    result = cursor.fetchone()

    if not result or not result['release_year']:
        return None

    current_year = datetime.datetime.now().year
    musical_age = 2 * current_year - birth_year - result['release_year']
    print(f"Your musical age is: {musical_age if musical_age is not None else 'N/A'}")


def top_song_listened(cursor):
    query = """
            SELECT track_name, artist_name, COUNT(*) AS plays
            FROM recently_played_tracks
            GROUP BY track_id, track_name, artist_name
            ORDER BY plays DESC
            LIMIT 5
        """
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print("Top 5 Songs Listened:")
        print()
        for row in result:
            print(f"{row['track_name']} by {row['artist_name']} - {row['plays']} plays")
    else:
        print("No songs found in the database.")

def top_artist_listened(cursor):
    query = """
            SELECT artist_name, COUNT(*) AS plays
            FROM recently_played_tracks
            GROUP BY artist_name
            ORDER BY plays DESC
            LIMIT 5
        """
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print("Top 5 Artists Listened:")
        print()
        for row in result:
            print(f"{row['artist_name']} - {row['plays']} plays")
    else:
        print("No artists found in the database.")

def top_popularity_listened(cursor):
    query = """
            SELECT track_name, artist_name, popularity, COUNT(*) AS plays
            FROM recently_played_tracks
            GROUP BY track_id, track_name, artist_name, popularity
            ORDER BY popularity DESC, plays DESC
            LIMIT 5
        """
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print("Top 5 Most Popular Songs Listened:")
        print()
        for row in result:
            print(f"{row['track_name']} by {row['artist_name']} - Popularity: {row['popularity']}, Plays: {row['plays']}")
    else:
        print("No songs found in the database.")


with DBConnection() as cursor:
    os.system('cls')
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    musical_age(2001,cursor)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    input("Press Enter to Next...")
    os.system('cls')
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    top_song_listened(cursor)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    input("Press Enter to Next...")
    os.system('cls')
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    top_artist_listened(cursor)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    input("Press Enter to Next...")
    os.system('cls')
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    top_popularity_listened(cursor)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    input("Press Enter to Summarize...")
    os.system('cls')
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    musical_age(2001, cursor)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    top_song_listened(cursor)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    top_artist_listened(cursor)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    top_popularity_listened(cursor)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    input("Press Enter to Exit...")
    os.system('cls')
    cursor.close()