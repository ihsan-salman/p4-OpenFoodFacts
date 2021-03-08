'''!/usr/bin/python3
   -*- coding: Utf-8 -'''

from os import environ
from app.menu import Menu
from app.fav import SavedProd
from app.app import App
from sql_init.connexion import Connexion
from sql_init.base import Init
from sql_query.category import Category
from sql_query.product import Product
from sql_query.favorite import Favorite


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
