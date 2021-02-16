# importation of moduls
import requests
from random import randint


class Data:

    def __init__(self):
        # Initialize the class
        self.i = 0
        self.selected_product = []
        self.product_list = []

    def display_category(self):
        #display the 5 categories avalaible
        print("\nveuillez choisir une catégorie parmis les choix suivants")
        print("1 - pizzas"
              "\n2 - boissons"
              "\n3 - glaces"
              "\n4 - biscuits"
              "\n5 - eaux"
              "\n")
        self.choose_category()

    def choose_category(self):
        #
        self.choice_category = input(
            "-------------------------------------------------------"
            "\nEntrez le chiffre correspondant à votre choix "
            "puis pressez sur ENTER :\n")
        if self.choice_category == "1":
            print("\n----------------------------------------"
                  "\nVous avez choisis la catégorie : pizzas"
                  "\n----------------------------------------")
        elif self.choice_category == "2":
            print("\n----------------------------------------"
                  "\nVous avez choisis la catégorie : boissons"
                  "\n----------------------------------------")
        elif self.choice_category == "3":
            print("\n----------------------------------------"
                  "\nVous avez choisis la catégorie : glaces"
                  "\n----------------------------------------")
        elif self.choice_category == "4":
            print("\n----------------------------------------"
                  "\nVous avez choisis la catégorie : biscuits"
                  "\n----------------------------------------")
        elif self.choice_category == "5":
            print("\n----------------------------------------"
                  "\nVous avez choisis la catégorie : eaux"
                  "\n----------------------------------------")
        else:
            print("\n\nVotre choix n'est pas valable!"
                  " Veuillez entrez un nombre valide"
                  "\n------------------------------------------------------")
            self.display_category()
        print('\n---------------------------------------------------------'
              '\nVoici la liste de produit disponible dans cette catégorie'
              '\n---------------------------------------------------------')
        self.display_product()
        self.choose_product()

    def choose_product(self):
        self.choice_product = input(
              "\n--------------------------------------------------"
              "\nEntrez le chiffre correspondant à votre choix de produit"
              " puis pressez sur ENTER:\n")
        self.choice_product = self.choice_product.split()
        self.selected_product_number = int(self.choice_product[0])
        if self.selected_product_number < self.i and self.selected_product_number >= 0:
            self.select_substitute_product()
            print('\n\nVous avez choisi :', 
                self.json_product_category['products']
                                          [self.selected_product_number]
                                          ['product_name'])
            for data in self.product_list[self.selected_product_number]:
                print(data)
            print(self.rand_numb)
        else:
            print("\nVotre choix n'est pas valable!"
                  " Veuillez entrez un nombre valide")
            self.i = 0
            self.display_product()
            self.choose_product()

    def display_product(self):
        self.product = []
        if self.choice_category == "1":
            self.json_request = requests.get(
                'https://world.openfoodfacts.org/category/pizzas.json')
        if self.choice_category == "2":
            self.json_request = requests.get(
                'https://world.openfoodfacts.org/category/beverages.json')
        if self.choice_category == "3":
             self.json_request = requests.get(
                'https://world.openfoodfacts.org/category/ice-creams.json')
        if self.choice_category == "4":
             self.json_request = requests.get(
                'https://world.openfoodfacts.org/category/biscuits.json')
        if self.choice_category == "5":
             self.json_request = requests.get(
                'https://world.openfoodfacts.org/category/waters.json')
        self.json_product_category = self.json_request.json()
        for product in self.json_product_category['products']:
            if 'nutriscore_grade' in product and product[
               'nutriscore_grade'] != '':
                nutriscore_grade = product['nutriscore_grade']
            else:
                nutriscore_grade = None

            if 'brands' in product and product['brands'] != '':
                brands = product['brands']
            else:
                brands = None

            if 'stores' in product and product['stores'] != '':
                stores = product['stores']
            else:
                stores = None

            self.product = [product['product_name'],
                            brands,
                            nutriscore_grade,
                            product['url'],
                            stores]
            self.product_list.append(self.product)
            print("")
            print("\n\n", self.i,"- nom du produit:", self.product[0])
            print("---------------------------------------------------------")
            self.i += 1

    def select_substitute_product(self):
        self.rand_numb = self.select_substitute_product
        self.substitute_product = []
        while self.rand_numb == self.selected_product_number:
            self.rand_numb = randint(0, 23)
            if self.rand_numb != self.selected_product_number:
                print(self.rand_numb)