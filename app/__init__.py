from app.models import UserModel, Auth
from app.functions import print_table, headline
from app.views import (
    EmployeesView,
    CustomersView,
    RoomsView,
    ReservationsView,
    BillsView,
)


class App:
    __session = {}

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
            ["1", "Karyawan", "Manajemen karyawan"],
            ["2", "Pelanggan", "Manajemen pelanggan"],
            ["3", "Kamar", "Manajemen Kamar"],
            ["4", "Transaksi", "Catatan transaksi"],
            ["0", "Keluar", "-"],
        )

        menu_admin = (
            ["1", "Pelanggan", "Manajemen pelanggan"],
            ["2", "Kamar", "Manajemen Kamar"],
            ["3", "Transaksi", "Cek Transaksi"],
            ["0", "Keluar", "-"],
        )

        menu_user = (
            ["1", "Kamar", "Lihat daftar kamar yang tersedia"],
            ["2", "Check in", "Pesan kamar disini"],
            ["3", "Check out", "Check out kamar disini."],
            ["4", "Pembayaran", "Bayar tagihan anda disini"],
            ["0", "Keluar", "-"],
        )

        if self.__session["is_admin"] == 0:
            text = menu_user
        elif self.__session["is_admin"] == 1:
            text = menu_admin
        else:
            text = menu_owner

        print_table("Main Menu", colomn, text)
        choice = int(input("> "))
        # owner
        if self.__session["is_admin"] == 2:
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

        # karyawan
        elif self.__session["is_admin"] == 1:
            if choice == 0:
                exit()
            elif choice == 1:
                CustomersView().main_menu()
            elif choice == 2:
                RoomsView().main_menu()
            elif choice == 3:
                pass

        # Pelanggan
        else:
            if choice == 0:
                exit()
            elif choice == 1:
                RoomsView().list_rooms(session=self.__session)
            elif choice == 2:
                ReservationsView().book_room(session=self.__session)
            elif choice == 3:
                ReservationsView().checkout_room(session=self.__session)
            elif choice == 4:
                BillsView().mybills(session=self.__session)

    def run(self):
        while True:
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
            else:
                self.main_menu()
