data_satwa = []
satwa_dilindungi = ["elang jawa", "harimau sumatera", "anoa", "burung maleo", "orangutan", "macan tutul", "komodo"]

while True:
    print("\n==========================================")
    print("   LOGBOOK OBSERVASI SATWA LIAR PENDAKIAN  ")
    print("==========================================")
    print("1. Tambah Data Satwa")
    print("2. Tampilkan Semua Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        print("\n--- Tambah Data Satwa ---")
        nama = input("Nama satwa      : ")

        jumlah = input("Jumlah (ekor)   : ")
        while not jumlah.isdigit() or int(jumlah) <= 0:
            print("Jumlah harus angka bulat positif!")
            jumlah = input("Jumlah (ekor)   : ")
        jumlah = int(jumlah)

        tinggi = input("Ketinggian (mdpl): ")
        while not tinggi.isdigit() or int(tinggi) <= 0:
            print("Ketinggian harus angka positif!")
            tinggi = input("Ketinggian (mdpl): ")
        tinggi = int(tinggi)

        if nama.lower() in satwa_dilindungi:
            status = "Dilindungi"
        else:
            jawab = input(f"'{nama}' tidak ada di daftar, apakah dilindungi? (y/n): ")
            if jawab.lower() == "y":
                status = "Dilindungi"
            else:
                status = "Tidak Dilindungi"

        if tinggi < 1000:
            zona = "Zona Dataran Rendah (Hutan Hujan)"
        elif tinggi < 2400:
            zona = "Zona Montane (Hutan Pegunungan)"
        else:
            zona = "Zona Sub-Alpin (Puncak/Vegetasi Rendah)"

        data_satwa.append((nama, jumlah, tinggi, status, zona))

        print("\nData berhasil ditambahkan!")
        print(f"    Status : {status}")
        print(f"    Zona   : {zona}")

    elif pilihan == "2":
        print("\n--- Riwayat Observasi Satwa ---")
        if len(data_satwa) == 0:
            print("Belum ada data satwa yang dicatat.")
        else:
            nomor = 1
            for s in data_satwa:
                print(f"{nomor}. {s[0]} ({s[1]} ekor) | Ketinggian: {s[2]} mdpl")
                print(f"   Status: {s[3]} | Zona: {s[4]}")
                print("-" * 50)
                nomor += 1

    elif pilihan == "3":
        print("\n--- Ubah Data Satwa ---")
        if len(data_satwa) == 0:
            print("Belum ada data satwa yang bisa diubah.")
        else:
            nomor = 1
            for s in data_satwa:
                print(f"{nomor}. {s[0]} ({s[1]} ekor) | {s[2]} mdpl | {s[3]}")
                nomor += 1

            no = input("Pilih nomor data yang mau diubah (0 untuk batal): ")
            while not no.isdigit():
                print("Masukkan angka yang valid!")
                no = input("Pilih nomor data yang mau diubah (0 untuk batal): ")
            no = int(no)

            if no == 0:
                print("Proses ubah data dibatalkan.")
            elif no >= 1 and no <= len(data_satwa):
                nama = input("Nama satwa baru      : ")

                jumlah = input("Jumlah baru (ekor)   : ")
                while not jumlah.isdigit() or int(jumlah) <= 0:
                    print("Jumlah harus angka bulat positif!")
                    jumlah = input("Jumlah baru (ekor)   : ")
                jumlah = int(jumlah)

                tinggi = input("Ketinggian baru (mdpl): ")
                while not tinggi.isdigit() or int(tinggi) <= 0:
                    print("Ketinggian harus angka positif!")
                    tinggi = input("Ketinggian baru (mdpl): ")
                tinggi = int(tinggi)

                if nama.lower() in satwa_dilindungi:
                    status = "Dilindungi"
                else:
                    jawab = input(f"'{nama}' tidak ada di daftar, apakah dilindungi? (y/n): ")
                    if jawab.lower() == "y":
                        status = "Dilindungi"
                    else:
                        status = "Tidak Dilindungi"

                if tinggi < 1000:
                    zona = "Zona Dataran Rendah (Hutan Hujan)"
                elif tinggi < 2400:
                    zona = "Zona Montane (Hutan Pegunungan)"
                else:
                    zona = "Zona Sub-Alpin (Puncak/Vegetasi Rendah)"

                data_satwa[no - 1] = (nama, jumlah, tinggi, status, zona)
                print("\nData berhasil diubah!")
                print(f"    Status : {status}")
                print(f"    Zona   : {zona}")
            else:
                print("Nomor data tidak ditemukan.")

    elif pilihan == "4":
        print("\n--- Hapus Data Satwa ---")
        if len(data_satwa) == 0:
            print("Belum ada data satwa yang bisa dihapus.")
        else:
            nama_hapus = input("Nama satwa yang ingin dihapus: ")
            ditemukan = None

            for s in data_satwa:
                if s[0].lower() == nama_hapus.lower():
                    ditemukan = s

            if ditemukan != None:
                print(f"\n[Data Ditemukan]")
                print(f"Nama       : {ditemukan[0]}")
                print(f"Jumlah     : {ditemukan[1]} ekor")
                print(f"Ketinggian : {ditemukan[2]} mdpl")
                print(f"Status     : {ditemukan[3]}")
                print(f"Zona       : {ditemukan[4]}")

                konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ")
                if konfirmasi.lower() == "y":
                    data_satwa.remove(ditemukan)
                    print(f"Data '{ditemukan[0]}' berhasil dihapus!")
                else:
                    print("Penghapusan dibatalkan.")
            else:
                print(f"Data satwa '{nama_hapus}' tidak ditemukan.")

    elif pilihan == "5":
        print("\nTerima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid! Silakan pilih angka 1 sampai 5.")