'''!/usr/bin/python3
   -*- coding: Utf-8 -'''

from os import environ
from menu import Menu
from fav import SavedProd
from app import App
from connexion import Connexion
from init import Init
from category import Category
from product import Product
from favorite import Favorite


def main():
    '''main function instantiate all class'''
    # Instances of classes
    connexion = Connexion(environ)
    category = Category(connexion.connexion_mysql)
    product = Product(connexion.connexion_mysql)
    favorite = Favorite(connexion.connexion_mysql)
    Init(connexion.connexion_mysql, category, product, favorite)
    savedprod = SavedProd(connexion.connexion_mysql, favorite)
    app = App(connexion.connexion_mysql, category, product, favorite)
    Menu(savedprod, app)


if __name__ == "__main__":
    main()
