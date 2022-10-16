from datetime import datetime
from pickle import TRUE
from prettytable import PrettyTable

karyawan = []


def tambahKaryawan():
    id = len(karyawan) + 1
    nama = input("Masukkan nama karyawan: ")
    usia = input("Masukkan usia karyawan: ")
    karyawan.append({'id': id, 'nama': nama, 'usia': usia})
    print("Karyawan berhasil ditambahkan\n")
    t = PrettyTable()
    t.field_names = ["ID", "Nama", "Usia"]
    t.add_row([id, nama, usia])
    print(t)


def tampilkanSemuaKaryawan():
    t = PrettyTable()
    t.field_names = ["ID", "Nama", "Usia"]
    for k in karyawan:
        t.add_row([k["id"], k["nama"], k["usia"]])
    print(t)
    print("\n")


def tampilkanKaryawan():
    id = input("Masukkan ID karyawan: ")
    for k in karyawan:
        if k["id"] == id:
            t = PrettyTable()
            t.field_names = ["ID", "Nama", "Usia"]
            t.add_row([k["id"], k["nama"], k["usia"]])
            print(t)
    print("\n")


def updateKaryawan():
    id = input("Masukkan ID karyawan: ")
    for k in karyawan:
        if k["id"] == id:
            k["nama"] = input("Masukkan nama karyawan: ")
            k["usia"] = input("Masukkan usia karyawan: ")
    print("Karyawan berhasil diupdate\n")


def hapusKaryawan():
    id = input("Masukkan ID karyawan: ")
    for k in karyawan:
        if k["id"] == id:
            karyawan.remove(k)
    print("Karyawan berhasil dihapus\n")


while TRUE:
    print("1. Tambah Karyawan")
    print("2. Tampilkan Semua Karyawan")
    print("3. Tampilkan Karyawan")
    print("4. Update Karyawan")
    print("5. Hapus Karyawan")
    print("6. Keluar")
    pilihan = input("Masukkan pilihan: ")
    if pilihan == "1":
        tambahKaryawan()
    elif pilihan == "2":
        tampilkanSemuaKaryawan()
    elif pilihan == "3":
        tampilkanKaryawan()
    elif pilihan == "4":
        updateKaryawan()
    elif pilihan == "5":
        hapusKaryawan()
    elif pilihan == "6":
        break
    else:
        print("Pilihan tidak ditemukan")
