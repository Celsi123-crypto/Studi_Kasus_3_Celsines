batas_nilai = (65, 100)

nilai_masuk = []
lulus = []
remedi = []

while True:
    nilai = input("Masukkan nilai (ketik selesai): ")

    if nilai == "selesai":
        break
    nilai = int(nilai)
    nilai_masuk.append(nilai)

    if nilai >= batas_nilai[0]:
        lulus.append(nilai)
    else:
        remedi.append(nilai)

hapus = input("Ada nilai yang salah? (ya/tidak): ")

if hapus == "ya":
    nilai_hapus = int(input("Masukkan nilai yang ingin dihapus: "))

    if nilai_hapus in nilai_masuk:
        nilai_masuk.remove(nilai_hapus)

        if nilai_hapus in lulus:
            lulus.remove(nilai_hapus)
        else:
            remedi.remove(nilai_hapus)

print("Nilai masuk:", nilai_masuk)
print("Lulus:", lulus)
print("Remedi:", remedi)
