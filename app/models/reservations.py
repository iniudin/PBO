from app.database.connection import Database


class Reservations(Database):
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS `reservations` (
            `id` INT AUTO_INCREMENT,
            `customer_id` INT NOT NULL,
            `room_id` INT NOT NULL,
            `check_in` DATETIME NOT NULL,
            `check_out` DATETIME NOT NULL,
            `price` INT NOT NULL,
            PRIMARY KEY(id),
            FOREIGN KEY (customer_id) REFERENCES users(id),
            FOREIGN KEY (room_id) REFERENCES rooms(id)
        )"""
        self.execute(query)
        self.commit()

    def insert(
        self,
        customer_id,
        room_id,
        check_in,
        check_out,
    ):
        self.execute(
            """
            INSERT INTO reservations (
                customer_id,
                room_id,
                check_in,
                check_out
            )
            VALUES (%s,%s,%s,%s)
            """,
            (
                customer_id,
                room_id,
                check_in,
                check_out,
            ),
        )
        self.commit()

    def fetch_all(self):
        self.execute("SELECT * FROM reservations")
        result = self.cursor.fetchall()
        return result

    def find(self, id):
        self.execute("SELECT * FROM reservations WHERE id = ?", (id,))
        result = self.cursor.fetchone()
        return result

    def delete(self, id):
        self.execute("DELETE FROM reservations WHERE id = ?", (id,))

    def drop(self):
        self.execute("DROP TABLE reservations")
        self.commit()