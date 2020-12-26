from app.models.RoomsModel import Rooms


class RoomsView(Rooms):
    def tambah_data(self):
        room_code = input("nananan: ")
        room_type = input("nananan: ")
        room_description = input("nananan: ")
        price = input("nananan: ")
        self.insert(code, type, description, price)