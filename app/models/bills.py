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

    def get_bills(self, approved=1):
        # sudah dibayar
        if approved == 1:
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
            ORDER By B.date
            """,
            )
        elif approved == 0:
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
                WHERE B.approve = 0
                ORDER By B.date
                """,
            )
        else:
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
                ORDER By B.date
                """,
            )
        result = []
        for res in self.cursor.fetchall():
            result.append(
                {
                    "Nama Lengkap": res["fullname"],
                    "ID Resi": res["id"],
                    "Id Kamar": res["room_id"],
                    "Status": "terbayar" if res["approve"] else "belum dibayar",
                    "Tagihan": res["price"],
                    "Tanggal Resi": res["date"],
                }
            )
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
        result = []
        for res in self.cursor.fetchall():
            result.append(
                {
                    "Nama Lengkap": res["fullname"],
                    "ID Resi": res["id"],
                    "Id Kamar": res["room_id"],
                    "Status": "terbayar" if res["approve"] else "belum dibayar",
                    "Tagihan": res["price"],
                    "Tanggal Resi": res["date"],
                }
            )
        return result

    def change_status(self, _id):
        query = "UPDATE bills SET approve = 1 WHERE reservation_id = %s"
        self.execute(query, (_id))
        self.commit()

    def drop(self):
        self.execute("DROP TABLE `bills`")
        self.commit()
