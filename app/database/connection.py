import pymysql
import pendulum
import traceback


class Database:
    connection = None

    def __init__(self):
        try:
            if not self.connection:
                self.connection = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="pbomyhotel",
                    cursorclass=pymysql.cursors.DictCursor,
                )
            pymysql.converters.conversions[
                pendulum.DateTime
            ] = pymysql.converters.escape_datetime
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
            traceback.print_tb(error.__traceback__)

    def execute_many(self, query, values=None):
        try:
            if values:
                self.cursor.executemany(query, values)
            else:
                self.cursor.executemany(query)
        except Exception as error:
            traceback.print_tb(error.__traceback__)

    def commit(self):
        self.connection.commit()
