from app.models import RoomModel
from app.functions import headline, print_table


class RoomsView(RoomModel):
    def main_menu(self):
        text_menu = (
            ["1", "Daftar Kamar"],
            ["2", "Tambah Kamar"],
            ["3", "Cari Kamar"],
            ["4", "Hapus Kamar"],
            ["0", "Menu utama"],
        )
        print_table("Menu Kamar", ["No", "Deskripsi"], text_menu)
        choice = int(input("> "))
        if choice == 0:
            return
        elif choice == 1:
            self.list_rooms()
        elif choice == 2:
            self.add_room()
        elif choice == 3:
            self.find_room()
        elif choice == 4:
            self.delete_room()
        else:
            print("Perintah tidak ditemukan")

    def list_rooms(self, session=None):
        rooms = self.get_rooms()
        column = [i.title() for i in rooms[0].keys()]
        rows = [list(i.values()) for i in rooms]
        print_table("Daftar Kamar", column, rows)
        if session and session["is_admin"] == 0:
            input("Status:\n1 = Dipesan\n0 = Kosong\nTekan Enter untuk kembali ke Menu")
            return
        self.back_to_menu

    def add_room(self):
        headline("Tambah Kamar")
        room_type = input("Tipe kamar: ")
        room_desc = input("Detail kamar: ")
        price = input("Harga kamar: ")
        self.add(room_type, room_desc, price)
        print("Berhasil menambahkan kamar.")
        self.back_to_menu

    def find_room(self):
        headline("Cari Kamar")
        _id = input("Masukkan id kamar: ")
        room = self.find(_id)
        column = [i.title() for i in room.keys()]
        rows = [[i for i in room.values()]]
        if len(room) > 0:
            print_table("Kamar ditemukan", column, rows)
        else:
            print("Kamar tidak ditemukan")
        self.back_to_menu

    def delete_room(self):
        headline("Hapus Kamar")
        kamar_id = input("Masukkan id kamar: ")
        self.delete(kamar_id)
        self.back_to_menu

    @property
    def back_to_menu(self):
        input("Tekan Enter untuk kembali ke Menu")
        self.main_menu()
