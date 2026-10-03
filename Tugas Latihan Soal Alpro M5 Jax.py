#Tugas Alpro M5
#Nomor 1
jadwal_hari=("Senin","Selasa","Rabu","Kamis","Jumat")
print(jadwal_hari)
print(type(jadwal_hari))

#Nomor 2
koordinat = (10, 20, 30, 40, 50)
print(koordinat[2])
print(koordinat[3:5])

#Nomor 3
warna=("jingga","hijau","biru")
# warna[0]="ungu"  # ini akan menyebabkan error karena tuple bersifat immutable
# warna.append("merah")  # ini juga akan menyebabkan error karena tuple tidak memiliki metode append
print(warna)

#Nomor 4
kumpulan_huruf = ("a", "b", "c", "a", "d", "a", "e")
print("Index dari 'd':", kumpulan_huruf.index("d"))
print("Jumlah kemunculan 'a':", kumpulan_huruf.count("a"))

#Nomor 5
titik_lokasi = (112.79, -7.28)
(longitude,lattitude)=titik_lokasi
print("Longitude:", longitude)
print("Latitude:", lattitude)

#Nomor 6
kendaraan = ("Motor", "Mobil", "Sepeda")
print(kendaraan)
list_kendaraan=list(kendaraan)
list_kendaraan[1]="Bus"
list_kendaraan=tuple(list_kendaraan)
print(f'List kendaraan setelah diubah: {list_kendaraan}')
print(type(list_kendaraan))
