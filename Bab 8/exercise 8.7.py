def make_album(artist, title):
    album = {
        "artist": artist,
        "title": title
    }
    return album


album1 = make_album("My Chemical Romance", "The Black Parade")
album2 = make_album("Geisha", "Meraih Bintang")
album3 = make_album("Vierra", "My First Love")

print(album1)
print(album2)
print(album3)