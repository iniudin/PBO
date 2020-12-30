from app.database.connection import Database
from app.functions import encode_md5
import pendulum


class UserModel(Database):
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS `users` (
            `id` INT AUTO_INCREMENT,
            `first_name` VARCHAR(20) NOT NULL,
            `last_name` VARCHAR(20) NOT NULL,
            `email` VARCHAR(30) UNIQUE NOT NULL,
            `username` VARCHAR(20) UNIQUE NOT NULL,
            `password` VARCHAR(32) NOT NULL,
            `phone` VARCHAR(15) NOT NULL,
            `address` VARCHAR(50) NOT NULL,
            `gender` ENUM('L', 'P') NOT NULL,
            `is_admin` TINYINT(1) NOT NULL,
            `register_date` DATETIME DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY(id)
        )
        """

        self.execute(query)
        self.commit()

    def login_session(self, username, password):
        self.execute(
            """
            SELECT id, username, is_admin
            FROM users
            WHERE username=%s AND password=%s""",
            (username, encode_md5(password)),
        )
        result = self.cursor.fetchone()
        return result

    def add_user(
        self,
        first_name,
        last_name,
        username,
        password,
        email,
        phone,
        address,
        gender,
        is_admin,
    ):
        timeNow = pendulum.now("Asia/Jakarta")
        self.execute(
            """INSERT INTO `users`(
                first_name,
                last_name,
                username,
                password,
                email,
                phone,
                address,
                gender,
                is_admin,
                register_date
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                first_name,
                last_name,
                username,
                encode_md5(password),
                email,
                phone,
                address,
                gender,
                is_admin,
                timeNow,
            ),
        )
        self.commit()

    def get_admins(self):
        self.execute(
            """
        SELECT
            CONCAT(first_name, ' ', last_name) AS 'fullname',
            username,
            is_admin,
            register_date
        FROM
            `users`
        WHERE
            `is_admin` >= 0
        """
        )
        result = []
        for user in self.cursor.fetchall():
            result.append(
                (
                    user["fullname"],
                    user["username"],
                    "Owner" if user["is_admin"] == 2 else "Admin",
                    user["register_date"],
                )
            )
        return result

    def get_customers(self):
        self.execute(
            """
        SELECT
            CONCAT(first_name, ' ', last_name) AS 'fullname',
            username,
            email,
            phone,
            address,
            gender,
            is_admin,
            register_date
        FROM
            `users`
        WHERE
            `is_admin` = 0
        """
        )
        result = self.cursor.fetchall()
        return result

    def find_user(self, username):
        self.execute(
            """
        SELECT
            CONCAT(first_name, ' ', last_name) AS 'fullname',
            username,
            is_admin,
            register_date
        FROM
            `users`
        WHERE
            `username` = %s
        """,
            (username),
        )
        result = []
        for user in self.cursor.fetchall():
            result.append(
                (
                    user["fullname"],
                    user["username"],
                    "Admin" if user["is_admin"] > 0 else "Customers",
                    user["register_date"],
                )
            )
        return result

    def update_users(
        self,
        first_name,
        last_name,
        username,
        password,
        email,
        phone,
        address,
        gender,
        user_id,
    ):
        self.execute(
            """
        UPDATE users
        SET first_name = %s,
            last_name = %s,
            username = %s,
            password = %s,
            email = %s,
            phone = %s,
            address = %s,
            gender = %s
        WHERE id = %s
        """,
            (
                first_name,
                last_name,
                username,
                password,
                email,
                phone,
                address,
                gender,
                user_id,
            ),
        )

    def delete(self, username):
        self.execute("DELETE FROM `users` WHERE `username` = %s", (username,))
        self.commit()

    def drop(self):
        self.execute("DROP TABLE `users`")
        self.commit()
