from app.database.connection import Database


class BillModel(Database):
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS bills (
            `id` INT AUTO_INCREMENT,
            `reservation_id` INT,
            `price` INT NOT NULL,
            `date` DATETIME DEFAULT CURRENT_TIMESTAMP,
            `approve` TINYINT(1) DEFAULT(0),
            PRIMARY KEY(id),
            FOREIGN KEY(reservation_id) REFERENCES reservations(id)
        )"""
        self.execute(query)
        self.commit()

    def add_bill(self, reservation_id, price):
        self.execute(
            "INSERT INTO `bills` (reservation_id, price) VALUES (%s, %s)",
            (reservation_id, price),
        )
        self.commit()

    def get_bills(self, approved=True):
        self.execute(
            """
            SELECT
                CONCAT(U.first_name, ' ', U.last_name) AS 'fullname',
                R.id,
                R.room_id,
                B.approve,
                B.price,
                B.date
            FROM reservations as R
            INNER JOIN bills as B
            ON R.id = B.reservation_id
            INNER JOIN users as U
            ON U.id = R.customer_id
            WHERE B.approve = 1
            ORDER By B.date"""
        )
        result = self.cursor.fetchall()
        return result

    def get_bill_user(self, _id):
        self.execute(
            """
            SELECT
                CONCAT(U.first_name, ' ', U.last_name) AS 'fullname',
                R.id,
                R.room_id,
                B.approve,
                B.price,
                B.date
            FROM reservations as R
            INNER JOIN bills as B
            ON R.id = B.reservation_id
            INNER JOIN users as U
            ON U.id = R.customer_id
            WHERE U.id = %s
            ORDER By B.date
            """,
            (_id),
        )
        result = self.cursor.fetchone()
        return result

    def drop(self):
        self.execute("DROP TABLE `bills`")
        self.commit()
