from app.models.users import UserModel
from app.functions import headline, print_table


class RoomsView(UserModel):
    def main_menu(self):
        text_menu = (
            ["1", "Daftar Kamar"],
            ["2", "Tambah Kamar"],
            ["3", "Cari Kamar"],
            ["4", "Ubah detail Kamar"],
            ["5", "Hapus Kamar"],
            ["0", "Menu utama"],
        )
        print_table("Menu Kamar", ["No", "Deskripsi"], text_menu)
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
        column = ["Nama Lengkap", "Username", "Role", "Tanggal Daftar"]
        print_table("Daftar Karyawan", column, admins)
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
        try:
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
        except Exception as err:
            print(err)
        print("Berhasil menambahkan admin.")
        self.main_menu()

    def find_employee(self):
        headline("Cari karyawan")
        username = input("Masukkan username: ")
        admins = self.find_user(username)
        column = ["Nama Lengkap", "Username", "Role", "Tanggal Daftar"]
        if len(admins) > 0:
            print_table("Daftar Karyawan", column, admins)
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
        is_agree = input("Apakah anda yakin untuk mengupdate data karyawan?")
        if is_agree:
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

    def delete_employee(self):
        headline("Hapus karyawan")
        username = input("Masukkan username: ")
        self.delete(username)
        self.back_to_menu

    @property
    def back_to_menu(self):
        input("Tekan Enter untuk kembali ke Menu")
        self.main_menu()
