from app.models.ReservationsModel import Reservations
from app.functions import headline

class ReservationsView(Reservations):
    def Menu(self):
        headline("Daftar kelas kamar: ")
        text = ["1. Deluxe Rooms",
                "2. Permium Rooms",
                "0. Menu Utama"]

        print("\n".join(text))
        choice = int(input(">"))
        if choice == 1:
            headline("Daftar kelas kamar Deluxe Rooms: ")
            text = ["1. Kamar A",
                    "2. Kamar B",
                    "3. Kamar C",
                    "4. Kamar D",
                    "5. Kamar E"]

            print("\n".join(text))
            choice1 = int(input(">"))
            if choice1 == 1:
                headline("Daftar kelas kamar Deluxe Rooms A: ")
                text = ["1. Kamar A 1",
                        "2. Kamar A 2",
                        "3. Kamar A 3",
                        "4. Kamar A 4",
                        "5. Kamar A 5"]

                choice2 = int(input(">"))
                if choice2 == 1:
                    pass
                elif choice2 == 2:
                    pass
                elif choice2 == 3:
                    pass
                elif choice2 == 4:
                    pass
                elif choice2 == 5:
                    pass
            if choice1 == 2:
                headline("Daftar kelas kamar Deluxe Rooms B: ")
                text = ["1. Kamar B 1",
                        "2. Kamar B 2",
                        "3. Kamar B 3",
                        "4. Kamar B 4",
                        "5. Kamar B 5"]

                choice2 = int(input(">"))
                if choice2 == 1:
                    pass
                elif choice2 == 2:
                    pass
                elif choice2 == 3:
                    pass
                elif choice2 == 4:
                    pass
                elif choice2 == 5:
                    pass
            if choice1 == 3:
                headline("Daftar kelas kamar Deluxe Rooms C: ")
                text = ["1. Kamar C 1",
                        "2. Kamar C 2",
                        "3. Kamar C 3",
                        "4. Kamar C 4",
                        "5. Kamar C 5"]

                choice2 = int(input(">"))
                if choice2 == 1:
                    pass
                elif choice2 == 2:
                    pass
                elif choice2 == 3:
                    pass
                elif choice2 == 4:
                    pass
                elif choice2 == 5:
                    pass
            if choice1 == 4:
                headline("Daftar kelas kamar Deluxe Rooms D: ")
                text = ["1. Kamar D 1",
                        "2. Kamar D 2",
                        "3. Kamar D 3",
                        "4. Kamar D 4",
                        "5. Kamar D 5"]

                choice2 = int(input(">"))
                if choice2 == 1:
                    pass
                elif choice2 == 2:
                    pass
                elif choice2 == 3:
                    pass
                elif choice2 == 4:
                    pass
                elif choice2 == 5:
                    pass
            if choice1 == 5:
                headline("Daftar kelas kamar Deluxe Rooms E: ")
                text = ["1. Kamar E 1",
                        "2. Kamar E 2",
                        "3. Kamar E 3",
                        "4. Kamar E 4",
                        "5. Kamar E 5"]

                choice2 = int(input(">"))
                if choice2 == 1:
                    pass
                elif choice2 == 2:
                    pass
                elif choice2 == 3:
                    pass
                elif choice2 == 4:
                    pass
                elif choice2 == 5:
                    pass
        elif choice == 2:
            headline("Daftar kelas kamar Premium Rooms: ")
            text = ["1. Kamar A",
                    "2. Kamar B",
                    "3. Kamar C",
                    "4. Kamar D",
                    "5. Kamar E"]

            print("\n".join(text))
            choice1 = int(input(">"))
            if choice1 == 1:
                headline("Daftar kelas kamar Premium Rooms A: ")
                text = ["1. Kamar A 1",
                        "2. Kamar A 2",
                        "3. Kamar A 3",
                        "4. Kamar A 4",
                        "5. Kamar A 5"]

                choice2 = int(input(">"))
                if choice2 == 1:
                    pass
                elif choice2 == 2:
                    pass
                elif choice2 == 3:
                    pass
                elif choice2 == 4:
                    pass
                elif choice2 == 5:
                    pass
            if choice1 == 2:
                headline("Daftar kelas kamar Premium Rooms B: ")
                text = ["1. Kamar B 1",
                        "2. Kamar B 2",
                        "3. Kamar B 3",
                        "4. Kamar B 4",
                        "5. Kamar B 5"]

                choice2 = int(input(">"))
                if choice2 == 1:
                    pass
                elif choice2 == 2:
                    pass
                elif choice2 == 3:
                    pass
                elif choice2 == 4:
                    pass
                elif choice2 == 5:
                    pass
            if choice1 == 3:
                headline("Daftar kelas kamar Premium Rooms C: ")
                text = ["1. Kamar C 1",
                        "2. Kamar C 2",
                        "3. Kamar C 3",
                        "4. Kamar C 4",
                        "5. Kamar C 5"]

                choice2 = int(input(">"))
                if choice2 == 1:
                    pass
                elif choice2 == 2:
                    pass
                elif choice2 == 3:
                    pass
                elif choice2 == 4:
                    pass
                elif choice2 == 5:
                    pass
            if choice1 == 4:
                headline("Daftar kelas kamar Premium Rooms D: ")
                text = ["1. Kamar D 1",
                        "2. Kamar D 2",
                        "3. Kamar D 3",
                        "4. Kamar D 4",
                        "5. Kamar D 5"]

                choice2 = int(input(">"))
                if choice2 == 1:
                    pass
                elif choice2 == 2:
                    pass
                elif choice2 == 3:
                    pass
                elif choice2 == 4:
                    pass
                elif choice2 == 5:
                    pass
            if choice1 == 5:
                headline("Daftar kelas kamar Premium Rooms E: ")
                text = ["1. Kamar E 1",
                        "2. Kamar E 2",
                        "3. Kamar E 3",
                        "4. Kamar E 4",
                        "5. Kamar E 5"]

                choice2 = int(input(">"))
                if choice2 == 1:
                    pass
                elif choice2 == 2:
                    pass
                elif choice2 == 3:
                    pass
                elif choice2 == 4:
                    pass
                elif choice2 == 5:
                    pass
        elif choice == 0:
            exit()
        else:
            Menu()

    def Booking(self):
        pemesanan = input("Pemesanan kamar: ")
        tipe_kamar = input("tipe kamar: ")
        self.INSERT()
    
