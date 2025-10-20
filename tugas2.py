# Program menyusun ulang list: genap di depan, ganjil di belakang

def susun_list(data):
    genap = []
    ganjil = []
    for angka in data:
        if angka % 2 == 0:
            genap.append(angka)
        else:
            ganjil.append(angka)
    return genap + ganjil


# Input dari user
n = int(input("Masukkan jumlah elemen: "))
angka_list = []
for i in range(n):
    angka = int(input(f"Masukkan angka ke-{i+1}: "))
    angka_list.append(angka)

print("List awal:", angka_list)
print("List hasil susun:", susun_list(angka_list))