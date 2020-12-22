from app.Database.DBconnection import Database


class User(Database):
    def __init__(self, query=None, value=None):
        super.__init__(self, query, value)