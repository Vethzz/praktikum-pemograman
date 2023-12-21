import os
os.system("clear")

nim = ["2","3","1","0","3","1","0","9","4"]

print(nim)

print("item indeks 0 (pertama)",nim[0])
print("item indeks 1 (kedua)",nim[1])

print(f"item indeks 0 (pertama) {nim[0]}")
print(f"item indeks 0 (kedua) {nim[1]}")
print(f"item indeks terakhir {nim[len(nim)-1]}")
print(f"item indeks terakhir {nim[-1]}")
print(f"item indeks (pertama) {nim[-len(nim)]}")
print()

data = ['Redo Triansyah',2023,'Aktif']
nilai= [90,89,93,97]

print('Nama: '+ data[0])
print('angkatan:', data[1])
print('status: '+ data[2])
print(f"{data[0]} status Kuliah: {data[2]}")
print(f"Data terbesar nilai adalah: {max(nilai)}")
print(f"Data terkecil nilai adalah: {min(nilai)}")
x = sum(nilai) / len(nilai)
print(f"Rata-rata nilai adalah: {x}")
print(f"Jumlah nilai {data[0]} adalah: {len(nilai)}")

data = [('Redo Triansyah',2023,'Aktif'),
        (90,89,93,97),
        (20,22),
        ('S1-Reguler Sistem Informasi C','Ganjil')]

matkul = ['Agama Islam',
          'Pancasila',
          'Bahasa Indonesia',
          'Wawasan Cinta IPTEK dan IMTAQ',
          'Pengantar Pemrograman',
          'Pengantar Teknologi Informasi',
          'Kalkulus Dasar I',
          'Sains Terpadu',]
sks = [2,2,2,2,3,3,3,3]

# Tambahkan matkul dan sks ke dalam data (pakai append)

print()
print(data[0][0])
print(data[-1][0])
print(data[2][0:])

print()
# Daftar Mata kuliah
print("Daftar Mata kuliah:")
# Mata kuliah 1: Matkul1 dengan jumlah 2 sks
print(f"Mata kuliah 1: {matkul[0]} dengan jumlah {sks[0]} sks")
# Mata kuliah 2: Matkul2 dengan jumlah 3 sks
print(f"Mata kuliah 2: {matkul[1]} dengan jumlah {sks[1]} sks")
# Mata kuliah 3: Matkul3 dengan jumlah 2 sks
print(f"Mata kuliah 3: {matkul[2]} dengan jumlah {sks[2]} sks")
# Mata kuliah 4: Matkul4 dengan jumlah 3 sks
print(f"Mata kuliah 4: {matkul[3]} dengan jumlah {sks[3]} sks")
# Mata kuliah 5: Matkul5 dengan jumlah 3 sks
print(f"Mata kuliah 5: {matkul[4]} dengan jumlah {sks[4]} sks")
# Mata kuliah 6: Matkul6 dengan jumlah .. sks
print(f"Mata kuliah 6: {matkul[5]} dengan jumlah {sks[5]} sks")
# Mata kuliah 7: Matkul7 dengan jumlah .. sks
print(f"Mata kuliah 7: {matkul[6]} dengan jumlah {sks[6]} sks")
# Mata kuliah 8: Matkul8 dengan jumlah .. sks
print(f"Mata kuliah 8: {matkul[7]} dengan jumlah {sks[7]} sks")

# Tambah Nilai jadi 8 (pakai append)
print(f"Total SKS: {sum(sks)}")

print()
print(f"Nama mahasiswa: {data[0][0]}")
print(f"Inisial {data[0][0]}: {data[0][0][0]} {data[0][0][5]}")
print(f"NIM {data[0][0]}: {''.join(nim)}")
print(f"Program pendidikan {data[0][0]}: {data[3][0]}")
print(f"Angkatan {data[0][0]} : {data[3][1]}-{data[0][1]}")
print(f"Total sks {data[0][0]}: {data[2][0]}")
print(f"Jumlah nilai {data[0][0]} adalah: {len(data[1])}")
print(f"Data terbesar {data[0][0]} adalah: {max(data[1])}")
print(f"Data terkecil {data[0][0]} adalah: {min(data[1])}")
rata = sum(data[1]) / len(data[1])
print(f"Rata-rata nilai {data[0][0]}: {rata}")