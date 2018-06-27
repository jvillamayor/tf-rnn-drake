# get_all_songs.py

import lyricsgenius as genius

print("hello julius!")

api = genius.Genius(
    "")
print("api set.")
artist = api.search_artist("Drake")
print("artist set.")

print("number of songs from {}: {}\n".format(artist.name, artist.num_songs))

print("Songs titles:")
for i in artist.songs:
    print(i.title)

print("exiting with no errors.")
