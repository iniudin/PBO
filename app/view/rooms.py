from app.models.rooms import RoomModel
from app.functions import headline, print_table


class RoomsView(RoomModel):
    def main_menu(self):
        text_menu = (
            ["1", "Daftar Kamar"],
            ["2", "Tambah Kamar"],
            ["3", "Cari Kamar"],
            ["5", "Hapus Kamar"],
            ["0", "Menu utama"],
        )
        print_table("Menu Kamar", ["No", "Deskripsi"], text_menu)
        choice = int(input("> "))
        if choice == 0:
            return
        elif choice == 1:
            self.list_rooms(no_input=True)
        elif choice == 2:
            self.add_room()
        elif choice == 3:
            self.find_room()
        elif choice == 4:
            self.update_room()
        elif choice == 5:
            self.delete_room()
        else:
            print("Perintah tidak ditemukan")

    def list_rooms(self, no_input=None):
        rooms = self.get_rooms()
        column = [i.title() for i in rooms[0].keys()]
        rows = [list(i.values()) for i in rooms]
        print_table("Daftar Kamar", column, rows)
        if no_input:
            self.back_to_menu

    def add_room(self):
        headline("Tambah Kamar")
        room_type = input("Tipe kamar: ")
        room_desc = input("Detail kamar: ")
        price = input("Harga kamar: ")
        self.add(room_type, room_desc, price)
        print("Berhasil menambahkan kamar.")
        self.main_menu()

    def find_room(self):
        headline("Cari Kamar")
        code = input("Masukkan kode kamar: ")
        room = self.find(code)
        column = [i.title() for i in room.keys()]
        rows = [[i for i in room.values()]]
        if len(room) > 0:
            print_table("Kamar ditemukan", column, rows)
        else:
            print("Kamar tidak ditemukan")
        self.back_to_menu

    def delete_room(self):
        headline("Hapus karyawan")
        username = input("Masukkan username: ")
        self.delete(username)
        self.back_to_menu

    @property
    def back_to_menu(self):
        input("Tekan Enter untuk kembali ke Menu")
        self.main_menu()
