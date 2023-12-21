print("Nama : Redo Triansyah")
print("Nim  : 231031094")
print("Prodi: Sistem Informasi")
print("Tanggal Lahir : 08-07-2005")

#Operator Penugasan
print()
a = 94
print("Nilai a =", a)

print()
a+=2
print("Nilai a+=2 =", a)

print()
a-=2
print("Nilai a-=2 =", a)

print()
a*=2
print("Nilai a*=2 =", a)

print()
a/=2
print("Nilai a/=2 =", a)

print()
a%=2
print("Nilai a%=2 =", a)

print()
a**=2
print("Nilai a**=2 =", a)

print()
a//=2
print("Nilai a//=2 =", a)

print()
a = 94
a&=2
print("Nilai a&=2 =", a)

print()
a|=2
print("Nilai a|=2 =", a)

print()
a^=2
print("Nilai a^=2 =", a)

print()
a>>=2
print("Nilai a>>=2 =", a)

print()
a<<=2
print("Nilai a<<=2 =", a)

#Or
print()
b = True
print("Nilai b =",b)

b|=False
print("Nilai b|=False akan menjadi",b)

b=False
print("Nilai b=False akan menjadi",b)

b|=False
print("Nilai b|=False akan menjadi",b)

#AND
b=True
print("Nilai b =",b)

b&=False
print("Nilai b|=False akan menjadi",b)

b=False
print("Nilai b =",b)

b&=False
print("Nilai b|=False akan menjadi",b)

#XOR
b=True
print("Nilai b =",b)

b^=False
print("Nilai b|=False akan menjadi",b)

b=False
print("Nilai b =",b)

b^=False
print("Nilai b|=False akan menjadi",b)

#Shifthing
c=0b0100
print("Nilai c =",format(c, "04b"))

c>>=1
print("Nilai c>>=1 akan menjadi",format(c, "04b"))

c<<=1
print("Nilai c<<=1 akan menjadi",format(c, "04b"))

#Operasi Komparasi/Perbandingan
a=4
b=9
print("================== Besar dari 9")
hasil = a>4
print(a,"> 4 adalah",hasil)
hasil = b>9
print(b,"> 9 adalah",hasil)

print("================== Kecil dari 9")
hasil = a<4
print(a,"< 4 adalah",hasil)
hasil = b<9
print(b,"< 9 adalah",hasil)

print("================== Besar atau sama dari 9")
hasil = a>=4
print(a,">= 4 adalah",hasil)
hasil = b>=9
print(b,">= 9 adalah",hasil)

print("================== Kecil atau sama dari 9")
hasil = a<=4
print(a,"<= 4 adalah",hasil)
hasil = b<=9
print(b,"<= 9 adalah",hasil)

print("================== Sama dengan 9")
hasil = a==4
print(a,"== 4 adalah",hasil)
hasil = b==9
print(b,"== 9 adalah",hasil)

print("================== Tidak sama dengan 9")
hasil = a!=4
print(a,"!= 4 adalah",hasil)
hasil = b!=9
print(b,"!= 9 adalah",hasil)

#Operasi Logika
print("=============NOT=============")
a=Truec = not a
print("a adalah",a)
print("------c = not a-------NOT")
print("c adalah",c)

print("=============OR=============")
a=True
b=True
c=a or b
print(a, "OR",b,"menjadia",c)

a=True
b=False
c=a or b
print(a, "OR",b,"menjadia",c)

a=False
b=True
c=a or b
print(a, "OR",b,"menjadia",c)

a=False
b=False
c=a or b
print(a, "OR",b,"menjadia",c)

print("=============AND=============")
a=True
b=True
c=a or b
print(a, "AND",b,"menjadia",c)

a=True
b=False
c=a or b
print(a, "AND",b,"menjadia",c)

a=False
b=True
c=a or b
print(a, "AND",b,"menjadia",c)

a=False
b=False
c=a or b
print(a, "AND",b,"menjadia",c)

print("=============XOR=============")
a=True
b=True
c=a ^ b
print(a, "^",b,"menjadia",c)

a=True
b=False
c=a ^ b
print(a, "^",b,"menjadia",c)

a=False
b=True
c=a ^ b
print(a, "^",b,"menjadia",c)

a=False
b=False
c=a ^ b
print(a, "^",b,"menjadia",c)

#TUGAS
#Buat kode untuk masing masing operator berikut
print("=============NAND=============")
print("=============NOR=============")
print("=============NXOR=============")

#Operator Membership
print("======================= IN")
nama_lengkap = "Bachruddin Jusuf Habibie"
test = "a"
cek = test in nama_lengkap
print(test," terdapat di ",nama_lengkap," adalah ",str(cek))

test = "rud"
cek = test in nama_lengkap
print(test," terdapat di ",nama_lengkap," adalah ",str(cek))

test = "bac"
cek = test in nama_lengkap
print(test," terdapat di ",nama_lengkap," adalah ",str(cek))

print("=======================NOT IN")
nama_lengkap = "Bachruddin Jusuf Habibie"
test = "a"
cek = test not in nama_lengkap
print(test,"tidak terdapat di ",nama_lengkap," adalah ",str(cek))

test = "rud"
cek = test not in nama_lengkap
print(test,"tidak terdapat di ",nama_lengkap," adalah ",str(cek))

test = "bac"
cek = test not in nama_lengkap
print(test,"tidak terdapat di ",nama_lengkap," adalah ",str(cek))

#Tugas
#Dengan cara yang sama buat operator in dan not in , ubah nama ←- lengkap menjadi nama masing - masing dengan uji test
test1 = "re"
test2 = "er"
test3 = "a"
test4 = "i"
test5 = "e"
test6 = "o"

#Operator Bitwise
a=8
a +=60
b=7
b+= 90
print("=============================OR")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(|)")
hasil=a|b
print("Nilai",a,"|",b,"dalam biner =", format(hasil,"08b"))

print("=============================AND")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(&)")
hasil=a&b
print("Nilai",a,"&",b,"dalam biner =", format(hasil,"08b"))

print("=============================XOR")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(^)")
hasil=a^b
print("Nilai",a,"^",b,"dalam biner =", format(hasil,"08b"))

print("=============================NOT")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(~a)")
hasil= ~a
print("Nilai ~",a,"dalam biner =", format(hasil,"08b"))

print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(~b)")
hasil= ~b
print("Nilai ~",b,"dalam biner =", format(hasil,"08b"))

print("=============================>>")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(>>2)")
hasil= a >> 2
print("Nilai ~",a,"dalam biner =", format(hasil,"08b"))

print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(<<2)")
hasil= b << 2
print("Nilai ~",b,"dalam biner =", format(hasil,"08b"))