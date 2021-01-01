from app.models import ReservationModel, RoomModel
from .rooms import RoomsView


class ReservationsView(ReservationModel):
    def book_room(self, session):
        user_id = session["id"]
        RoomsView().list_rooms(session=session)
        room_code = input("Masukkan code kamar:")
        room = RoomModel().find(room_code)
        if room:
            room_id = room["id"]
            if room["status"] == 1:
                print("Maaf Kamar telah dipesan")
                self.back_to_menu
            else:
                self.check_in(user_id, room_id)
                RoomModel().change_status(room_code, 1)
                print("Kamar berhasil dipesan")
        else:
            print("Kode kamar tidak ditemukan")
            self.back_to_menu

    def checkout_room(self, session):
        customer_id = session["id"]
        self.get_reservation(customer_id)

    @property
    def back_to_menu(self):
        input("Tekan Enter untuk kembali ke Menu")
        return
