from app.models import ReservationModel, RoomModel, BillModel
from .rooms import RoomsView
from app.functions import count_days, print_table


class ReservationsView(ReservationModel):
    def book_room(self, session):
        user_id = session["id"]
        RoomsView().list_rooms(session=session)
        room_code = input("Masukkan id kamar: ")
        room = RoomModel().find(room_code)
        if room:
            room_id = room["id"]
            if room["status"] == 1:
                print("Maaf Kamar telah dipesan")
            else:
                self.check_in(user_id, room_id)
                RoomModel().change_status(room_code, 1)
                print("Kamar berhasil dipesan")
        else:
            print("Id kamar tidak ditemukan")
        self.back_to_menu

    def checkout_room(self, session):
        customer_id = session["id"]
        try:
            list_resi = self.get_reservation_user(customer_id)
            column = [i.title() for i in list_resi[0].keys()]
            rows = [list(i.values()) for i in list_resi]
            print_table("Reservasi", column, rows)

            resi_id = input("Masukkan No Reservasi: ")
            resi = self.get_reservation(resi_id)
            if not resi["check_out"]:
                # catat tanggal check out
                self.check_out(resi_id, customer_id)
                # get new resi details
                new_resi = self.get_reservation(resi_id)
                check_in, check_out, room_id = (
                    new_resi["check_in"],
                    new_resi["check_out"],
                    new_resi["room_id"],
                )
                day = count_days(check_in, check_out)
                if day == 0:
                    price = (day + 1) * 300
                else:
                    price = day * 300
                BillModel().add_bill(resi_id, price)
                RoomModel().change_status(room_id, 0)
                print("Checkout berhasil")
                print("Tagihan telah ditambahkan, silahkan cek di menu transaksi.")
            else:
                print("Anda telah check out sebelumnya terima kasih :)")
        except Exception as err:
            print("Error:", err)
        self.back_to_menu

    @property
    def back_to_menu(self):
        input("Tekan Enter untuk kembali ke Menu")
        return
