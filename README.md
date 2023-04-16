# Save Spotify playlists

Just a simple script to dump Spotify playlists in JSON.

## Configuration

Create the file config.json with configuration for using the Spotify API, e.g.:

```
{
    "spotify_client_id": "<your client_id",
    "spotify_client_secret": "your:_client_secret",
    "spotify_scope": "user-library-read playlist-read-private",
    "spotify_redirect_uri": "http://localhost"
}
```

## Requirements

In your environment install required modules:

```
pip install -r requirements.txt
```

## Execution

```
python3 get_spotify_playlists.py
```

This will open your browser, just copy-paste the URL to script input.

