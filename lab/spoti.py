import spotipy
import webbrowser
import tkinter as tk

from spotipy import SpotifyOAuth

# Spotify API credentials
client_id = 'b5233cf7bf9a438c9f235a9929071bf7'
client_secret = '42d9d08fe82545c2839e92dfe8cc76c8'
redirect_uri = 'http://127.0.0.1:8080'
scope = "playlist-modify-public"

# Authentication object
oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)

# Get access token
token_dict = oauth.get_access_token()
token = token_dict['access_token']

# Create Spotify object
spotify = spotipy.Spotify(auth=token)

# Get current user
user = spotify.current_user()

# Create tkinter window
root = tk.Tk()
root.title("Spotify Console")
root.geometry('320x250')
root.resizable(False, False)
root.configure(bg='#121212')


# Create function to search for a song
def search_song():
    search_song = song_entry.get()
    results = spotify.search(search_song, 1, 0, "track")
    songs_dict = results['tracks']
    song_items = songs_dict['items']
    song = song_items[0]['external_urls']['spotify']
    webbrowser.open(song)
    song_entry.delete(0, tk.END)


# Create function to search for an album
def search_album():
    search_album = album_entry.get()
    results = spotify.search(search_album, 1, 0, "album")
    albums_dict = results['albums']
    album_items = albums_dict['items']
    album = album_items[0]['external_urls']['spotify']
    webbrowser.open(album)
    album_entry.delete(0, tk.END)


# Create function to search for an artist
def search_artist():
    search_artist = artist_entry.get()
    results = spotify.search(search_artist, 1, 0, "artist")
    artists_dict = results['artists']
    artist_items = artists_dict['items']
    artist = artist_items[0]['external_urls']['spotify']
    webbrowser.open(artist)
    artist_entry.delete(0, tk.END)


# Create function to get current user's playlists
def get_playlists():
    playlists = spotify.current_user_playlists()
    playlist_list.delete(0, tk.END)
    for playlist in playlists['items']:
        playlist_list.insert(tk.END, playlist['name'])


# Create function to create a playlist
def create_playlist():
    playlist_name = playlist_name_entry.get()
    playlist_description = playlist_description_entry.get()
    playlist_public = playlist_public_var.get()

    if playlist_public:
        playlist_public = True
    else:
        playlist_public = False
    spotify.user_playlist_create(user['id'], playlist_name, description=playlist_description, public=playlist_public)
    playlist_name_entry.delete(0, tk.END)
    playlist_description_entry.delete(0, tk.END)
    playlist_public_check.deselect()
    playlist_created_label.config(text="Playlist created successfully!")


# Create GUI elements
song_label = tk.Label(root, text="Search for a song:", bg='#121212', fg='#ffffff')
song_entry = tk.Entry(root)
song_button = tk.Button(root, text="Search", command=search_song, bg='#006350', fg='#ffffff')

album_label = tk.Label(root, text="Search for an album:", bg='#121212', fg='#ffffff')
album_entry = tk.Entry(root)
album_button = tk.Button(root, text="Search", command=search_album, bg='#006350', fg='#ffffff')

artist_label = tk.Label(root, text="Search for an artist:", bg='#121212', fg='#ffffff')
artist_entry = tk.Entry(root)
artist_button = tk.Button(root, text="Search", command=search_artist, bg='#006350', fg='#ffffff')

playlist_label = tk.Label(root, text="Your playlists:", bg='#121212', fg='#ffffff')
playlist_list = tk.Listbox(root)

get_playlists_button = tk.Button(root, text="Get playlists", command=get_playlists, bg='#006350', fg='#ffffff')



# Add GUI elements to window
song_label.grid(row=0, column=0)
song_entry.grid(row=0, column=1)
song_button.grid(row=0, column=2)

album_label.grid(row=1, column=0)
album_entry.grid(row=1, column=1)
album_button.grid(row=1, column=2)

artist_label.grid(row=2, column=0)
artist_entry.grid(row=2, column=1)
artist_button.grid(row=2, column=2)

playlist_label.grid(row=3, column=0)
playlist_list.grid(row=3, column=1)
get_playlists_button.grid(row=3, column=2)



root.mainloop()
