import json
import os 

# lihat barang
def lihat_barang():
    print("=" * 50)
    print("              Data Barang di Toko")
    print("=" * 50)
    with open ("data_toko.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    print(data) 

# tambah barang
def tambah_barang():
    with open ("data_toko.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    print("=" * 50)
    print("              Tambah Data Baru")
    print("=" * 50)
    nama_barang = input("Masukkan nama barang : ")
    stok_barang = input("Masukkan stok barang : ")
    data_baru = {
        "barang": nama_barang,
        "stok": stok_barang
    }
    data.append(data_baru)
    print("Barang baru telah ditambahkan.")

    with open (r"data_toko.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# main
def main():
    while True:
        print("=" * 50)
        print("            SISTEM MANAJEMEN DATA TOKO")
        print("=" * 50)
        print("Pilihlah menu berikut :")
        print("1. Lihat Data Barang")
        print("2. Tambah Barang")
        print("0. Keluar")
        pilihan = input("\nMasukkan pilihan menu : ")

        os.system("cls" if os.name == "nt" else "clear")
        if pilihan == "1":
            lihat_barang()
        elif pilihan == "2":
            tambah_barang()
        elif pilihan =="0":
            print("\nTERIMA KASIH TELAH MENGGUNAKAN PROGRAM")
            break
        else :
            print("\nPilihan tidak valid.")

main()