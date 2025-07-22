from django.shortcuts import render
from django.conf import settings
from .spotify import get_spotify_access_token, get_artist_albums, get_artist_top_tracks


# Create your views here.
def landing(request):
    return render(request, "landing.html")

def drumkits(request):
    return render(request, "drumkits.html")

def samples(request):
    return render(request, "samples.html")

def plugins(request):
    return render(request, "plugins.html")

def listen(request):
    token = get_spotify_access_token(settings.SPOTIFY_CLIENT_ID, settings.SPOTIFY_CLIENT_SECRET)
    artist_id = "5arfYeRczWtKre7ptGoEXp"  # example ID
    top_tracks = get_artist_top_tracks(artist_id, token)
    return render(request, 'listen.html', {'tracks': top_tracks})


def contact(request):
    return render(request, "contact.html")
