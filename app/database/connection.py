from pymysql import connect, cursors
import time


class Database:
    connection = None

    def __init__(self):
        try:
            if not self.connection:
                self.connection = connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="pbomyhotel",
                    cursorclass=cursors.DictCursor,
                )
            self.cursor = self.connection.cursor()
        except Exception as error:
            print(error)

    def execute(self, query, value=None):
        try:
            if value:
                self.cursor.execute(query, value)
            else:
                self.cursor.execute(query)
        except Exception as error:
            print(error)


    def execute_many(self, query, values=None):
        try:
            if value:
                self.cursor.executemany(query, value)
            else:
                self.cursor.executemany(query)
        except Exception as error:
            print(error)

    def commit(self):
        self.connection.commit()