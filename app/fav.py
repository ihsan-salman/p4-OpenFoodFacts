'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


class SavedProd:
    """
    Class responsible of display favorite product or delete them
    """

    def __init__(self, connexion, favorite):
        # Recover the connexion to the slq server
        self.connexion = connexion
        # Recover the cursor fonction to use the sql requests
        self.cursor = self.connexion.cursor()
        self.favorite = favorite
        self.record = None
        self.records = None

    def display_saved_prod(self):
        '''Display all the saved product'''
        self.records = self.favorite.get_all()
        # Check if there are saved product
        if self.records != []:
            # Run the list of all saved product
            for i in range(len(self.records)):
                print('------------------------------------------------------')
                # Run between the product and the substitute
                for k in range(2):
                    self.record = self.favorite.get_favorite_product_data(
                        self.records[i][k])
                    # Run the list of the products
                    for value in self.record:
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
        self.favorite.delete_favorite_product()
        # Return a message that the products are deleted
        print('\nTous vos produits enregistrés ont été supprimés')
