from app.models.users import UserModel
from app.functions import headline, print_table


class CustomersView(UserModel):
    def main_menu(self):
        text_menu = (
            ["1", "Daftar Pelanggan"],
            ["2", "Cari Pelanggan"],
            ["3", "Hapus Pelanggan"],
            ["0", "Menu utama"],
        )
        print_table("Menu Pelanggan", ["No", "Deskripsi"], text_menu)
        choice = int(input("> "))
        if choice == 0:
            return
        elif choice == 1:
            self.list_customers(no_input=True)
        elif choice == 2:
            self.find_customer()
        elif choice == 3:
            self.delete_customer()
        else:
            print("Perintah tidak ditemukan")

    def list_customers(self, no_input=None):
        customers = self.get_customers()
        column = [i.title() for i in customers[0].keys()]
        rows = [list(i.values()) for i in customers]
        print_table("Daftar Pelanggan", column, rows)
        if no_input:
            self.back_to_menu

    def find_customer(self):
        headline("Cari Pelanggan")
        username = input("Masukkan username: ")
        admins = self.find_user(username)
        column = [i.title() for i in admins.keys()]
        rows = [[i for i in admins.values()]]
        if len(admins) > 0:
            print_table("User ditemukan", column, rows)
        else:
            print("User tidak ditemukan")
        self.back_to_menu

    def delete_customer(self):
        headline("Hapus Pelanggan")
        username = input("Masukkan username: ")
        self.delete(username)
        self.back_to_menu

    @property
    def back_to_menu(self):
        input("Tekan Enter untuk kembali ke Menu")
        self.main_menu()
