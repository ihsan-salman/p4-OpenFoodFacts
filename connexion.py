import mysql.connector


class Connexion_mysql:

    def __init__(self):
        self.ask_connexion_data()
        self.connexion()

    def ask_connexion_data(self):
        self.user = input("votre nom d'utilisateur mysql : \n")
        self.password = input("votre mot de passe mysql : \n")
        self.database = input("votre nom de base de données mysql : \n")

    def connexion(self):
        self.connexion = mysql.connector.connect(host='localhost',
                                                 user=self.user,
                                                 password=self.password,
                                                 database=self.database)
        self.cursor = self.connexion.cursor()