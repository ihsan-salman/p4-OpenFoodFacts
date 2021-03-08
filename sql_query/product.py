'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


class Product:
    '''Class responsible of product table sql requests'''

    def __init__(self, connexion):
        self.connexion = connexion
        self.cursor = self.connexion.cursor()
        self.request = None
        self.records = None
        self.prod_id = []

    def insert_product_data(self, product_data):
        '''Insert the product data into the product table'''
        self.product_data = product_data
        # Insert the name of the category in the table
        self.cursor.execute("""
                        INSERT IGNORE INTO Product (
                            product_name,
                            brands,
                            nutriscore_grade,
                            url,
                            stores,
                            category_id)
                        VALUES (%s, %s, %s, %s, %s, %s)""", self.product_data)
        # Save all the change in the mysql database
        self.connexion.commit()

    def count_product(self):
        '''Return the number of line in the product table'''
        # Sql request who give the line number of the table
        self.cursor.execute('''SELECT COUNT(*) FROM Product''')
        # Recover query result to be used as a python variable
        self.records = self.cursor.fetchall()
        return self.records[0][0]

    def create_product_table(self):
        '''Create the product table'''
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
        self.connexion.commit()

    def get_product_category(self, choice):
        '''Return the product in the selected category'''
        self.choice = choice
        # Sql request who get the needful data to choose a product
        self.request = '''
            SELECT id, product_name
            FROM Product
            WHERE category_id = %s
            LIMIT 30'''
        # Execute the sql request
        self.cursor.execute(self.request, (self.choice, ))
        # Recover query result to be used as a python variable
        self.records = self.cursor.fetchall()
        return self.records

    def get_product_data(self, choice):
        '''Return all data of the selected product'''
        self.choice = choice
        # Sql request who get all data of the selected product
        self.request = '''SELECT * FROM Product WHERE id = %s'''
        # Execute the sql request
        self.cursor.execute(self.request,
                            (self.choice, ))
        # Recover query result to be used as a python variable
        self.records = self.cursor.fetchall()
        return self.records

    def display_product(self, choice1, choice2, choice3):
        '''Display 5 product with a better nutriscore grade
           than the product'''
        self.choice1 = choice1
        self.choice2 = choice2
        self.choice3 = choice3
        self.request = '''
            SELECT id, product_name, nutriscore_grade
            FROM Product
            where category_id = %s
            AND product_name IS NOT NULL
            AND nutriscore_grade IN {}
            AND nutriscore_grade IS NOT NULL AND id != %s LIMIT 5'''.format(
                self.choice2)
        # Execute the sql request
        self.cursor.execute(self.request,
                            (self.choice1, self.choice3, ))
        # Recover query result to be used as a python variable
        self.records = self.cursor.fetchall()
        # Run the list
        for record in self.records:
            # Display the data of each find substitute
            print(record)

    def get_product_id(self, choice1, choice2, choice3):
        '''Return the id of the finding substitute product'''
        self.choice1 = choice1
        self.choice2 = choice2
        self.choice3 = choice3
        self.request = '''
            SELECT id, product_name, nutriscore_grade
            FROM Product
            where category_id = %s
            AND product_name IS NOT NULL
            AND nutriscore_grade IN {}
            AND nutriscore_grade IS NOT NULL AND id != %s LIMIT 5'''.format(
                self.choice2)
        # Execute the sql request
        self.cursor.execute(self.request,
                            (self.choice1, self.choice3, ))
        # Recover query result to be used as a python variable
        self.records = self.cursor.fetchall()
        # Run the list
        for record in self.records:
            # Display the data of each find substitute
            self.prod_id.append(record[0])
        return self.prod_id
