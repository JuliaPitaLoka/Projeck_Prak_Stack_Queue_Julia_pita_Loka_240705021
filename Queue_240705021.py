class Queue:
    def __init__(self):  # constructor harus pakai double underscore
        self.qList = []

    def isEmpty(self):
        return len(self.qList) == 0

    def __len__(self):  # juga harus pakai double underscore
        return len(self.qList)

    def enqueue(self, data):
        self.qList.append(data)

    def dequeue(self):
        if self.isEmpty():
            print("Queue kosong. Tidak ada data yang dapat di-dequeue.")
            return None
        else:
            return self.qList.pop(0)

    def display(self):
        if self.isEmpty():
            print("Queue kosong. Tidak ada data yang dapat ditampilkan.")
        else:
            print(" ".join(str(item) for item in self.qList))

    def DeleteAll(self):
        self.qList.clear()


# Program utama
myQueue = Queue()
cek = True

while cek:
    print("\n------- Masukan Pilihan Anda -------")
    print("1. Tambah Elemen pada Queue")
    print("2. Tampil Elemen dalam Queue")
    print("3. Hapus Elemen dalam Queue")
    print("4. Hapus Seluruh data dalam Queue")
    print("0. Keluar")
    print("------------------------------------")

    try:
        pil = int(input("Masukan pilihan anda: "))
    except ValueError:
        print("Input harus berupa angka!")
        continue

    if pil == 1:
        try:
            jum = int(input("Masukan jumlah data yang ingin diinputkan: "))
            if jum > 0:
                for i in range(1, jum + 1):
                    data = input(f"Masukan data ke-{i}: ")
                    myQueue.enqueue(data)
            else:
                print("Jumlah data minimal 1 !!!")
        except ValueError:
            print("Input harus berupa angka!")

    elif pil == 2:
        print("Isi Queue:")
        myQueue.display()

    elif pil == 3:
        removed = myQueue.dequeue()
        if removed is not None:
            print(f"Data '{removed}' telah dihapus")

    elif pil == 4:
        myQueue.DeleteAll()
        print("Seluruh data telah dihapus")

    elif pil == 0:
        print("Bye troopers...\n")
        cek = False

    else:
        print("Pilihan tidak ada")