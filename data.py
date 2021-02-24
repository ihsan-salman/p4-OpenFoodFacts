class Data:

    def __init__(self, connexion):
        self.connexion = connexion
        self.cursor = self.connexion.cursor()
        self.i = 0
        self.selected_product = []
        self.product_list = []

    def display_category(self):
        # display the 5 categories avalaible
        print("\nveuillez choisir une catégorie parmis les choix suivants")
        self.cursor.execute("SELECT * FROM Category")
        self.records = self.cursor.fetchall()
        for record in self.records:
            print(record)
        self.choose_category()

    def choose_category(self):
        self.choice_category = input(
            "-------------------------------------------------------"
            "\nEntrez le chiffre correspondant à votre choix "
            "puis pressez sur ENTER :\n")
        print("\n----------------------------------------")
        self.request = '''
        SELECT id, product_name
        FROM FoodData
        WHERE category_id = %s'''
        if 1 <= int(self.choice_category) <= 5:
            self.cursor.execute(self.request, (int(self.choice_category), ))
            self.records = self.cursor.fetchall()
        # elif self.choice_category == '0':
            # self.menu.display_menu()
        else:
            print("\n\nVotre choix n'est pas valable!"
                  " Veuillez entrez un nombre valide"
                  "\n------------------------------------------------------")
            self.display_category()
        self.display_product()

    def display_product(self):
        for record in self.records:
            print(record)
        print('\n---------------------------------------------------------'
              '\nVoici la liste de produit disponible dans cette catégorie')
        self.choose_product()

    def choose_product(self):
        self.product = []
        self.choice_product = input(
            "-------------------------------------------------------"
            "\nEntrez le chiffre correspondant à votre produit "
            "puis pressez sur ENTER :\n")
        self.request_product = 'SELECT * FROM FoodData WHERE id = %s'
        if ((24 * (int(self.choice_category) - 1)) +
            1) <= int(self.choice_product) <= (24 *
                                               int(self.choice_category)):
            self.cursor.execute(self.request_product,
                                (int(self.choice_product), ))
            self.records_product = self.cursor.fetchall()
            for record in self.records_product:
                self.product = record
            print('\n---------------------------------------------------------'
                  '\nVous avez choisi:', self.product[1])
        elif self.choice_product == '0':
            self.display_category()
        else:
            print("\n\nVotre choix n'est pas valable!"
                  " Veuillez entrez un nombre valide"
                  "\n------------------------------------------------------")
            self.display_product()
        self.finding_substitute()

    def finding_substitute(self):
        self.sub_number = []
        print('\n-----------------------------------------------------------')
        if self.product[3] == 'a':
            self.request_substitute = '''
            SELECT id, product_name, nutriscore_grade
            FROM FoodData where category_id = %s
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
        elif self.sub_number == []:
            print('il y a aucun substitut à votre produit\n')
            self.display_product()

    def choose_substitute(self):
        self.substitute = []
        self.choice_substitute = input(
            "-------------------------------------------------------"
            "\nEntrez le chiffre correspondant à votre substitut "
            "puis pressez sur ENTER :\n")
        self.request_product = 'SELECT * FROM FoodData WHERE id = %s'
        if int(self.choice_substitute) in self.sub_number:
            self.cursor.execute(self.request_product,
                                (int(self.choice_substitute), ))
            self.records_subtitute = self.cursor.fetchall()
            for record in self.records_subtitute:
                self.substitute = record
            print('\n---------------------------------------------------------'
                  '\nVous avez choisi:', self.substitute[1])
            self.display_prod_vs_sub()
        elif self.choice_substitute == '0':
            self.display_product()
        else:
            print("\n\nVotre choix n'est pas valable!"
                  " Veuillez entrez un nombre valide"
                  "\n------------------------------------------------------")
            self.finding_substitute()

    def display_prod_vs_sub(self):
        print('\n--------------------------------------------------'
              '\nvoici le récapitutaltif des choix précédents'
              '\n--------------------------------------------------'
              '\n\nproduit choisis:', self.product[1],
              '\nsubstitut choisis:', self.substitute[1],
              '\ncomparatif des scores nutritionnels:',
              self.product[3], 'VS', self.substitute[3])
        self.choice = input(
            '\n-----------------------------------------------------------'
            '\n0 pour revenir arrière '
            'et 1 pour enregister ces produits dans votre base de données\n')
        if self.choice == '0':
            self.finding_substitute()
        elif self.choice == '1':
            self.save_prod_sub()
        else:
            print('Votre choix est incorrecte!'
                  'Veuillez entrez un choix valide')
            self.display_prod_vs_sub()

    def save_prod_sub(self):
        self.request = '''
        INSERT IGNORE INTO favorite_product (
            selected_product_id,
            substitute_product_id)
        VALUES (%s, %s)'''
        self.cursor.execute(self.request,
                            (self.product[0],
                             self.substitute[0], ))
        self.connexion.commit()
        print('\nVos produits ont éte enregistré!'
              'Vous pouvez voir tous vos produits '
              'enregistrés')

    def display_saved_prod(self):
        self.request = '''
        SELECT * FROM favorite_product'''
        self.cursor.execute(self.request)
        self.records = self.cursor.fetchall()
        if self.records != []:
            for i in range(len(self.records)):
                print('------------------------------------------------------')
                for k in range(2):
                    self.request = '''
                    SELECT product_name,
                    nutriscore_grade,
                    url,
                    stores
                    FROM FoodData
                    WHERE id = %s'''
                    self.cursor.execute(self.request, (self.records[i][k], ))
                    self.records_fav = self.cursor.fetchall()
                    for value in self.records_fav:
                        if k == 0:
                            print('\nnom du produit:', value[0],
                                  '\nscore nutritionnel:', value[1],
                                  '\nlien:', value[2],
                                  '\nMagasin:', value[3])
                        else :
                            print('\nnom du substitut:', value[0],
                                  '\nscore nutritionnel:', value[1],
                                  '\nlien:', value[2],
                                  '\nMagasin:', value[3])
                print('----------------------------------------------------\n')
            print('Voici vos aliments substitués!')
        else:
            print('\nvous avez enregistrés aucune données')

    def delete_saved_prod(self):
        self.request = '''
        DELETE FROM favorite_product'''
        self.cursor.execute(self.request)
        self.connexion.commit()
        print('Tous vos produits enregistrés ont été supprimés')

    def delete_table(self):
        self.request = '''SELECT COUNT(*) FROM FoodData'''
        self.cursor.execute(self.request)
        self.record = self.cursor.fetchall()
        print(self.record[0][0])
        self.connexion.commit()