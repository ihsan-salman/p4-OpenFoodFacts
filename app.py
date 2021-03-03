'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


class App:
    '''Class responsible of selecting product and substitute'''

    def __init__(self, connexion):
        self.connexion = connexion
        self.cursor = self.connexion.cursor()
        self.records = None
        self.request = None
        self.choice_category = None
        self.choice_product = None
        self.choice_substitute = None
        self.choice = None
        self.category_id_list = []
        self.sub_number = []
        self.product = []
        self.substitute = []

    def display_category(self):
        '''display the avalaible categories'''
        print("\nveuillez choisir une catégorie parmis les choix suivants")
        # get all from Category table
        self.cursor.execute("SELECT * FROM Category")
        # Recover query result to be used as a python variable
        self.records = self.cursor.fetchall()
        # Run the list and print the category name
        for record in self.records:
            print(record)
        self.choose_category()
        self.display_product()
        self.finding_substitute()

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
            # Sql request who get the category id
            self.cursor.execute('''SELECT id FROM Category''')
            # Recover query result to be used as a python variable
            self.records = self.cursor.fetchall()
            for i in range(len(self.records)):
                self.category_id_list.append(self.records[i][0])
            # Check if the  category choice is correct
            if int(self.choice_category) in self.category_id_list:
                # Sql request who get the needful data to choose a product
                self.request = '''
                SELECT id, product_name
                FROM Product
                WHERE category_id = %s'''
                # Execute the sql request
                self.cursor.execute(self.request,
                                    (int(self.choice_category), ))
                # Recover query result to be used as a python variable
                self.records = self.cursor.fetchall()
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
        # Run the data and display each wanted product data
        for record in self.records:
            print(record)
        print('\n---------------------------------------------------------'
              '\nVoici la liste de produit disponible dans cette catégorie')
        self.choose_product()

    def choose_product(self):
        '''Ask a number to the user corresponding to the selected product'''
        try:
            # Ask a number
            self.choice_product = input(
                "-------------------------------------------------------"
                "\nEntrez le chiffre correspondant à votre produit "
                ' ou 0 pour revenir au choix de la catégorie'
                "\nPuis pressez sur ENTER :\n")
            # Sql request who get all data of the selected product
            self.request = '''SELECT * FROM Product WHERE id = %s'''
            # Check if the number is in the right category of product
            if ((24 * (int(self.choice_category) - 1)) +
                    1) <= int(self.choice_product) <= (
                        24 * int(self.choice_category)):
                # Execute the sql request
                self.cursor.execute(self.request,
                                    (int(self.choice_product), ))
                # Recover query result to be used as a python variable
                self.records = self.cursor.fetchall()
                # Run the list
                for record in self.records:
                    # Add the product data to the corresponding list
                    self.product = record
                # Display the selected product name
                print('\n-----------------------------------------------------'
                      '\nVous avez choisi:', self.product[1])
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
        if self.product[3] == 'a':
            # Sql request who get the wanted data of the substitutes
            self.request = '''
            SELECT id, product_name, nutriscore_grade
            FROM Product where category_id = %s
            AND nutriscore_grade IS NOT NULL AND id != %s LIMIT 5'''
            self.display_substitute()
            # Instantiate the choose substitute method
            self.choose_substitute()
        # Same as before
        elif self.product[3] == 'b':
            self.request = '''
            SELECT id, product_name, nutriscore_grade
            FROM Product where category_id = %s
            AND nutriscore_grade IN ('b', 'a')
            AND nutriscore_grade IS NOT NULL AND id != %s LIMIT 5'''
            self.display_substitute()
            self.choose_substitute()
        elif self.product[3] == 'c':
            self.request = '''
            SELECT id, product_name, nutriscore_grade
            FROM Product where category_id = %s
            AND nutriscore_grade IN ('c', 'b', 'a')
            AND nutriscore_grade IS NOT NULL AND id != %s LIMIT 5'''
            self.display_substitute()
            self.choose_substitute()
        elif self.product[3] == 'd':
            self.request = '''
            SELECT id, product_name, nutriscore_grade
            FROM Product where category_id = %s
            AND nutriscore_grade IN ('c', 'b', 'a')
            AND nutriscore_grade IS NOT NULL AND id != %s LIMIT 5'''
            self.display_substitute()
            self.choose_substitute()
        elif self.product[3] == 'e':
            self.request = '''
            SELECT id, product_name, nutriscore_grade
            FROM Product where category_id = %s
            AND nutriscore_grade != 'e'
            AND nutriscore_grade IS NOT NULL AND id != %s LIMIT 5'''
            self.display_substitute()
            self.choose_substitute()
        # Return a message if there is no substitute for the selected product
        elif self.sub_number == []:
            print('il y a aucun substitut à votre produit\n')
            # Send to the product choice
            self.display_product()

    def display_substitute(self):
        '''Execute the sql request'''
        self.cursor.execute(self.request,
                            (int(self.choice_category),
                             int(self.choice_product), ))
        # Recover query result to be used as a python variable
        self.records = self.cursor.fetchall()
        # Run the list
        for record in self.records:
            # Add all the substitutes number
            self.sub_number.append(record[0])
            # Display the data of each find substitute
            print(record)

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
            # Sql request who get the data of the selected substitute product
            self.request = 'SELECT * FROM Product WHERE id = %s'
            # Check if the number is in the substitute number list
            if int(self.choice_substitute) in self.sub_number:
                # Execute the sql request
                self.cursor.execute(self.request,
                                    (int(self.choice_substitute), ))
                # Recover query result to be used as a python variable
                self.records = self.cursor.fetchall()
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
              '\n\nproduit choisis:', self.product[1],
              '\nsubstitut choisis:', self.substitute[1],
              '\ncomparatif des scores nutritionnels:',
              self.product[3], 'VS', self.substitute[3])
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
        # Sql request who insert the id of the product
        # and the substitute in the table
        self.request = '''
        INSERT IGNORE INTO favorite_product (
            selected_product_id,
            substitute_product_id)
        VALUES (%s, %s)'''
        # Execute the sql
        self.cursor.execute(self.request,
                            (self.product[0],
                             self.substitute[0], ))
        # Save the change of the database
        self.connexion.commit()
        # Display a message that the products are correctly saved
        print('\n--------------------------------------------------------'
              '\nVos produits ont éte enregistré!')
