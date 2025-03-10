nama = input("Masukkan Nama : ")
nik = input("Masukkan NIK : ")
status = input("Masukkan Status (Tetap/Honor) : ")
golongan = input("Masukkan Golongan (A/B/C) : ")

gaji = {"Tetap": 1000000, "Honor": 750000}

bonus = {
    "Tetap": {
        "A": 200000,
        "B": 400000,
        "C": 550000
    },
    "Honor": {
        "A": 150000,
        "B": 275000,
        "C": 480000
    },
}

# Cek apakah status dan golongan sesuai
if status in gaji and golongan in bonus[status]:
    total = gaji[status] + bonus[status][golongan]
    print(f"\nNama: {nama}")
    print(f"NIK: {nik}")
    print(f"Status: {status}")
    print(f"Golongan: {golongan}")
    print(f"Gaji Pokok: {gaji[status]}")
    print(f"Bonus: {bonus[status][golongan]}")
    print(f"Total Gaji: {total}")
else:
    print("Error: Status dan golongan tidak sesuai. Silakan periksa kembali input Anda.")
