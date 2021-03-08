'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


class Favorite:
    '''Class responsible of favorite table sql requests'''

    def __init__(self, connexion):
        self.connexion = connexion
        self.cursor = self.connexion.cursor()
        self.records = None
        self.request = None

    def create_favorite_table(self):
        '''Create the favorite product table'''
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
        # Save all the change in the mysql database
        self.connexion.commit()

    def get_all(self):
        '''Get all data from the favorite table'''
        # Execute the sql request who get all from favorite product's table
        self.cursor.execute('SELECT * FROM favorite_product')
        # Recover query result to be used as a python variable
        self.records = self.cursor.fetchall()
        return self.records

    def get_favorite_product_data(self, data):
        '''Get the product data of the favorite product'''
        self.data = data
        self.request = '''
            SELECT product_name,
                   nutriscore_grade,
                   url,
                   stores
            FROM Product
            WHERE id = %s'''
        # Execute the sql request
        self.cursor.execute(self.request, (self.data, ))
        # Recover query result to be used as a python variable
        self.records = self.cursor.fetchall()
        return self.records

    def delete_favorite_product(self):
        '''Delete all data from favorite table'''
        # Sql request who delete all the saved product in the table
        self.request = '''
        DELETE FROM favorite_product'''
        # Execute the sql request
        self.cursor.execute(self.request)
        # Save the change of the database
        self.connexion.commit()

    def save_product(self, product, substitute):
        '''Save the selected products id in favorite table'''
        self.product = product
        self.substitute = substitute
        # Sql request who insert the id of the product
        # and the substitute in the table
        self.request = '''
        INSERT IGNORE INTO favorite_product (
            selected_product_id,
            substitute_product_id)
        VALUES (%s, %s)'''
        # Execute the sql
        self.cursor.execute(self.request,
                            (self.product,
                             self.substitute, ))
        # Save the change of the database
        self.connexion.commit()
