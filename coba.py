nama = input("Masukan nama: ")
nik = int(input("Masukan NIK: "))
status = input("Masukan status (tetap/honor): ")
gol = input("Masukan golongan (A/B/C): ")

gaji = 0

if status == "tetap":

    if gol == "A":
        gaji = 1000000 + 200000

    elif gol == "B":
        gaji = 1000000 + 400000

    elif gol == "C":
        gaji = 1000000 + 550000

    else :
        print("Golongan tidak valid.")


elif status == "honor":

    if gol == "A":
        gaji = 750000 + 150000

    elif gol == "B":
        gaji = 750000 + 275000
    
    elif gol == "C":
        gaji = 750000 + 480000
    
    else :
        print("Golongan tidak valid.")

else:
    print("Status tidak valid.")


print("Nama:", nama)
print("NIK", nik)
print("Status:", status)
print("Golongan:", gol)
print("Gaji:", gaji)