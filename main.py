# Importation of moduls
from menu import Menu
from data import Data
# from init import Init_db
from connexion import Connexion_mysql

# Instances of classes
connexion = Connexion_mysql()
# init = Init_db(connexion.cursor)
data = Data(connexion.cursor)
menu = Menu(data)