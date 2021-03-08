'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


class App:
    '''Class responsible of selecting product and substitute'''

    def __init__(self, connexion, category, product, favorite):
        self.connexion = connexion
        self.cursor = self.connexion.cursor()
        self.category = category
        self.product = product
        self.favorite = favorite
        self.records = None
        self.choice = None
        self.choice_category = None
        self.choice_product = None
        self.choice_substitute = None
        self.sub_number = []
        self.product_data = []
        self.substitute = []
        self.category_id_list = []

    def display_category(self):
        '''display the avalaible categories'''
        print("\nveuillez choisir une catégorie parmis les choix suivants")
        self.category.display_category()
        self.choose_category()

    def choose_category(self):
        '''Ask a number to the display after all products of the category'''
        self.category_id_list = []
        # send a message if the user enter another caracter than a number
        try:
            self.choice_category = input(
                "-------------------------------------------------------"
                "\nEntrez le chiffre correspondant à votre choix "
                "puis pressez sur ENTER :\n")
            print("\n----------------------------------------")
            self.records = self.category.get_id()
            for i in range(len(self.records)):
                self.category_id_list.append(self.records[i][0])
            # Check if the  category choice is correct
            if int(self.choice_category) in self.category_id_list:
                self.display_product()
            # Return a message if the choice isn't correct
            else:
                print("\n\nVotre choix n'est pas valable!"
                      " Veuillez entrez un nombre valide"
                      "\n----------------------------------------------------")
                # Instantiate the display category method to go back
                self.display_category()
        except ValueError:
            print('\nVous avez utilisez un autre caractère!\n')
            self.display_category()

    def display_product(self):
        '''display all product of the selected category'''
        self.records = self.product.get_product_category(
            int(self.choice_category))
        print('\n---------------------------------------------------------')
        # Run the data and display each wanted product data
        for record in self.records:
            print(record)
        print('\n---------------------------------------------------------'
              '\nVoici la liste de produit disponible dans cette catégorie')
        self.choose_product()

    def choose_product(self):
        '''Ask a number to the user corresponding to the selected product'''
        self.product_data = []
        try:
            # Ask a number
            self.choice_product = input(
                "-------------------------------------------------------"
                "\nEntrez le chiffre correspondant à votre produit "
                ' ou 0 pour revenir au choix de la catégorie'
                "\nPuis pressez sur ENTER :\n")
            # Check if the number is in the right category of product
            if ((100 * (int(self.choice_category) - 1)) +
                    1) <= int(self.choice_product) <= (
                        100 * int(self.choice_category)):
                self.records = self.product.get_product_data(
                    int(self.choice_product))
                # Run the list
                for record in self.records:
                    # Add the product data to the corresponding list
                    self.product_data = record
                # Display the selected product name
                print('\n-----------------------------------------------------'
                      '\nVous avez choisi:', self.product_data[1],
                      'avec un score nutritionnel de', self.product_data[3])
                self.finding_substitute()
            # if the choice is 0, go back to the before step
            elif self.choice_product == '0':
                self.display_category()
            # Return a message if the choice isn't correct
            else:
                print("\n\nVotre choix n'est pas valable!"
                      " Veuillez entrez un nombre valide"
                      "\n----------------------------------------------------")
                # Instantiate the display product method to go back
                self.display_product()
        except ValueError:
            print('\nVous avez utilisez un autre caractère!\n')
            self.display_product()

    def finding_substitute(self):
        '''Find all the substitute of the product from the nutriscore grade'''
        print('\n-----------------------------------------------------------')
        # Check if the nutriscore grade is equal to the corresponding letter
        if self.product_data[3] == 'a':
            self.product.display_product(int(self.choice_category),
                                         ('a'),
                                         int(self.choice_product))
            self.sub_number = self.product.get_product_id(
                int(self.choice_category),
                ('a'),
                int(self.choice_product))
            # Instantiate the choose substitute method
            self.choose_substitute()
        # Same as before
        elif self.product_data[3] == 'b':
            self.product.display_product(int(self.choice_category),
                                         ('b', 'a'),
                                         int(self.choice_product))
            self.sub_number = self.product.get_product_id(
                int(self.choice_category),
                ('b', 'a'),
                int(self.choice_product))
            self.choose_substitute()
        elif self.product_data[3] == 'c':
            self.product.display_product(int(self.choice_category),
                                         ('b', 'a'),
                                         int(self.choice_product))
            self.sub_number = self.product.get_product_id(
                int(self.choice_category),
                ('b', 'a'),
                int(self.choice_product))
            self.choose_substitute()
        elif self.product_data[3] == 'd':
            self.product.display_product(int(self.choice_category),
                                         ('c', 'b', 'a'),
                                         int(self.choice_product))
            self.sub_number = self.product.get_product_id(
                int(self.choice_category),
                ('c', 'b', 'a'),
                int(self.choice_product))
            self.choose_substitute()
        elif self.product_data[3] == 'e':
            self.product.display_product(int(self.choice_category),
                                         ('d', 'c', 'b', 'a'),
                                         int(self.choice_product))
            self.sub_number = self.product.get_product_id(
                int(self.choice_category),
                ('d', 'c', 'b', 'a'),
                int(self.choice_product))
            self.choose_substitute()
        # Return a message if there is no substitute for the selected product
        elif self.sub_number == []:
            print('il y a aucun substitut à votre produit\n')
            # Send to the product choice
            self.display_product()

    def choose_substitute(self):
        '''Ask a number to choose the substitute'''
        # list who will contain the data of the selected substitute product
        self.substitute = []
        try:
            # Ask a number
            self.choice_substitute = input(
                "-------------------------------------------------------"
                "\nEntrez le chiffre correspondant à votre substitut "
                'ou 0 pour revenir au choix de la catégorie'
                "\nPuis pressez sur ENTER :\n")
            # Check if the number is in the substitute number list
            if int(self.choice_substitute) in self.sub_number:
                # Recover query result to be used as a python variable
                self.records = self.product.get_product_data(
                    int(self.choice_substitute))
                # Run the list
                for record in self.records:
                    # Add data to the substitute product list
                    self.substitute = record
                # Display the substitute product name
                print('\n-----------------------------------------------------'
                      '\nVous avez choisi:', self.substitute[1])
                # Instantiate the display prod vs sub method
                self.display_prod_vs_sub()
            # if the choice is 0, send toto choose a product
            elif self.choice_substitute == '0':
                self.display_product()
            # Return a message if the choice isn't correct
            else:
                print("\n\nVotre choix n'est pas valable!"
                      " Veuillez entrez un nombre valide"
                      "\n----------------------------------------------------")
                # Send to the display substitute step
                self.finding_substitute()
        except ValueError:
            print('\nVous avez utilisez un autre caractère!\n')
            self.finding_substitute()

    def display_prod_vs_sub(self):
        '''Display a summary of the selected product and his substitute
           and give the to go back or save the products'''
        # Display th summary
        print('\n--------------------------------------------------'
              '\nvoici le récapitutaltif des choix précédents'
              '\n--------------------------------------------------'
              '\n\nproduit choisis:', self.product_data[1],
              '\nsubstitut choisis:', self.substitute[1],
              '\ncomparatif des scores nutritionnels:',
              self.product_data[3], 'VS', self.substitute[3])
        try:
            # Ask a number
            self.choice = input(
                '\n-----------------------------------------------------------'
                '\nEntrez 0 pour revenir arrière '
                '\nOu 1 pour enregister ces produits\n')
            # Send back if the choice is 0
            if self.choice == '0':
                self.finding_substitute()
            # Save the product in the favorite product's table if choice is 1
            elif self.choice == '1':
                self.save_prod_sub()
            # Return a message if the choice isn' correct
            else:
                print('Votre choix est incorrecte!'
                      'Veuillez entrez un choix valide')
                # Ask again a number
                self.display_prod_vs_sub()
        except ValueError:
            print('\nVous avez utilisez un autre caractère!\n')
            self.choose_substitute()

    def save_prod_sub(self):
        '''Save the product in the favorite product's table'''
        self.favorite.save_product(self.product_data[0], self.substitute[0])
        # Display a message that the products are correctly saved
        print('\n--------------------------------------------------------'
              '\nVos produits ont éte enregistré!')
