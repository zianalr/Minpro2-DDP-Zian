data_karyawan = {
    "Username" : "Karyawan",
    "Password" : "goyounjung"
}

data_manager = {
    "Username" : "Manager",
    "Password" : "seorina"
}

jenis_cupang = ["Cupang HMPK", "Cupang Blue Rim", "Cupang Plakat"]

layak_kontes = []

def login():
    print("--------------------------")
    print("        LAMAN LOGIN       ")
    print("--------------------------")
    while True:
        try:
            usn = input("Masukkan username: ")
            pw = input("Masukkan password: ")
            if usn == data_karyawan["Username"] and pw == data_karyawan["Password"]:
                menu_karyawan()
                break
            elif usn == data_manager["Username"] and pw == data_manager["Password"]:
                menu_manager()
                break
            else:
                print("Tolong Masukkan Username dan Password dengan benar")
        except KeyboardInterrupt:
            print("Jangan pencet CTRL C")
        except EOFError:
            print("Jangan pencet CTRL Z")
        except:
            print("Tolong masukkan dengan benar!")

def menu_karyawan():
    print("\nAnda berhasil login sebagai Karyawan")
    print("SELAMAT DATANG!")
    while True:
        print("-----------------MENU------------------")
        print("1. Lihat Jenis Ikan Cupang")
        print("2. Singkirkan Ikan Cupang")
        print("3. Validasi Kelayakan Untuk Kontes Ikan Cupang")
        print("4. Update Ikan")
        print("5. Keluar")
        print("---------------------------------------")

        try:
            menu = int(input("Pilih Menu dengan Angka: "))
            if menu == 1:
                lihat_ikan()
            elif menu == 2:
                singkirkan_ikan()
            elif menu == 3:
                validasi_kontes()
            elif menu == 4:
                update_ikan()
            elif menu == 5:
                print("Terimakasih Sudah Menggunakan Program Ini")
                break
            else:
                print("\nError")
        except ValueError:
            print("Tolong Masukkan Angka!")
        except KeyboardInterrupt:
            print("Jangan pencet CTRL C")
        except EOFError:
            print("Jangan pencet CTRL Z")
        except:
            print("Tolong masukkan dengan benar!")

def menu_manager():
    print("\nAnda berhasil login sebagai Manager")
    print("SELAMAT DATANG!")
    while True:
        print("-----------------MENU------------------")
        print("1. Lihat Jenis Ikan Cupang")
        print("2. Singkirkan Ikan Cupang")
        print("3. Validasi Kelayakan Untuk Kontes Ikan Cupang")
        print("4. Update Ikan")
        print("5. Tambah Jenis Ikan Cupang")
        print("6. Keluar")
        print("---------------------------------------")

        try:
            menu = int(input("Pilih Menu dengan Angka: "))
            if menu == 1:
                lihat_ikan()
            elif menu == 2:
                singkirkan_ikan()
            elif menu == 3:
                validasi_kontes()
            elif menu == 4:
                update_ikan()
            elif menu == 5:
                tambah_ikan()
            elif menu == 6:
                print("Terimakasih Sudah Menggunakan Program Ini")
                break
            else:
                print("\nError")
        except ValueError:
            print("Tolong Masukkan Angka!")
        except KeyboardInterrupt:
            print("Jangan pencet CTRL C")
        except EOFError:
            print("Jangan pencet CTRL Z")
        except:
            print("Tolong masukkan dengan benar!")

def lihat_ikan():
    print("1. Lihat Semua Jenis Ikan")
    print("2. Lihat Ikan Layak Kontes")
    try:
        pilihan = int(input("Pilih dengan angka: "))
        if pilihan == 1:
            print("List Jenis Ikan Cupang\n",jenis_cupang)
        elif pilihan == 2:
            if not layak_kontes:
                print("Jenis Ikan Cupang Belum Ada")
            else:
                print("List Jenis Ikan Cupang Layak Kontes\n", layak_kontes)
        else:
            print("Error")
    except ValueError:
        print("Tolong Masukkan Angka: ")        
    except KeyboardInterrupt:
        print("Jangan pencet CTRL C")
    except EOFError:
        print("Jangan pencet CTRL Z")
    except:
        print("Tolong masukkan dengan benar!")

def tambah_ikan():
    try:
        tambah = input("Masukkan Jenis Ikan Cupang: ")
        jenis_cupang.append(tambah)
        print("\nAnda telah menambahkan", tambah)
        print(jenis_cupang)
    except KeyboardInterrupt:
        print("Jangan pencet CTRL C")
    except EOFError:
        print("Jangan pencet CTRL Z")
    except:
        print("Tolong masukkan dengan benar!")

def singkirkan_ikan():
    try:
        hapus_ikan = input("Masukkan Jenis Ikan Cupang Yang Ingin Disingkirkan: ")
        if hapus_ikan in jenis_cupang:
            jenis_cupang.remove(hapus_ikan)
            print(hapus_ikan, "Telah Disingkirkan")
            print(jenis_cupang)
        else:
            print("Ikan Cupang Tidak Valid")
    except KeyboardInterrupt:
        print("Jangan pencet CTRL C")
    except EOFError:
        print("Jangan pencet CTRL Z")
    except:
        print("Tolong masukkan dengan benar!")

def validasi_kontes():
    try:
        cek_nama = input("\nJenis Ikan Cupang: ")
        if cek_nama not in jenis_cupang:
            print("Ikan Cupang Tidak Valid")
        else:
            cek_umur = int(input("Umur?(Bulan): "))
            cek_penyakit = input("Penyakit?(Ada/Tidak Ada): ")
            cek_fisik = input("Kondisi Fisik?(Luka/Normal): ")
            if cek_penyakit == "Ada" or cek_fisik == "Luka":
                print("\nIkan Cupang Tidak Layak Ikut Kontes")
            else:
                print("\nIkan Cupang Layak Ikut Kontes")
                layak_kontes.append(cek_nama)
                print(cek_nama, "Ditambahkan Ke Daftar Lolos Validasi Kelayakan Kontes")
                print(layak_kontes)
    except ValueError:
        print("Tolong Masukkan Angka!")
    except KeyboardInterrupt:
        print("Jangan pencet CTRL C")
    except EOFError:
        print("Jangan pencet CTRL Z")
    except:
        print("Tolong masukkan dengan benar!")

def update_ikan():
    try:
        lama = input("Pilih Ikan Yang Ingin Diganti: ")
        if lama in jenis_cupang:
            index = jenis_cupang.index(lama)
            baru = input("Masukkan Jenis Ikan Baru: ")
            jenis_cupang[index] = baru
            print(lama, "Telah tergantikan oleh", baru)
            print(jenis_cupang)
        else:
            print("Jenis Ikan Cupang Tidak Valid")
    except KeyboardInterrupt:
            print("Jangan pencet CTRL C")
    except EOFError:
            print("Jangan pencet CTRL Z")
    except:
            print("Tolong masukkan dengan benar!")

login()