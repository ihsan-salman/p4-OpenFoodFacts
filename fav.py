'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


class Favorite:
    """
    Class responsible of display favorite product or delete them
    """

    def __init__(self, connexion):
        # Recover the connexion to the slq server
        self.connexion = connexion
        # Recover the cursor fonction to use the sql requests
        self.cursor = self.connexion.cursor()
        self.records = []
        self.records_fav = []
        self.request = None

    def display_saved_prod(self):
        '''Display all the saved product'''
        # Execute the sql request who get all from favorite product's table
        self.cursor.execute('SELECT * FROM favorite_product')
        # Recover query result to be used as a python variable
        self.records = self.cursor.fetchall()
        # Check if there are saved product
        if self.records != []:
            # Run the list of all saved product
            for i in range(len(self.records)):
                print('------------------------------------------------------')
                # Run between the product and the substitute
                for k in range(2):
                    # Sql request who get the data of the product
                    # and the substitute
                    self.request = '''
                    SELECT product_name,
                    nutriscore_grade,
                    url,
                    stores
                    FROM Product
                    WHERE id = %s'''
                    # Execute the sql request
                    self.cursor.execute(self.request, (self.records[i][k], ))
                    # Recover query result to be used as a python variable
                    self.records_fav = self.cursor.fetchall()
                    # Run the list of the products
                    for value in self.records_fav:
                        # Check if it's the product or the substitute
                        if k == 0:
                            # Display the data of the product
                            print('\nnom du produit:', value[0],
                                  '\nscore nutritionnel:', value[1],
                                  '\nlien:', value[2],
                                  '\nMagasin:', value[3])
                        else:
                            print('\nnom du substitut:', value[0],
                                  '\nscore nutritionnel:', value[1],
                                  '\nlien:', value[2],
                                  '\nMagasin:', value[3])
                print('----------------------------------------------------\n')
            print('Voici vos aliments substitués!')
        # Return a message of there isn't saved product
        else:
            print('\nvous avez enregistrés aucune données')

    def delete_saved_prod(self):
        '''Delele the saved products'''
        # Sql request who delete all the saved product in the table
        self.request = '''
        DELETE FROM favorite_product'''
        # Execute the sql request
        self.cursor.execute(self.request)
        # Save the change of the database
        self.connexion.commit()
        # Return a message that the products are deleted
        print('\nTous vos produits enregistrés ont été supprimés')
