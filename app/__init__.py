from app.functions import headline
from app.Models.RoomModel import Room
from app.Database.DBconnection import Database


class App:

    __session: str = ""

    def login(self):
        headline("Login")
        username = input("Username: ")
        password = input("Password: ")
        if username == "user" and password == "pass":
            self.__session = username + password
        else:
            print("Kombinasi user dan password salah")

    def register(self):
        pass

    def main_menu(self):
        headline("Main Menu")
        text_menu = [
            "1. MyRoom",
            "2. MyBills",
            "0. Exit",
        ]
        print("\n".join(text_menu))
        choice = int(input("> "))
        if choice == 0:
            exit()
        elif choice == 1:
            pass
        elif choice == 2:
            pass

    def run(self):

        # data = Database()
        # Room().create_table()
        # Room().drop()
        # Room().insert("biasa", "ya biasa biasa aja")
        # Room().update(id=2, type="luar biasa")
        Room().fetch_all()
        # while True:
        # if not self.__session:
        #     self.login()
        # else:
        #     self.main_menu()
