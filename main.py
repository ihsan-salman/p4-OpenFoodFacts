#!/usr/bin/python3
# -*- coding: Utf-8 -*

# Importation of moduls
from menu import Menu
from fav import Favorite
from app import App
from connexion import Connexion_mysql
from init import Init_db
from os import environ

# Instances of classes
connexion = Connexion_mysql(environ)
Init_db(connexion.connexion)
favorite = Favorite(connexion.connexion)
app = App(connexion.connexion)
menu = Menu(favorite, app)
