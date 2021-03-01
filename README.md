# OpenFoodFacts 

You can find a substitute to your product by searching them in this program.  
All the data needful to your search are here !

#  Installation and requierement 

first of all, download [Python](https://www.python.org/) by going in the official website and choose the version you want ([Python download](https://www.python.org/downloads/)).

then, install [Pip](https://pypi.org/project/pip/) by entering in the terminal the following command line:
```bash
python3 -m pip --version
```
after that, you have the choice to download the zip of the code or clone with the following command Line:
```bash
git clone https://github.com/ihsan-salman/p5-OpenFoodFacts.git
```

finally, use the requirement document by entering the following command in the terminal:
```bash
pip3 install -r requirements.txt
```
Before starting the program, please be sure that you have your mysql username, password and the database name.  
You have two choice to connect your database:  
- using environment variable with the following tutorial  
First, install [virtualenv](https://pypi.org/project/virtualenv/) by entering the following code in the terminal:
```bash
sudo pip3 install virtualenv 
```
After that, create your virtual environment by entering the following code in the terminal:
```bash
virtualenv <name_of_your_environment>
```
then activate your virtual environment:
```bash
source <name_of_your_environment>/bin/activate
```
Finally, create the 3 environment variable by entering the following command in the terminal:
```bash
export MYSQL_CONNEXION_TYPE=<your_connexion_type> # "localhost" most of time
export MYSQL_USERNAME=<your_mysql_username>
export MYSQL_PASSWORD=<your_mysql_password>
export MYSQL_DATABASE=<your_mysql_database_name>
```
- edit the connexion.py modul by changing 3 information between line 17 and 20 like this:
```bash
host=<your_connexion_type> # "localhost" most of time
user=<your_mysql_username>,
password=<your_mysql_password>,
database=<your_mysql_database_name>)
```  
if you doesn't have any database in Mysql, create one with the following command in your Mysql terminal:
```bash
CREATE DATABASE <name_of_your database>;
```

# How to use the program

To start the program, enter the following command in the terminal:
```bash
python3 main.py
```

You can surf in the menu by entering numbers corresponding to the each choice given in the screen.  
Be sure to use just numbers to surf in program!
You have four choice in the main menu:  
- first for selecting a product, find a substitute and save them in your database  
- second for display all your saved products  
- third for deleting your saved products  
- four for quit the program