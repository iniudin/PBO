from app.Database.DBconnection import Database


class Account(Database):
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS `account` (
            `id` INTEGER PRIMARY KEY,
            `username` VARCHAR(15),
            `password` VARCHAR(15),
            `user_id` VARCHAR(10)
        )"""
        self.execute(query)
        self.commit()

    def insert(self, username, password):
        self.execute(
            "INSERT INTO account (`username`, `password`) values (?,?)",
            (
                username,
                password,
            ),
        )
        self.commit()

    def change_password(self, id, password):
        self.execute(
            "UPDATE account SET `password` = ? WHERE `id` = ?",
            (
                password,
                id,
            ),
        )
        self.commit()

    def fetch_all(self):
        self.execute("SELECT * FROM account")
        result = self.cursor.fetchall()

    def delete(self, id):
        self.execute("DELETE FROM account WHERE id = ?", (id,))

    def drop(self):
        self.execute("DROP TABLE account")
        self.commit()