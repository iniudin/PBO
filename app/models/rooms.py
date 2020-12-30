from app.database.connection import Database


class RoomModel(Database):
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS `rooms` (
            `id` INT AUTO_INCREMENT,
            `code` VARCHAR(5) UNIQUE NOT NULL,
            `type` VARCHAR(20) NOT NULL,
            `description` VARCHAR(250) NOT NULL,
            `status` ENUM(1, 0) NOTNULL,
            `price` INT NOT NULL,
            PRIMARY KEY(id)
        )"""
        self.execute(query)
        self.commit()

    def add_users(self, type, description, price):
        rooms = len(self.get_rooms())
        code = f"RO-{rooms}"
        self.execute(
            """
            INSERT INTO `rooms` (
                code,
                type,
                description,
                status,
                price
            )
            VALUES (%s,%s,%s,%s,%s)
            """,
            (code, type, description, 0, price),
        )
        self.commit()

    def get_rooms(self):
        self.execute("SELECT * FROM `rooms`")
        result = self.cursor.fetchall()
        for room in self.cursor.fetchall().keys():
            result.append(room)
        return result

    def find_room(self, code):
        self.execute("SELECT * FROM `rooms` WHERE `code` = %s", (code))
        result = []
        for room in self.cursor.fetchall():
            result.append(room)
        return result

    def change_status(self, code, status):
        status = not status
        query = "UPDATE rooms SET status = %s WHERE code = %s"
        self.execute(query, (int(status), code))

    def delete(self, code):
        self.execute("DELETE FROM rooms WHERE code = %s", (code,))
        self.commit()

    def drop(self):
        self.execute("DROP TABLE `users`")
        self.commit()
