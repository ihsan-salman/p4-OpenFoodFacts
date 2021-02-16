import requests
import pprint
url = 'https://world.openfoodfacts.org/category/pizzas.json'
json_request = requests.get(url)
json_product_category = json_request.json()


connexion = mysql.connector.connect(host="localhost",
                                    user="ihsan",
                                    password="ihsan",
                                    database="OpenFoodFacts")
cursor = connexion.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS FoodData (
    subtitute_product_name varchar(200) NOT NULL,
    nutriscore_grade char(1),
    url char(200) NOT NULL,
    stores varchar(100)
 )
 ;""")

"""cursor.execute("INSERT IGNORE INTO FoodData (subtitute_product_name, nutriscore_grade, url, stores, description) VALUES (%s, %s, %s, %s, %s)", value)

connexion.commit()
cursor.execute("SELECT * FROM FoodData")
records = cursor.fetchall()
for record in records:
    print(record)
    print('--------------------------------------------------------------')

connexion.close()"""

"""Data searching class"""


