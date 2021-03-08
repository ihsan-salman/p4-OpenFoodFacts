''' Importation of the moduls '''
import mysql.connector


class Connexion:
    '''Class responsible for connexion'''

    def __init__(self, environ):
        # Initialize the class
        self.environ = environ
        self.connexion()

    def connexion(self):
        '''Make connexion to the sql server'''
        self.connexion_mysql = mysql.connector.connect(
            host=self.environ["MYSQL_CONNEXION_TYPE"],
            user=self.environ["MYSQL_USERNAME"],
            password=self.environ["MYSQL_PASSWORD"],
            database=self.environ["MYSQL_DATABASE"])
