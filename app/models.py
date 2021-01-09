import os
import psycopg2


class DBManager:
    def __init__(self):
        self.connection = psycopg2.connect(dbname=os.environ.get('DATABASE'),
                                           user=os.environ.get('DB_USERNAME'),
                                           password=os.environ.get('DB_PASSWORD'),
                                           host='localhost')
        self.cursor = self.connection.cursor()

    def select(self, query: str, *args):
        self.cursor.execute(query, args)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        if exc_type is not None:
            return False
