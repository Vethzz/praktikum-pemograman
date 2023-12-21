nama='Redo Triansyah''
nim='231031094'
meet="Praktikum 3 (string)"
prodi="sistem informasi c"
email="6rdhoz9@gmail.com"
kota="parepare"
lahir="08-07-2005"
hobi="main game"
alamat="jln Kesuma Timur"
tinggi=184
asal=kota

#CARA KE 1
print("-"*144)

str1 = 'Redo Triansyah''
a = str1.center(143)
print(a)

str2 = '231031094''
a = str2.center(143)
print(a)

str3 = '|'
a = str3.center(143)
print(a)

str3 = '|'
a = str3.center(143)
print(a)


str4 = "Praktikum 3 (string)"
a = str4.rjust(143)
print(a)

str5 = "sistem informasi c"
a = str5.rjust(143)
print(a)

str6 = "6rdhoz9@gmail.com"
a = str6.rjust(143)
print(a)

print("-"*143)

#CARA KE 2

print()

sp=143
print('-'*sp)
print(nama.upper().center(sp))
print(nim.center(sp))
str3 = '|'
a = str3.center(sp)
str3 = '|'
a = str3.center(sp)
print(a)
print(a)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.rjust(sp))
print('-'*sp)

print()
print(f'''     \thalo,nama saya",{nama},"dengan NIM",{nim},"dari prodi",{prodi},"ini adalah file",{meet},"terima kasih. \n''')
print()
print(f'''Biodata Saya:
nama\t:{nama.upper()}
NIM\t:{nim}
Prodi\t:{prodi}
ttl\t:{lahir}
alamat\t:{alamat}                               
asal\t:{asal}      
hobi\t:{hobi}
tinggi\t:{tinggi}cm            
''')
print()

stat1 = 'duFort Frankel Sir Issac'
# Issac duFort Frankel Sir

stat2 = 'duFort Frankel Sir Issac'
# d F S Issac

stat3 = 'duFort Frankel Sir Issac'
# duFort F S I

stat4 = 'duFort Frankel Sir Issac'
# I duFort Frankel Sir

stat5 = 'duFort Frankel Sir Issac'
# Issac d F S

stat6 = 'duFort Frankel Sir Issac'
# ISSAC D F S

stat7 = '#duFort Frankel Sir Issac$'
# duFort Frankel Sir Issac

stat8 = '#duFort-Frankel-Sir-Issac$'
# duFort Frankel Sir Issac

stat9 = '#duFort@ ^Frankel* (Sir( (Issac$'
# duFort Frankel Sir Issac

stat10 = '#duFort@-^Frankel*-(Sir(-(Issac$'
# DUFORT FRANKEL SIR ISSAC



