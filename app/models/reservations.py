from app.database.connection import Database
from app.functions import get_date_today


class ReservationModel(Database):
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS `reservations` (
            `id` INT AUTO_INCREMENT,
            `customer_id` INT NOT NULL,
            `room_id` INT NOT NULL,
            `check_in` DATETIME NOT NULL,
            `check_out` DATETIME,
            PRIMARY KEY(id),
            FOREIGN KEY(customer_id) REFERENCES users(id),
            FOREIGN KEY(room_id) REFERENCES rooms(id)
        )"""
        self.execute(query)
        self.commit()

    def check_in(
        self,
        customer_id,
        room_id,
    ):
        self.execute(
            """
            INSERT INTO reservations (
                customer_id,
                room_id,
                check_in
            )
            VALUES (%s,%s,%s)
            """,
            (customer_id, room_id, get_date_today()),
        )
        self.commit()

    def check_out(self, _id, customer_id):
        self.execute(
            "UPDATE reservations SET check_out = %s WHERE id = %s AND customer_id=%s",
            (get_date_today(), _id, customer_id),
        )
        self.commit()

    def get_reservation_user(self, user_id):
        self.execute("SELECT * FROM reservations WHERE customer_id = %s", (user_id))
        result = self.cursor.fetchall()
        return result

    def get_reservation(self, _id):
        self.execute("SELECT * FROM reservations WHERE id = %s", (_id))
        result = self.cursor.fetchone()
        return result

    def delete(self, id):
        self.execute("DELETE FROM reservations WHERE id = %s", (id,))

    def drop(self):
        self.execute("DROP TABLE reservations")
        self.commit()
