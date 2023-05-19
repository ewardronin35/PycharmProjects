from speech_recognition import Microphone, Recognizer, UnknownValueError
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth
import tkinter as tk


from pytspi2 import play_artist, play_album, get_album_uri, get_artist_uri, get_track_uri, play_track, \
    InvalidSearchError

# Set variables from setup
setup = {
    'client_id': 'b5233cf7bf9a438c9f235a9929071bf7',
    'client_secret': '42d9d08fe82545c2839e92dfe8cc76c8',
    'device_name': 'MIDORIN',
    'redirect_uri': 'http://127.0.0.1:8080',
    'username': 'Midoyoki',
    'scope': 'user-read-private user-read-playback-state user-modify-playback-state'
}

client_id = setup['client_id']
client_secret = setup['client_secret']
device_name = setup['device_name']
redirect_uri = setup['redirect_uri']
scope = setup['scope']
username = setup['username']\

# Connecting to the Spotify account
auth_manager = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope,
    username=username)
spotify = sp.Spotify(auth_manager=auth_manager)

window = tk.Tk()
window.title('Spotify Player')
window.geometry('400x300')
window.resizable(False, False)

# Selecting device to play from
devices = spotify.devices()
deviceID = None
for d in devices['devices']:
    d['name'] = d['name'].replace('’', '\'')
    if d['name'] == device_name:
        deviceID = d['id']
        break

# Setup microphone and speech recognizer
r = Recognizer()
m = None
input_mic = 'Microphone (2- Usb Audio Device)'
for i, microphone_name in enumerate(Microphone.list_microphone_names()):
    if microphone_name == input_mic:
        m = Microphone(device_index=i)
        print("Working")

while True:
    """
    Commands will be entered in the specific format explained here:
     - the first word will be one of: 'album', 'artist', 'play'
     - then the name of whatever item is wanted
    """
    with m as source:
        r.adjust_for_ambient_noise(source=source)
        audio = r.listen(source=source)

    command = None
    try:
        command = r.recognize_google(audio_data=audio).lower()
    except UnknownValueError:
        continue

    print(command)
    words = command.split()
    if len(words) <= 1:
        print('Could not understand. Try again')
        continue

    if words[0] == 'stop':
        break

    name = ' '.join(words[1:])
    try:
        if words[0] == 'album':
            uri = get_album_uri(spotify=spotify, name=name)
            play_album(spotify=spotify, device_id=deviceID, uri=uri)
        elif words[0] == 'artist':
            uri = get_artist_uri(spotify=spotify, name=name)
            play_artist(spotify=spotify, device_id=deviceID, uri=uri)
        elif words[0] == 'play':
            uri = get_track_uri(spotify=spotify, name=name)
            play_track(spotify=spotify, device_id=deviceID, uri=uri)
        else:
            print('Specify either "album", "artist" or "play". Try Again')
    except InvalidSearchError:
        print('InvalidSearchError. Try Again')

