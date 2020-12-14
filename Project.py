def MenuUtama():
    print("Login")
    pilih = input("Apakah anda ingin login Aplikasi ?")
    print("[1] Yes")
    print("[2] No")

    if pilih.lower() == "1":
        Main()
    elif pilih.lower() == "2":
        Exit()
    else:
        Exit()

def Main():
    pilih1 = input("Username: ")
    pilih2 = input("Password: ")


def Menu():
    print("Dashboard")
    print("[1] MyBooking")
    print("[2] Rooms")
    print("[3] Bills")
    print("[4] Feedback")
    print("[5] Logout")

    pilih = input("Pilih menu: ")
    if pilih.lower() == "1":
        Booking()
    elif pilih.lower() == "2":
        Rooms()
    elif pilih.lower() == "3":
        Bills()
    elif pilih.lower() == "4":
        Feedback()
    elif pilih.lower() == "5":
        Exit()
    else:
        Exit()

def BackToMenu():
    Menu()

def Booking():
    
def Rooms():

def Bills():

def Feedback():


def Exit():
    exit

if __name__ == "__main__":
    menu()
