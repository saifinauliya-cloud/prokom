places = ["Japan", "Singapore", "Switzerland", "UK", "Italy"]

# Menampilkan urutan awal
print("Original list:")
print(places)

# Mengurutkan secara alfabetis tanpa mengubah urutan asli
print("\nAlphabetical order:")
print(sorted(places))

# Memastikan urutan asli tidak berubah
print("\nOriginal list:")
print(places)

# Mengurutkan seacara alfabetis terbalik
print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))

# Memastikan urutan asli tidak berubah
print("\nOriginal list:")
print(places)

# Membalik urutan list
places.reverse()
print("\nReversed list:")
print(places)

# Mengembalikan urutan list
places.reverse()
print("\nBack to original list:")
print(places)

# Mengurutkan secara alfabetis secara permanen
places.sort()
print("\nAlphabetical order:")
print(places)

# Mengurutkan secara alfabetis terbalik secara permanen
places.sort(reverse=True)
print("\nReverse alphabetical order:")
print(places)