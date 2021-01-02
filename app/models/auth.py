from app.models.users import UserModel
from app.functions import encode_md5


class Auth(UserModel):
    def login_session(self, username, password):
        self.execute(
            """
            SELECT id, username, is_admin
            FROM users
            WHERE username=%s AND password=%s""",
            (username, encode_md5(password)),
        )
        session = self.cursor.fetchone()
        return session
