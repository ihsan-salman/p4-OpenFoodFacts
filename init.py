import requests


class Init_db:

    def __init__(self, cursor):
        self.cursor = cursor
        self.category_table = [
            ('pizzas',
             'https://world.openfoodfacts.org/category/pizzas.json'),
            ('boissons_sucrées',
             'https://world.openfoodfacts.org/category/sodas.json'),
            ('glaces',
             'https://world.openfoodfacts.org/category/ice-creams.json'),
            ('biscuits',
             'https://world.openfoodfacts.org/category/biscuits.json'),
            ('eaux',
             'https://world.openfoodfacts.org/category/waters.json')]
        self.product = []
        self.product_categorie = []
        self.table_creation()

    def table_creation(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Category(
            id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            name char(50) NOT NULL
        )
        ;""")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS FoodData (
            id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            product_name varchar(200) NOT NULL,
            brands varchar(200),
            nutriscore_grade char(1),
            url char(200) NOT NULL,
            stores varchar(100),
            category_id INT NOT NULL,
            CONSTRAINT fk_cat_id FOREIGN KEY (category_id)
            REFERENCES Category(id)
         )
         ;""")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorite_product(
            selected_product_id INT NOT NULL,
            substitute_product_id INT NOT NULL,
            CONSTRAINT fk_sel_prod_id FOREIGN KEY (selected_product_id)
            REFERENCES FoodData(id),
            CONSTRAINT fk_sub_prod_id FOREIGN KEY (substitute_product_id)
            REFERENCES FoodData(id)
        )
        ;""")
        self.requests()

    def requests(self):
        for i in range(5):
            self.json_request = requests.get(self.category_table[i][1])
            self.json_category = self.json_request.json()
            self.product_categorie.append(self.json_category)
        self.category_input()

    def category_input(self):
        for i in range(5):
            self.cursor.execute('''
                INSERT IGNORE INTO Category (name)
                VALUES (%s)''', (self.category_table[i][0], ))
        self.fooddata_input()

    def fooddata_input(self):
        for i in range(5):
            for product in self.product_categorie[i]['products']:
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
                                stores,
                                i + 1]
                self.cursor.execute("""
                INSERT IGNORE INTO FoodData (
                    product_name,
                    brands,
                    nutriscore_grade,
                    url,
                    stores,
                    category_id)
                VALUES (%s, %s, %s, %s, %s, %s)""", self.product)
        self.connexion.commit()