from app.models.RoomsModel import Rooms
from app.functions import headline


class RoomsView(Rooms):
    def menu(self):
        headline("Perintah Kamar")
        text = ["1. tambah kamar", "2. daftar kamar", "3. dll", "0. Menu utama"]

        print("\n".join(text))
        choice = int(input("> "))
        if choice == 0:
            exit()
        elif choice == 1:
            pass
        elif choice == 2:
            pass

    def tambah_data(self):
        room_code = input("nananan: ")
        room_type = input("nananan: ")
        room_description = input("nananan: ")
        price = input("nananan: ")
        self.insert(code, type, description, price)