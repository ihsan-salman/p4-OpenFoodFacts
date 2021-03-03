'''!/usr/bin/python3
   -*- coding: Utf-8 -'''

from os import environ
from menu import Menu
from fav import Favorite
from app import App
from connexion import Connexion
from init import Init


def main():
    '''main function instantiate all class'''
    # Instances of classes
    connexion = Connexion(environ)
    Init(connexion.connexion_mysql)
    favorite = Favorite(connexion.connexion_mysql)
    app = App(connexion.connexion_mysql)
    Menu(favorite, app)


if __name__ == "__main__":
    main()
