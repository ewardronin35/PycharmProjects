import tkinter as tk
import webbrowser

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import speech_recognition as sr

# Initialize Spotify    client
client_id = 'b5233cf7bf9a438c9f235a9929071bf7'
client_secret = '42d9d08fe82545c2839e92dfe8cc76c8'
redirect_uri = 'http://127.0.0.1:8080'

# Create the Spotipy client with authorization code flow and redirect URI
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,
                              scope='user-library-read user-modify-playback-state'))
print(sp.auth_manager.get_access_token(as_dict=True)['scope'])
# Initialize tkinter window
window = tk.Tk()
window.title('Spotify Player')
window.geometry('400x300')
window.resizable(False, False)
window.configure(bg='#1DB954')


# Define functions for playing, pausing, and skipping tracks
def play_music():
    sp.start_playback()
    update_track_info()


def pause_music():
    sp.pause_playback()
    update_track_info()


def skip_music():
    sp.next_track()
    update_track_info()


def stop_music():
    sp.pause_playback()
    exit()


# Define function for recognizing speech
def recognize_speech():
    # Initialize speech recognizer
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        # Convert speech to text
        speech_text = r.recognize_google(audio)
        print("You said: " + speech_text)

        # Play, pause, skip, or search for music based on speech
        if 'play' in speech_text.lower():
            song_name = speech_text.lower().replace('play', '').strip()
            results = sp.search(q=song_name, type='track', limit=1)
            if results['tracks']['items']:
                track_uri = results['tracks']['items'][0]['uri']
                sp.start_playback(uris=[track_uri])
                update_track_info()
            else:
                status_label.config(text='Song not found')
        elif 'pause' in speech_text.lower():
            pause_music()
        elif 'skip' in speech_text.lower():
            skip_music()
        elif 'search' in speech_text.lower():
            query = speech_text.lower().replace('search', '').strip()
            webbrowser.open(f'https://open.spotify.com/search/{query}')
        else:
            status_label.config(text='Invalid command')

    except sr.UnknownValueError:
        status_label.config(text='Speech recognition could not understand audio')
    except sr.RequestError as e:
        status_label.config(text='Could not request results from speech recognition service: {0}'.format(e))


# Define function for updating track info label
def update_track_info():
    current_track = sp.current_playback()
    if current_track:
        track_name = current_track['item']['name']
        artist_name = current_track['item']['artists'][0]['name']
        album_name = current_track['item']['album']['name']
        album_art_url = current_track['item']['album']['images'][0]['url']
        track_info_label.config(text=f'{track_name} - {artist_name} | {album_name}')
        album_art_image.config(url=album_art_url)
    else:
        track_info_label.config(text='Not currently playing')
        album_art_image.config(url='')


# GUI buttons and labels
play_button = tk.Button(window, text='Play', command=play_music)
play_button.pack(pady=10)

pause_button = tk.Button(window, text='Pause', command=pause_music)
pause_button.pack(pady=10)

speak_button = tk.Button(window, text='Speak', command=recognize_speech)
speak_button.pack(pady=10)

stop_button = tk.Button(window, text='Stop', command=stop_music)
stop_button.pack(pady=10)

status_label = tk.Label(window, text='Ready')
status_label.pack(pady=10)
# Run tkinter window
window.mainloop()
