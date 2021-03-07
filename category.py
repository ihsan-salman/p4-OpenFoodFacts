'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


class Category:
    '''Class responsible of category table sql requests'''

    def __init__(self, connexion):
        self.connexion = connexion
        self.cursor = self.connexion.cursor()
        self.records = None

    def insert_category_name(self, name):
        '''insert category's name into the table'''
        self.name = name
        # Insert the name of the category in the table
        self.cursor.execute('''
            INSERT IGNORE INTO Category (name)
            VALUES (%s)''', (self.name, ))
        # Save all the change in the mysql database
        self.connexion.commit()

    def count_category(self):
        '''Return  the number of line in the category table'''
        # Sql request who give the line number of the table
        self.cursor.execute('''SELECT COUNT(*) FROM Category''')
        # Recover query result to be used as a python variable
        self.records = self.cursor.fetchall()
        return self.records[0][0]

    def display_category(self):
        '''Display all data from category table'''
        # get all from Category table
        self.cursor.execute("SELECT * FROM Category")
        # Recover query result to be used as a python variable
        self.records = self.cursor.fetchall()
        # Run the list and print the category name
        for record in self.records:
            print(record)

    def get_id(self):
        '''Return all category id'''
        # Sql request who get the Category id
        self.cursor.execute('''SELECT id FROM Category''')
        self.records = self.cursor.fetchall()
        return self.records

    def create_category_table(self):
        '''Create the  category table'''
        # Creation of the category table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Category(
            id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            name char(50) NOT NULL
        )
        ;""")
        self.connexion.commit()
