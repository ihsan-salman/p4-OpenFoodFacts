# Importation of the moduls
import requests
from connexion import Connexion_mysql
import os

''''''


class Init_db:

    def __init__(self, connexion):
        # Initialize the class
        # Recover the connexion to the slq server
        self.connexion = connexion
        # Recover the cursor fonction to use the sql requests
        self.cursor = self.connexion.cursor()
        # List who contain the name of the categories and their url
        self.category_table = [
            ('pizzas',
             'https://world.openfoodfacts.org/category/pizzas.json'),
            ('boissons_sucrées',
             'https://world.openfoodfacts.org/category/sodas.json'),
            ('glaces',
             'https://world.openfoodfacts.org/category/ice-creams.json'),
            ('biscuits',
             'https://world.openfoodfacts.org/category/biscuits.json'),
            ('eaux',
             'https://world.openfoodfacts.org/category/waters.json')]
        # List who will contain the products data
        self.product = []
        # List who will contain all the products data
        self.product_categorie = []
        # Instantiate the table creation method
        self.table_creation()
        self.get_category()
        self.insert_category()
        self.insert_product()

    def table_creation(self):
        # Create the 3  needful table to the program
        # Creation of the category table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Category(
            id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            name char(50) NOT NULL
        )
        ;""")
        # Creation of the products data table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Product (
            id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            product_name varchar(200) NOT NULL,
            brands varchar(200),
            nutriscore_grade char(1),
            url char(200) NOT NULL,
            stores varchar(100),
            category_id INT NOT NULL,
            CONSTRAINT fk_cat_id FOREIGN KEY (category_id)
            REFERENCES Category(id)
         )
         ;""")
        # Creation of the saved favorite products table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorite_product(
            selected_product_id INT NOT NULL,
            substitute_product_id INT NOT NULL,
            CONSTRAINT fk_sel_prod_id FOREIGN KEY (selected_product_id)
            REFERENCES Product(id),
            CONSTRAINT fk_sub_prod_id FOREIGN KEY (substitute_product_id)
            REFERENCES Product(id)
        )
        ;""")

    def get_category(self):
        # Make requests to the OpenfoodFacts API
        # to get the data of each category
        # Run the category list
        for i in range(len(self.category_table)):
            # Request to the API
            self.json_request = requests.get(self.category_table[i][1])
            # Export data as json data
            self.json_category = self.json_request.json()
            # Add all json data in a list to make easier the usage
            self.product_categorie.append(self.json_category)

    def insert_category(self):
        # Input the categories name if the table is empty
        # Sql request who set all foreign keys at OFF mode
        self.cursor.execute('''SET FOREIGN_KEY_CHECKS = 0''')
        # Sql request who delete all data
        # in a table with the id auto-incremented
        self.cursor.execute('''TRUNCATE TABLE Category''')
        # Sql request who give the line number of the table
        self.request = '''SELECT COUNT(*) FROM Category'''
        # Execute the sql request
        self.cursor.execute(self.request)
        # Recover query result to be used as a python variable
        self.record = self.cursor.fetchall()
        # Check if the category table is empty
        if self.record[0][0] != len(self.category_table):
            for i in range(len(self.category_table)):
                # Insert the name of the category in the table
                self.cursor.execute('''
                    INSERT IGNORE INTO Category (name)
                    VALUES (%s)''', (self.category_table[i][0], ))
            # Save all the change in the mysql database
            self.connexion.commit()

    def insert_product(self):
        # Input the fooddata if the table is empty
        self.cursor.execute('''TRUNCATE TABLE Product''')
        # Sql request who set all foreign keys at ON mode
        self.cursor.execute('''SET FOREIGN_KEY_CHECKS = 1''')
        # Sql request who get the Category id
        self.cursor.execute('''SELECT id FROM Category''')
        self.record = self.cursor.fetchall()
        self.category_id = self.record
        # Sql request who give the line number of the table
        self.cursor.execute('''SELECT COUNT(*) FROM Product''')
        self.record_product = self.cursor.fetchall()
        # Check if the table's line number is different that 0
        if self.record_product[0][0] != 120:
            # Run the category list
            for i in range(len(self.category_table)):
                # Run the json data of each product
                for product in self.product_categorie[i]['products']:
                    # Check if the wanted data are in the json data
                    if 'nutriscore_grade' in product and product[
                       'nutriscore_grade'] != '':
                        nutriscore_grade = product['nutriscore_grade']
                    # return None if it's not the case
                    else:
                        nutriscore_grade = None

                    if 'brands' in product and product['brands'] != '':
                        brands = product['brands']
                    else:
                        brands = None

                    if 'stores' in product and product['stores'] != '':
                        stores = product['stores']
                    else:
                        stores = None
                    # Add all the data in the product list
                    self.product = [product['product_name'],
                                    brands,
                                    nutriscore_grade,
                                    product['url'],
                                    stores,
                                    self.category_id[i][0]]
                    # Insert all the data of each product
                    # in the Product table
                    self.cursor.execute("""
                        INSERT IGNORE INTO Product (
                            product_name,
                            brands,
                            nutriscore_grade,
                            url,
                            stores,
                            category_id)
                        VALUES (%s, %s, %s, %s, %s, %s)""", self.product)
        # Save all the change in the mysql database
        self.connexion.commit()


# if main modul is executed the following code is executed
if __name__ == "__main__":
    connexion = Connexion_mysql(os.environ)
    init = Init_db(connexion.connexion)