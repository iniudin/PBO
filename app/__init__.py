from app.models.users import UserModel
from app.models.rooms import RoomModel

from app.models.auth import Auth
from app.functions import print_table, headline
from app.view.employees import EmployeesView
from app.view.customers import CustomersView
from app.view.rooms import RoomsView


class App:
    __session = []

    def login(self):
        headline("Login")
        username = input("Username: ")
        password = input("Password: ")
        self.__session = Auth().login_session(username, password)
        if self.__session:
            self.main_menu()
        else:
            print("Kombinasi user dan password salah")
            check = input("Mau daftar? (y/N)")
            if check.lower() == "y":
                self.register()
            else:
                exit()

    def register(self):
        headline("Pendaftaran Pelanggan")
        first_name = input("Masukkan nama depan: ")
        last_name = input("Masukkan nama belakang: ")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        email = input("Masukkan email: ")
        phone = input("Masukkan phone: ")
        address = input("Masukkan address: ")
        gender = input("Masukkan gender (L/P): ")
        try:
            UserModel().add_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                email=email,
                phone=phone,
                address=address,
                gender=gender,
                is_admin=0,
            )
        except Exception as err:
            return print(err)
        print("Berhasil daftar silahkan login.")
        self.login()

    def main_menu(self):
        colomn = ["No", "Perintah", "Deskripsi"]
        menu_owner = (
            ["1", "Karyawan", "Management karyawan"],
            ["2", "Pelanggan", "Management pelanggan"],
            ["3", "Kamar", "Management Kamar"],
            ["4", "Transaksi", "Catatan transaksi"],
            ["0", "Keluar", "-"],
        )

        print_table("Main Menu", colomn, menu_owner)
        choice = int(input("> "))
        if choice == 0:
            exit()
        elif choice == 1:
            EmployeesView().main_menu()
        elif choice == 2:
            CustomersView().main_menu()
        elif choice == 3:
            RoomsView().main_menu()
        elif choice == 4:
            pass

    def run(self):
        while True:
            """
            if not self.__session:
                column = ["No", "Perintah"]
                rows = [["1", "Login"], ["2", "Register"], ["0", "Keluar"]]
                print_table("Selamat datang di MyHotel", column, rows)
                choice = int(input("> "))
                if choice == 0:
                    exit()
                elif choice == 1:
                    self.login()
                elif choice == 2:
                    self.register()
            else:"""
            self.main_menu()
