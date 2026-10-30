cities = ["Jakarta", "Bandung", "Surabaya"]

# Mengakses elemen dalam list
print("First city:", cities[0]) 

# Mengubah elemen dalam list
cities [1] = "Yogyakarta"
print("After changing an item:", cities)

# Menambahkan elemen di akhir list
cities.append("Semarang")
print("After append():", cities)

# Menambahkan elemen pada posisi tertentu
cities.insert(1, "Malang")
print("After insert():", cities)

# Menghapus elemen menggunakan del
del cities[0]
print("After del:", cities)

# Menghapus elemen menggunakan pop()
removed_city = cities.pop()
print("Popped city:", removed_city)
print("After pop():", cities)

# Menghapus elemen tertentu menggunakan remove()
cities.remove("Malang")
print("After remove():", cities)

# Mengurutkan list sementara
print("Sorted list:", sorted(cities))

# Membalik urutan list
cities.reverse()
print("After reverse():", cities)

# Mengurutkan list secara permanen
cities.sort()
print("After sort():", cities)

# Menghitung jumlah elemen
print("Number of cities:", len(cities))