import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error


class DatabaseConnection:
    def __init__(self):
        load_dotenv()

        self.user = os.getenv('DB_USER')
        self.host = os.getenv('DB_HOST')
        self.password = os.getenv('DB_PASSWORD')
        self.database = os.getenv('DB_NAME')

        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except Error as e:
            raise ConnectionError("Connexion à la base de données non établie.")

    def fetch_data(self, query, params=None):
        try:
            cursor = self.conn.cursor(dictionary=True)
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            rows = cursor.fetchall()

            return rows
        except Error as e:
            raise ConnectionError(f"Erreur lors de la récupération des données : {e}")