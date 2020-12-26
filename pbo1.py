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
    print("Dashboard: ")
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
    elif pilih.lower() == "6":
        Exit()
    else:
        Exit()

def MyBooking():
    print("Daftar kelas kamar: ")
    print("[1] Daftar deluxe rooms")
    print("[2] Daftar premmium roos")

    pilih = input("Pilih kelas kelas kamar yang anda inginkan: ")
    if pilih.lower() == "1":
        print("[1] Kamar A")
        print("[2] Kamar B")
        print("[3] Kamar C")
        print("[4] Kamar D")
        print("[5] Kamar E")

        print("Kamar dengan kelas deluxe rooms yang tersedia: ")
        #Jadi disini kita isi database dari kelas premium kamar itu
        #Jadi harus ada data kamar dulu biar nanti user tinggal melakukan pemesanan 
        #Dan pemilihannya itu dari keersedian kamar, kamar mana saja yang kosong dan itu akan jadi pesanan untuk user
        conn = sqlite3.connect('ProjectDB.db')
        cursor = conn.cursor()
        query = "SELECT INTO ListRoomsDeluxe(IDRooms, Tipekamar, Fasilitas, Harga, Booking)"
        cursor.execute(query)
        conn.commit()
        conn.close()
        pilih1 = input("Pilih kamar: ")
        #Dan pilihan ini tergantung banyaknya kamar yang tersedia
        if pilih1.lower == "1":
            print("Terimakasih atas pemesanannya :)")
            print("Permintaan anda akan kami proses")
            Bills()

        elif pilih1.lower == "2":
            print("Terimakasih atas pemesanannya :)")
            print("Permintaan anda akan kami proses")
            Bills()

        elif pilih1.lower == "3":
            print("Terimakasih atas pemesanannya :)")
            print("Permintaan anda akan kami proses")
            Bills()

        elif pilih1.lower == "4":
            print("Terimakasih atas pemesanannya :)")
            print("Permintaan anda akan kami proses")
            Bills()

        elif pilih1.lower == "5":
            print("Terimakasih atas pemesanannya :)")
            print("Permintaan anda akan kami proses")
            Bills()

        else:
            ListRooms()

    else:
        print("[1] Kamar A")
        print("[2] Kamar B")
        print("[3] Kamar C")
        print("[4] Kamar D")
        print("[5] Kamar E")

        print("Kamar dengan kelas premium rooms yang tersedia: ")
        #Jadi disini kita isi database dari kelas premium kamar itu
        #Jadi harus ada data kamar dulu biar nanti user tinggal melakukan pemesanan 
        #Dan pemilihannya itu dari keersedian kamar, kamar mana saja yang kosong dan itu akan jadi pesanan untuk user
        conn = sqlite3.connect('ProjectDB.db')
        cursor = conn.cursor()
        query = "SELECT INTO ListRoomsPremiums(IDRooms, Tipekamar, Fasilitas, Harga, Booking)"
        cursor.execute(query)
        conn.commit()
        conn.close()
        pilih2 = input("Pilih kamar: ")
        #Dan pilihan ini tergantung banyaknya kamar yang tersedia
        if pilih2.lower == "1":
            print("Terimakasih atas pemesanannya :)")
            print("Permintaan anda akan kami proses")
            Bills()

        elif pilih2.lower == "2":
            print("Terimakasih atas pemesanannya :)")
            print("Permintaan anda akan kami proses")
            Bills()

        elif pilih2.lower == "3":
            print("Terimakasih atas pemesanannya :)")
            print("Permintaan anda akan kami proses")
            Bills()

        elif pilih2.lower == "4":
            print("Terimakasih atas pemesanannya :)")
            print("Permintaan anda akan kami proses")
            Bills()

        elif pilih2.lower == "5":
            print("Terimakasih atas pemesanannya :)")
            print("Permintaan anda akan kami proses")
            Bills()

        else:
            ListRooms()

def Bills():
    print("Metode pembayaran: ")
    print("[1] Debbit Card")
    print("[2] Cash")

    pilih = input("Masukkan pilihan Anda: ")
    if pilih.lower() == "1":
        Pin = input("Masukkan PIN Anda: ")
        conn = sqlite3.connect('ProjectDB.db')
        cursor = conn.cursor()
        query = f"INSERT INTO Bills(Pin) VALUES('{Pin}')"
        cursor.execute(query)
        conn.commit()
        conn.close()
        print("Transaksi selesai, Terimakasih :)")
    else: 
        print("Silahkan menuju kasir untuk melakukan pembayaran, Terimakasih :)")

    BackToMenu()

def Feedback():
    print("Jika ada saran dan kritik dari Anda: ")
    print("[1] Saran")
    print("[2] Kritik")

    pilih = input("Masukkan pilihan Anda: ")
    if pilih.lower() == "1":
        print("Saran yang ingin Anda sampaikan: ")
        saran = input()
        conn = sqlite3.connect('ProjectDB.db')
        cursor = conn.cursor()
        query = f"INSERT INTO Saran(Saran) VALUES('{Saran}')"
        cursor.execute(query)
        conn.commit()
        conn.close()
        print("Terima Kasih atas sarannya :)")
    else:
        print("Kritik yang igin Anda sampaikan: ")
        kritik = input()
        conn = sqlite3.connect('ProjectDB.db')
        cursor = conn.cursor()
        query = f"INSERT INTO Kritik(Kritik) VALUES('{Kritik}')"
        cursor.execute(query)
        conn.commit()
        conn.close()
        print("Terima Kasih atas kritiknya :)")

    BackToMenu()

def BackToMenu():
    Menu()

def Exit():
    exit

if __name__ == "__main__":
    menu()
