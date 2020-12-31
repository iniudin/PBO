from app.models.users import UserModel
from app.functions import headline, print_table


class EmployeesView(UserModel):
    def main_menu(self):
        text_menu = (
            ["1", "Daftar karyawan"],
            ["2", "Tambah karyawan"],
            ["3", "Cari karyawan"],
            ["4", "Ubah detail karyawan"],
            ["5", "Hapus karyawan"],
            ["0", "Menu utama"],
        )
        print_table("Menu Karyawan", ["No", "Deskripsi"], text_menu)
        choice = int(input("> "))
        if choice == 0:
            return
        elif choice == 1:
            self.list_employee(no_input=True)
        elif choice == 2:
            self.add_employee()
        elif choice == 3:
            self.find_employee()
        elif choice == 4:
            self.update_employee()
        elif choice == 5:
            self.delete_employee()
        else:
            print("Perintah tidak ditemukan")

    def list_employee(self, no_input=None):
        admins = self.get_admins()
        column = [i.title() for i in admins[0].keys()]
        rows = [list(i.values()) for i in admins]
        print_table("Daftar Karyawan", column, rows)
        if no_input:
            self.back_to_menu

    def add_employee(self):
        headline("Tambah karyawan")
        first_name = input("Masukkan nama depan: ")
        last_name = input("Masukkan nama belakang: ")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        email = input("Masukkan email: ")
        phone = input("Masukkan phone: ")
        address = input("Masukkan address: ")
        gender = input("Masukkan gender (L/P): ")
        self.add_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
            phone=phone,
            address=address,
            gender=gender,
            is_admin=1,
        )
        print("Berhasil menambahkan admin.")
        self.main_menu()

    def find_employee(self):
        headline("Cari karyawan")
        username = input("Masukkan username: ")
        admins = self.find_user(username)
        column = [i.title() for i in admins.keys()]
        rows = [[i for i in admins.values()]]
        if len(admins) > 0:
            print_table("User ditemukan", column, rows)
        else:
            print("User tidak ditemukan")
        self.back_to_menu

    def update_employee(self):
        self.list_employee(no_input=False)
        user_id = input("Masukkan Id Karyawan:")
        if user_id == 0:
            print("Anda tidak dapat mengubah data Owner!")
            self.back_to_menu

        first_name = input("Masukkan nama depan (baru):")
        last_name = input("Masukkan nama belakang (baru):")
        username = input("Masukkan username (baru):")
        password = input("Masukkan password (baru):")
        email = input("Masukkan email (baru):")
        phone = input("Masukkan phone (baru):")
        address = input("Masukkan address (baru):")
        is_agree = input("Apakah anda yakin untuk mengupdate data karyawan? (y/n)")
        if is_agree.lower() == "y":
            self.update_employee(
                first_name,
                last_name,
                username,
                password,
                email,
                phone,
                address,
                is_agree,
                user_id,
            )
            print("Detail karyawan berhasil di update")
        else:
            print("Batal mengupdate detail karyawan")
        self.back_to_menu

    def delete_employee(self):
        headline("Hapus karyawan")
        username = input("Masukkan username: ")
        self.delete(username)
        self.back_to_menu

    @property
    def back_to_menu(self):
        input("Tekan Enter untuk kembali ke Menu")
        self.main_menu()
