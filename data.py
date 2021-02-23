class Data:

    def __init__(self, cursor):
        self.cursor = cursor
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
        #
        self.choice_category = input(
            "-------------------------------------------------------"
            "\nEntrez le chiffre correspondant à votre choix "
            "puis pressez sur ENTER :\n")
        self.request = '''
        SELECT id, product_name
        FROM FoodData
        WHERE category_id = %s'''
        print("\n----------------------------------------")
        if 1 <= int(self.choice_category) <= 5:
            self.cursor.execute(self.request, (int(self.choice_category), ))
        else:
            print("\n\nVotre choix n'est pas valable!"
                  " Veuillez entrez un nombre valide"
                  "\n------------------------------------------------------")
            self.display_category()
        self.display_product()

    def display_product(self):
        self.records = self.cursor.fetchall()
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
        if ((24 * (int(self.choice_category) - 1)) + 1) <= int(self.choice_product) <= (24 * int(self.choice_category)):
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
            self.choose_product()
        self.finding_substitute()

    def finding_substitute(self):
        self.sub_number = []
        print('\n------------------------------------')
        if self.product[3] == 'a':
            self.request_substitute = '''
            SELECT id, product_name, nutriscore_grade
            FROM FoodData where category_id = %s
            AND nutriscore_grade IS NOT NULL
            AND stores IS NOT NULL
            AND id != %s LIMIT 5'''
            self.cursor.execute(self.request_substitute,
                                (int(self.choice_category),
                                 int(self.choice_product), ))
            self.records_product = self.cursor.fetchall()
            for record in self.records_product:
                self.sub_number.append(record[0])
                print(record)
        if self.product[3] == 'b':
            self.request_substitute = '''
            SELECT id, product_name, nutriscore_grade
            FROM FoodData where category_id = %s
            AND nutriscore_grade IN ('b', 'a')
            AND nutriscore_grade IS NOT NULL
            AND stores IS NOT NULL
            AND id != %s LIMIT 5'''
            self.cursor.execute(self.request_substitute,
                                (int(self.choice_category),
                                 int(self.choice_product), ))
            self.records_product = self.cursor.fetchall()
            for record in self.records_product:
                self.sub_number.append(record[0])
                print(record)
        if self.product[3] == 'c':
            self.request_substitute = '''
            SELECT id, product_name, nutriscore_grade
            FROM FoodData where category_id = %s
            AND nutriscore_grade IN ('c', 'b', 'a')
            AND nutriscore_grade IS NOT NULL
            AND stores IS NOT NULL
            AND id != %s LIMIT 5'''
            self.cursor.execute(self.request_substitute,
                                (int(self.choice_category),
                                 int(self.choice_product), ))
            self.records_product = self.cursor.fetchall()
            for record in self.records_product:
                self.sub_number.append(record[0])
                print(record)
        if self.product[3] == 'd':
            self.request_substitute = '''
            SELECT id, product_name, nutriscore_grade
            FROM FoodData where category_id = %s
            AND nutriscore_grade IN ('c', 'b', 'a')
            AND nutriscore_grade IS NOT NULL
            AND stores IS NOT NULL
            AND id != %s LIMIT 5'''
            self.cursor.execute(self.request_substitute,
                                (int(self.choice_category),
                                 int(self.choice_product), ))
            self.records_product = self.cursor.fetchall()
            for record in self.records_product:
                self.sub_number.append(record[0])
                print(record)
        if self.product[3] == 'e':
            self.request_substitute = '''
            SELECT id, product_name, nutriscore_grade
            FROM FoodData where category_id = %s
            AND nutriscore_grade != 'e'
            AND nutriscore_grade IS NOT NULL
            AND stores IS NOT NULL
            AND id != %s LIMIT 5'''
            self.cursor.execute(self.request_substitute,
                                (int(self.choice_category),
                                 int(self.choice_product), ))
            self.records_product = self.cursor.fetchall()
            for record in self.records_product:
                self.sub_number.append(record[0])
                print(record)
        self.choose_substitute()

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
        else:
            print("\n\nVotre choix n'est pas valable!"
                  " Veuillez entrez un nombre valide"
                  "\n------------------------------------------------------")
            self.finding_substitute()

     # def print_prod_vs_sub(self):
