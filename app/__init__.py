from app.functions import headline
from app.Database.DBconnection import Database
from app.Models.UserModel import Users


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
            check = input("Mau daftar? (y/N)")
            if check.lower == "y":
                self.register()
            else:
                exit()

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
        while True:
            if not self.__session:
                self.login()
            else:
                self.main_menu()
