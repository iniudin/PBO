import sqlite3

def MenuUtama():
    print("Login")
    
    pilih = input("Sudah mempunyai Akun ?")
    print("[1] Ya")
    print("[2] Tidak")
    if pilih.lower() == "1":
        print("Masukan Username dan Password Anda")
        conn = sqlite3.connect('ProjectDB.db')
        cursor = conn.cursor()
        username = input("Masukan Username: ")
        password = input("Masukkan Password: ")
        query = f"INSERT INTO Login(Username, Password) VALUES('{username}, {password}')"
        cursor.execute(query)
        conn.commit()
        conn.close()
        Menu()
    elif pilih.lower() == "2":
        print("Silahkan melakukan Register terlebih dahulu")
        Register()

    else:
        MenuUtama()

def Register():
    conn = sqlite3.connect('ProjectDB.db')
    cursor = conn.cursor()
    username = input("Masukan Username: ")
    password = input("Masukkan Password: ")     
    email = input("Masukkan E-mail: ")
    tempat = input("Masukan tempat tinggal: ")
    query = f"INSERT INTO Register(Username, Password, Email, TempatTinggal) VALUES('{username}, {password}, {email}, {tempat}')"
    cursor.execute(query)
    conn.commit()
    conn.close()
    
    MenuUtama()

def Menu():
    print(("*"*20),"Dashboard: ",("*"*20))
    print("[1] MyBooking")
    print("[2] Rooms")
    print("[3] Bills")
    print("[4] Feedback")
    print("[5] Logout")
    print("[6] Exit")

    pilih = input("Masukkan pilihan Anda: ")
    if pilih.lower() == "1":
        MyBooking()
    elif pilih.lower() == "2":
        Rooms()
    elif pilih.lower() == "3":
        Bills()
    elif pilih.lower() == "4":
        Feedback()
    elif pilih.lower() == "5":
        MenuUtama()
    else:
        Exit()

def MyBooking():
    print("\nsilahkan pilih kelas kamar yang Anda inginkan: ")
    print("[1] Deluxe Rooms")
    print("[2] Premium Rooms")
    print("[3] Kembali ")

    pilih1 = input("Masukkan pilihan Anda: ")
    if pilih1.lower() == "1":
        print("Anda memilih kelas kamar Deluxe Rooms")
        print("Silahkan pilih harga yang Anda inginkan: ")
        print("\n[1] Kamar A",
                "\n Harga = Rp 250.000/malam",
                "\n Faslitas = luas kamar 22 meter2, AC, kamar mandi dalam, WIFI, TV \n")
        print("\n[2] Kamar B",
                "\n Harga = Rp 350.000/malam",
                "\n Fasilitas = luas kamar 48 meter2 bertipe suite, AC, TV, WIFI, kamar mandi dalam, dan toilet terpisah \n")
        print("[3] Kembali \n")

        pilih2 = input("Masukkan pilihan Anda: ")
        if pilih2.lower() == "1":
            print("Anda telah memilih kamar A")
            print("Permintaan Anda sudah berhasil diproses")
            BackToMenu()
        elif pilih2.lower() == "2":
            print("Anda telah memilih kamar B")
            print("Permintaan Anda sudah berhasil diproses")
            BackToMenu() 
        else :
            MyBooking()
    elif pilih1.lower() == "2":
        print("Anda memilih kelas kamar Premium Rooms")
        print("Silahkan pilih harga yang Anda inginkan: ")
        print("[1] Kamar A",
                "\n Harga = Rp 500.000/malam",
                "\n Fasilitas = luas kamar 48 meter2 bertipe suite, AC, TV, WIFI, kamar mandi dalam, dan toilet terpisah, lobby ukuran 100m2")
        print("[2] Kamar B",
                "\n Harga = Rp 1.000.000/malam",
                "\n Fasilitas = luas kamar 52 meter2 bertipe suite, AC, TV, WIFI, kamar mandi dalam, dan toilet terpisah, lobby ukuran 100m2, laundry, kulkas, jacuzzi, soffa")
        print("[3] Kembali")

        pilih3 = input("Masukkan pilihan Anda: ")
        if pilih3.lower() == "1":
            print("Anda telah memilih kamar A")
            print("Permintaan Anda sudah berhasil diproses")
            BackToMenu()  
        elif pilih3.lower() == "2":
            print("Anda telah memilih kamar B")
            print("Permintaan Anda sudah berhasil diproses")
            BackToMenu() 
        else :
            MyBooking() 
    else :
        BackToMenu()

def Rooms():
    print("\nInformasi kamar yang ingin anda lihat")
    print("[1] Delux Rooms") 
    print("[2] Premium Rooms")
    print("[3] Booking Kamar")
    print("[4] Kembali \n")  

    pilih = input("Masukkan piihan anda: ")
    if pilih.lower() == "1":
        print("Anda memilih kelas kamar Deluxe Rooms")
        print("Kami memiliki 2 tipe Kamar A dan Kamar B: ")
        print("\n[1] Kamar A",
                "\n Harga = Rp 250.000/malam",
                "\n Faslitas = luas kamar 22 meter2, AC, kamar mandi dalam, WIFI, TV \n")
        print("\n[2] Kamar B",
                "\n Harga = Rp 350.000/malam",
                "\n Fasilitas = luas kamar 48 meter2 bertipe suite, AC, TV, WIFI, kamar mandi dalam, dan toilet terpisah \n")
        Rooms()
    elif pilih.lower() == "2":
        print("Anda memilih kelas kamar Premium Rooms")
        print("Kami memiliki 2 tipe Kamar A dan Kamar B: ")
        print("[1] Kamar A",
                "\n Harga = Rp 500.000/malam",
                "\n Fasilitas = luas kamar 48 meter2 bertipe suite, AC, TV, WIFI, kamar mandi dalam, dan toilet terpisah, lobby ukuran 100m2")
        print("[2] Kamar B",
                "\n Harga = Rp 1.000.000/malam",
                "\n Fasilitas = luas kamar 52 meter2 bertipe suite, AC, TV, WIFI, kamar mandi dalam, dan toilet terpisah, lobby ukuran 100m2, laundry, kulkas, jacuzzi, soffa")
        Rooms()
    elif pilih.lower() == "3":
        MyBooking()
    else :
        BackToMenu()



def Bills():
    print("\nMetode pembayaran: ")
    print("[1] Debbit Card")
    print("[2] OVO")
    print("[3] Cash")
    print("[4] Kembali \n")

    pilih = input("Masukkan pilihan Anda: ")
    if pilih.lower() == "1":
        card = input("Masukkan PIN Anda: ")
        print("Transaksi selesai, Terimakasih :)")
    elif pilih.lower() == "2":
        print("Transaksi selesai, Terimakasih :)")
    else: 
        print("Silahkan menuju kasir untuk melakukan pembayaran, Terimakasih :)")

    BackToMenu()

def Feedback():
    print("\n Jika ada saran dan kritik dari Anda: ")
    print("[1] Saran")
    print("[2] Kritik")

    pilih = input("Masukkan pilihan Anda: ")
    if pilih.lower() == "1":
        print("Saran yang ingin Anda sampaikan: ")
        saran = input()
    else:
        print("Kritik yang igin Anda sampaikan: ")
        kritik = input()

    BackToMenu()

def BackToMenu():
    Menu()

def Exit():
    print("Terimakasih atas kunjungannya :)")
    exit

if __name__ == "__main__":
    Menu()
