from app.models import ReservationModel, RoomModel, BillModel
from .rooms import RoomsView
from app.functions import count_days


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
        try:
            resi = ReservationModel().get_reservation(customer_id)["id"]
            self.check_out(resi, customer_id)
            resi = ReservationModel().get_reservation(customer_id)
            resi_id = resi["id"]
            check_in = resi["check_in"]
            check_out = resi["check_out"]
            room_id = resi["room_id"]

            day = count_days(check_in, check_out)
            if day == 0:
                price = (day + 1) * 300
            else:
                price = day * 300
            BillModel().add_bill(resi_id, price)
            RoomModel().change_status(room_id, 0)
            print("Checkout berhasil")
            print("Tagihan telah ditambahkan, silahkan cek di menu pembayaran.")

        except Exception as err:
            print("Error: ", err)
        self.back_to_menu

    @property
    def back_to_menu(self):
        input("Tekan Enter untuk kembali ke Menu")
        return
