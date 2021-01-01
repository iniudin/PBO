from app.database.connection import Database


class BillModel(Database):
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS bills (
            `id` INT AUTO_INCREMENT,
            `reservation_id` INT,
            `price` INT NOT NULL,
            `date` DATETIME DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY(id),
            FOREIGN KEY(reservation_id) REFERENCES reservations(id)
        )"""
        self.execute(query)
        self.commit()

    def insert(
        self,
        reservation_id,
    ):
        self.execute(
            "INSERT INTO `bills` (reservation_id) VALUES (%s)",
            (reservation_id,),
        )
        self.commit()

    def get_all(self):
        self.execute("SELECT * FROM `bills`")
        result = self.cursor.fetchall()
        return result

    def find(self, id):
        self.execute("SELECT * FROM `bills` WHERE id = %s", (id,))
        result = self.cursor.fetchone()
        return result

    def delete(self, id):
        self.execute("DELETE FROM `bills` WHERE id = %s", (id,))

    def drop(self):
        self.execute("DROP TABLE `bills`")
        self.commit()
