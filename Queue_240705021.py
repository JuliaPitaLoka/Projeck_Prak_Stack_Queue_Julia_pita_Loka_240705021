class Queue:
    def _init_(self):
        self.qList = []

    def isEmpty(self):
        return len(self.qList) == 0

    def _len_(self):
        return len(self.qList)

    def enqueue(self, data):
        self.qList.append(data)

    def dequeue(self):
        if self.isEmpty():
            print("Queue kosong. Tidak ada data yang dapat di-dequeue.")
        else:
            return self.qList.pop(0)

    def display(self):
        if self.isEmpty():
            print("Queue kosong. Tidak ada data yang dapat ditampilkan.")
        else:
            for item in self.qList:
                print(item, end=" ")
            print()

    def DeleteAll(self):
        self.qList.clear()

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
                i = 1
                while i <= jum:
                    data = input(f"Masukan data ke-{i}: ")
                    myQueue.enqueue(data)
                    i += 1
            else:
                print("Jumlah data minimal 1 !!!")
        except ValueError:
            print("Input harus berupa angka!")

    elif pil == 2:
        print("Isi Queue: ")
        myQueue.display()

    elif pil == 3:
        removed = myQueue.dequeue()
        if removed:
            print(f"Data '{removed}' telah dihapus")

    elif pil == 4:
        myQueue.DeleteAll()
        print("Seluruh data telah dihapus")

    elif pil == 0:
        print("Bye troopers...\n")
        cek = False

    else:
        print("Pilihan tidak ada")