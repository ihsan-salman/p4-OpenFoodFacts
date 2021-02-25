# Importation of the moduls
import mysql.connector

'''Class responsible for connections'''


class Connexion_mysql:

    def __init__(self):
        # Initialize the class
        self.ask_connexion_data()
        self.connexion()

    def ask_connexion_data(self):
        # Ask all the varaibles necessary for the connexion to the sql server
        self.user = input("votre nom d'utilisateur mysql : \n")
        self.password = input("votre mot de passe mysql : \n")
        self.database = input("votre nom de base de données mysql : \n")

    def connexion(self):
        # Make connexion to the sql server
        self.connexion = mysql.connector.connect(host='localhost',
                                                 user=self.user,
                                                 password=self.password,
                                                 database=self.database)
        # Method to communucate with the MySql database and ask requests
        self.cursor = self.connexion.cursor()