🎧 Spotify Insights: A Personal Analytics Dashboard
===================================================
<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white" />
  </a>
  <a href="https://developer.spotify.com/">
    <img src="https://img.shields.io/badge/Spotify-Web%20API-1DB954?logo=spotify&logoColor=white" />
  </a>
  <a href="https://www.mysql.com/">
    <img src="https://img.shields.io/badge/Database-MySQL-blue?logo=mysql&logoColor=white" />
  </a>
  <a href="https://github.com/PRIYADARSHAN-MAHENDRAN/Spotify_Insights-A_Personal_Analytics_Dashboard/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/PRIYADARSHAN-MAHENDRAN/Spotify_Insights-A_Personal_Analytics_Dashboard" />
  </a>
</p>


Spotify Insights is a Python-based tool that fetches your recently played Spotify tracks, stores them in a local MySQL database, and generates personalized "Wrapped-style" analytics. Discover your top songs, favorite artists, and even your "musical age" based on your listening habits.

*   Your **musical age**
    
*   Top **songs** listened to
  
*   Top **artists** listened to  
    
*   **Most popular** tracks you listen to
    

📌 Table of Contents
--------------------

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Schema](#database-schema)
- [Usage](#usage)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
    

Introduction
---------------

This project uses the [**Spotipy**](https://github.com/spotipy-dev/spotipy) library to fetch your Spotify listening history and persist it in a MySQL database. Over time, the collected data is analyzed to generate personalized insights about your listening habits.

It is designed to be run locally and assumes you have an existing Spotify Developer application and a MySQL instance running.

Features
----------

*   OAuth-based Spotify authentication
    
*   Incremental syncing of recently played tracks
    
*   Duplicate-safe database inserts
    
*   CLI-based analytics dashboard
    
*   Calculates a fun **Musical Age** metric
    
*   Displays:
    
    *   Musical age
        
    *   Top 5 songs
        
    *   Top 5 artists
        
    *   Top 5 most popular tracks
        

Project Structure
--------------------

```
│
└── config/
│   ├── secrets.py     # Spotify API credentials (not included)
│   └── db_config.py        # Database credentials
├── db/
│   └── connection.py  # MySQL connection wrapper (context manager)
├── update_db.py        # Fetches Spotify listening history and updates DB
└── wrapped.py          # CLI analytics & reporting
```

Installation
---------------

### 1\. Clone the repository

```bash
git clone https://github.com/your-username/spotify-insights.git
cd spotify-insights
```

### 2\. Create a virtual environment (recommended)

```bash
python -m venv venv  source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3\. Install dependencies

```bash
pip install spotipy mysql-connector-python
```

Configuration
----------------

### Spotify Credentials

Create a Spotify Developer app and add your credentials to:

```python
# config/secrets.py
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
```
> **Note:** Ensure your Spotify App's Redirect URI is set to http://127.0.0.1:5000/callback in the Developer Dashboard.

### Database Configuration

Edit db\_config.py:

```python
db_config = {
  "host": "localhost",
  "user": "root",
  "password": "root",
  "database": "spotify"
  }
```

Database Schema
------------------

You must create the following table before running the project:

```sql
CREATE TABLE recently_played_tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_id VARCHAR(255),
    track_name VARCHAR(255),
    artist_name VARCHAR(255),
    album_name VARCHAR(255),
    popularity INT,
    duration_ms INT,
    explicit BOOLEAN,
    release_date DATE,
    played_at DATETIME,
    UNIQUE(played_at)
);
```

Usage
--------

### 1\. Update the Database with Spotify Data

```bash
python update_db.py
```

What it does:

*   Authenticates your Spotify account
    
*   Fetches up to 50 recent tracks **after the last saved play**
    
*   Inserts only new tracks into the database
    

### 2\. View Listening Analytics

```bash
python wrapped.py
```

Interactive CLI walkthrough that shows:

*   Musical Age
    
*   Top Songs
    
*   Top Artists
    
*   Most Popular Tracks
    

Examples
-----------

**Musical Age Output**

```   Your musical age is: 23   ```

**Top Songs**

```   Blinding Lights by The Weeknd - 12 plays   ```

**Top Artists**

```   Drake - 34 plays   ```

Troubleshooting
------------------

**No recently played tracks found**

*   Play a song on Spotify
    
*   Ensure the correct Spotify account is authenticated
    

**Database connection errors**

*   Verify MySQL is running
    
*   Check credentials in db\_config.py
    

**OAuth redirect issues**

*   Ensure redirect URI matches Spotify Developer Dashboard exactly
    

Dependencies
---------------

*   Python 3.9+
    
*   spotipy
    
*   mysql-connector-python
    
*   MySQL Server
    
*   Spotify Developer Account
    
Contributing
---------------
Contributions are welcome and appreciated! If you would like to contribute to Spotify\_Insights – A Personal Analytics Dashboard, please follow these steps:

1.  Fork the repository.
    
2.  Create a new branch for your changes.
    
3.  Make your desired changes and commit them.
    
4.  Push your changes to your forked repository.
    
5.  Submit a pull request with a clear and detailed description of your changes.

License
----------

This project is licensed under the MIT License - see the [LICENSE](https://github.com/PRIYADARSHAN-MAHENDRAN/Spotify_Insights-A_Personal_Analytics_Dashboard/blob/main/LICENSE) file for details.
