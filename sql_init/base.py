'''Importation of the moduls'''
import os
import requests
from sql_init.connexion import Connexion
from sql_query.category import Category
from sql_query.product import Product
from sql_query.favorite import Favorite


class Init:
    """Class responsible for initilization the database"""

    def __init__(self, connexion, category, product, favorite):
        # Initialize the class
        # Recover the connexion to the slq server
        self.connexion = connexion
        # Recover the cursor fonction to use the sql requests
        self.cursor = self.connexion.cursor()
        self.category = category
        self.product = product
        self.favorite = favorite
        # List who contain the name of the categories and their url
        self.category_table = [('pizzas'),
                               ('boissons sucrées'),
                               ('glaces'),
                               ('biscuits'),
                               ('eaux')]
        # List who will contain the products data
        self.product_data = []
        # List who will contain all the products data
        self.product_categorie = []
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl?"
        # Instantiate the table creation method
        self.table_creation()
        self.get_category()
        self.insert_category()
        self.insert_product()

    def table_creation(self):
        '''Create the 3  needful table to the program'''
        # Creation of the category table
        self.category.create_category_table()
        # Creation of the products data table
        self.product.create_product_table()
        # Creation of the saved favorite products table
        self.favorite.create_favorite_table()

    def get_category(self):
        '''Make requests to the OpenfoodFacts API
           to get the data of each category'''
        # Run the category list
        for i in range(len(self.category_table)):
            self.payload = {"search_terms": self.category_table[i],
                            "json": 1,
                            "action": "process",
                            "lang": "fr",
                            "page_size": "100",
                            "page": "1"
                            }
            # Request to the API
            self.json_request = requests.get(self.url, params=self.payload,)
            # Export data as json data
            self.json_category = self.json_request.json()
            # Add all json data in a list to make easier the usage
            self.product_categorie.append(self.json_category)

    def insert_category(self):
        '''Input the categories name if the table is empty'''
        self.count = self.category.count_category()
        # Check if the category table is empty
        if self.count != len(self.category_table):
            for category in self.category_table:
                self.category.insert_category_name(category)

    def insert_product(self):
        '''Insert the product data if the table is empty'''
        self.category_id = self.category.get_id()
        self.count = self.product.count_product()
        # Check if the table's line number is different that 0
        if self.count != 500:
            # Run the category list
            for i in range(len(self.category_table)):
                # Run the json data of each product
                for product in self.product_categorie[i]['products']:
                    # Check if the wanted data are in the json data
                    #  And add all the data in the product list
                    self.product_data = [product.get('product_name'),
                                         product.get('brands'),
                                         product.get('nutriscore_grade'),
                                         product.get('url'),
                                         product.get('stores'),
                                         self.category_id[i][0]]
                    # Insert all the data of each product
                    # in the Product table
                    self.product.insert_product_data(self.product_data)


# if this modul is executed the following code is executed
if __name__ == "__main__":
    CONNEXION = Connexion(os.environ)
    CATEGORY = Category(CONNEXION.connexion_mysql)
    PRODUCT = Product(CONNEXION.connexion_mysql)
    FAVORITE = Favorite(CONNEXION.connexion_mysql)
    INIT = Init(CONNEXION.connexion_mysql, CATEGORY, PRODUCT, FAVORITE)
