
# core/spotify.py
import requests
import base64

def get_spotify_access_token(client_id, client_secret):

    print("DEBUG: client_id =", client_id)
    print("DEBUG: client_secret =", client_secret[:5], "...")  # não exibir tudo por segurança
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post("https://accounts.spotify.com/api/token", data=data, headers=headers)
    response.raise_for_status()
    return response.json()['access_token']


def get_artist_albums(artist_id, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums?include_groups=album,single&limit=10"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['items']


def get_artist_top_tracks(artist_id, token, market="BR"):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    params = {
        "market": market
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()["tracks"]
