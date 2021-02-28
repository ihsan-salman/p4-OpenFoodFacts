# Importation of the moduls
import mysql.connector

'''Class responsible for connections'''


class Connexion_mysql:

    def __init__(self, environ):
        self.environ = environ
        # Initialize the class
        self.connexion()

    def connexion(self):
        # Make connexion to the sql server
        self.environ["MYSQL_USERNAME"] = "ihsan"
        self.environ["MYSQL_PASSWORD"] = "ihsan"
        self.environ["MYSQL_DATABASE"] = "OPF"
        self.connexion = mysql.connector.connect(
            host="localhost",
            user=self.environ["MYSQL_USERNAME"],
            password=self.environ["MYSQL_PASSWORD"],
            database=self.environ["MYSQL_DATABASE"])