class Data:

    def __init__(self, connexion):
        # Initialize the class
        # Recover the connexion to the slq serve
        self.connexion = connexion
        # Recover the cursor fonction to use the sql requests
        self.cursor = self.connexion.cursor()

    def display_category(self):
        # display the avalaible categories
        print("\nveuillez choisir une catégorie parmis les choix suivants")
        # get all from Category table
        self.cursor.execute("SELECT * FROM Category")
        # Recover query result to be used as a python variable
        self.records = self.cursor.fetchall()
        # Run the list and print the category name
        for record in self.records:
            print(record)
        # Instantiate the choose category method
        self.choose_category()

    def choose_category(self):
        # Ask a number to the display after all products of the category
        self.choice_category = input(
            "-------------------------------------------------------"
            "\nEntrez le chiffre correspondant à votre choix "
            "puis pressez sur ENTER :\n")
        print("\n----------------------------------------")
        # Sql request who get the needful data to choose after a product
        self.request = '''
        SELECT id, product_name
        FROM FoodData
        WHERE category_id = %s'''
        # Check if the  category choice is correct
        if 1 <= int(self.choice_category) <= 5:
            # Execute the sql request
            self.cursor.execute(self.request, (int(self.choice_category), ))
            # Recover query result to be used as a python variable
            self.records = self.cursor.fetchall()
        # Return a message if the choice isn't correct
        else:
            print("\n\nVotre choix n'est pas valable!"
                  " Veuillez entrez un nombre valide"
                  "\n------------------------------------------------------")
            # Instantiate the display category method to go back
            self.display_category()
        # Instantiate the display product method
        self.display_product()

    def display_product(self):
        # display all product of the selected category
        # Run the data and display each wanted product data
        for record in self.records:
            print(record)
        print('\n---------------------------------------------------------'
              '\nVoici la liste de produit disponible dans cette catégorie')
        # Instantiate the choose product method
        self.choose_product()

    def choose_product(self):
        # Ask a number to the user corresponding to the selected product
        # List who will contain the needful data of the selected product
        self.product = []
        # Ask a number
        self.choice_product = input(
            "-------------------------------------------------------"
            "\nEntrez le chiffre correspondant à votre produit "
            ' ou 0 pour revenir au choix de la catégorie'
            "\nPuis pressez sur ENTER :\n")
        # Sql request who get all data of the selected product
        self.request_product = '''SELECT * FROM FoodData WHERE id = %s'''
        # Check if the number is in the right category of product
        if ((24 * (int(self.choice_category) - 1)) +
            1) <= int(self.choice_product) <= (24 *
                                               int(self.choice_category)):
            # Execute the sql request
            self.cursor.execute(self.request_product,
                                (int(self.choice_product), ))
            # Recover query result to be used as a python variable
            self.records_product = self.cursor.fetchall()
            # Run the list
            for record in self.records_product:
                # Add the product data to the corresponding list
                self.product = record
            # Display the selected product name
            print('\n---------------------------------------------------------'
                  '\nVous avez choisi:', self.product[1])
        # if the choice is 0, go back to the before step
        elif self.choice_product == '0':
            self.display_category()
        # Return a message if the choice isn't correct
        else:
            print("\n\nVotre choix n'est pas valable!"
                  " Veuillez entrez un nombre valide"
                  "\n------------------------------------------------------")
            # Instantiate the display product method to go back
            self.display_product()
        # Instantiate the finding substitute method
        self.finding_substitute()

    def finding_substitute(self):
        # Find all the substitute of the product from the nutriscore grade
        # List who will contain all the number of the substitute
        self.sub_number = []
        print('\n-----------------------------------------------------------')
        # Check if the nutriscore grade is equal to the corresponding letter
        if self.product[3] == 'a':
            # Sql request who get the wanted data of the substitutes
            self.request_substitute = '''
            SELECT id, product_name, nutriscore_grade
            FROM FoodData where category_id = %s
            AND nutriscore_grade IS NOT NULL
            AND id != %s LIMIT 5'''
            # Execute the sql request
            self.cursor.execute(self.request_substitute,
                                (int(self.choice_category),
                                 int(self.choice_product), ))
            # Recover query result to be used as a python variable
            self.records_product = self.cursor.fetchall()
            # Run the list
            for record in self.records_product:
                # Add all the substitutes number
                self.sub_number.append(record[0])
                # Display the data of each find substitute
                print(record)
            # Instantiate the choose substitute method
            self.choose_substitute()
        # Same as before
        elif self.product[3] == 'b':
            self.request_substitute = '''
            SELECT id, product_name, nutriscore_grade
            FROM FoodData where category_id = %s
            AND nutriscore_grade IN ('b', 'a')
            AND nutriscore_grade IS NOT NULL
            AND id != %s LIMIT 5'''
            self.cursor.execute(self.request_substitute,
                                (int(self.choice_category),
                                 int(self.choice_product), ))
            self.records_product = self.cursor.fetchall()
            for record in self.records_product:
                self.sub_number.append(record[0])
                print(record)
            self.choose_substitute()
        elif self.product[3] == 'c':
            self.request_substitute = '''
            SELECT id, product_name, nutriscore_grade
            FROM FoodData where category_id = %s
            AND nutriscore_grade IN ('c', 'b', 'a')
            AND nutriscore_grade IS NOT NULL
            AND id != %s LIMIT 5'''
            self.cursor.execute(self.request_substitute,
                                (int(self.choice_category),
                                 int(self.choice_product), ))
            self.records_product = self.cursor.fetchall()
            for record in self.records_product:
                self.sub_number.append(record[0])
                print(record)
            self.choose_substitute()
        elif self.product[3] == 'd':
            self.request_substitute = '''
            SELECT id, product_name, nutriscore_grade
            FROM FoodData where category_id = %s
            AND nutriscore_grade IN ('c', 'b', 'a')
            AND nutriscore_grade IS NOT NULL
            AND id != %s LIMIT 5'''
            self.cursor.execute(self.request_substitute,
                                (int(self.choice_category),
                                 int(self.choice_product), ))
            self.records_product = self.cursor.fetchall()
            for record in self.records_product:
                self.sub_number.append(record[0])
                print(record)
            self.choose_substitute()
        elif self.product[3] == 'e':
            self.request_substitute = '''
            SELECT id, product_name, nutriscore_grade
            FROM FoodData where category_id = %s
            AND nutriscore_grade != 'e'
            AND nutriscore_grade IS NOT NULL
            AND id != %s LIMIT 5'''
            self.cursor.execute(self.request_substitute,
                                (int(self.choice_category),
                                 int(self.choice_product), ))
            self.records_product = self.cursor.fetchall()
            for record in self.records_product:
                self.sub_number.append(record[0])
                print(record)
            self.choose_substitute()
        # Return a message if there is no substitute for the selected product
        elif self.sub_number == []:
            print('il y a aucun substitut à votre produit\n')
            # Send to the product choice
            self.display_product()

    def choose_substitute(self):
        # Ask a number to choose the substitute
        # list who will contain the data of the selected substitute product
        self.substitute = []
        # Ask a number
        self.choice_substitute = input(
            "-------------------------------------------------------"
            "\nEntrez le chiffre correspondant à votre substitut "
            'ou 0 pour revenir au choix de la catégorie'
            "\nPuis pressez sur ENTER :\n")
        # Sql request who get the data of the selected substitute product
        self.request_product = 'SELECT * FROM FoodData WHERE id = %s'
        # Check if the number is in the substitute number list
        if int(self.choice_substitute) in self.sub_number:
            # Execute the sql request
            self.cursor.execute(self.request_product,
                                (int(self.choice_substitute), ))
            # Recover query result to be used as a python variable
            self.records_subtitute = self.cursor.fetchall()
            # Run the list
            for record in self.records_subtitute:
                # Add data to the substitute product list
                self.substitute = record
            # Display the substitute product name
            print('\n---------------------------------------------------------'
                  '\nVous avez choisi:', self.substitute[1])
            # Instantiate the display prod vs sub method
            self.display_prod_vs_sub()
        # if the choice is 0, send to the before step to the choose a product
        elif self.choice_substitute == '0':
            self.display_product()
        # Return a message if the choice isn't correct
        else:
            print("\n\nVotre choix n'est pas valable!"
                  " Veuillez entrez un nombre valide"
                  "\n------------------------------------------------------")
            # Send to the display substitute step
            self.finding_substitute()

    def display_prod_vs_sub(self):
        # Display a summary of the selected product and his substitute
        # and give the to go back or save the products
        # Display th summary
        print('\n--------------------------------------------------'
              '\nvoici le récapitutaltif des choix précédents'
              '\n--------------------------------------------------'
              '\n\nproduit choisis:', self.product[1],
              '\nsubstitut choisis:', self.substitute[1],
              '\ncomparatif des scores nutritionnels:',
              self.product[3], 'VS', self.substitute[3])
        # Ask a number
        self.choice = input(
            '\n-----------------------------------------------------------'
            '\nEntrez 0 pour revenir arrière '
            '\nOu 1 pour enregister ces produits dans votre base de données\n')
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

    def save_prod_sub(self):
        # Save the product in the favorite product's table
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

    def display_saved_prod(self):
        # Display all the saved product
        # Sql request who get all from favorite product's table
        self.request = '''
        SELECT * FROM favorite_product'''
        # Execute the sql request
        self.cursor.execute(self.request)
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
                    FROM FoodData
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
        # Delele the saved products
        # Sql request who delete all the saved product in the table
        self.request = '''
        DELETE FROM favorite_product'''
        # Execute the sql request
        self.cursor.execute(self.request)
        # Save the change of the database
        self.connexion.commit()
        # Return a message that the products are deleted
        print('\nTous vos produits enregistrés ont été supprimés')