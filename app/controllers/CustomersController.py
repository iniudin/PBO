from app.models.CustomerModel import Customers
from app.functions import headline

class CustomersView(Customers):
    def menu(self):
        headline("Main Menu")
        text = ["1. Info Kamar", "2.Pemesanan", "3. Pembayaran", "0. Menu utama"]

        print("\n".join(text))
        choice = int(input("> "))
        if choice == 0:
            exit()
        elif choice == 1:
            Rooms()
        elif choice == 2:
            Reservation()
        elif choice == 3:
            Bills()
    
    def Registrasi(self):
        headline("Registrasi")
        first_name=input("First Name : ")
        last_name=input("Last Name : ")
        password=input("Password : ")
        email=input("Email : ")
        phone=input("Phone: ")
        address=input("Address: ")
        gender=input("Gender : ")
