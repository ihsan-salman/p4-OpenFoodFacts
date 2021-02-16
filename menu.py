# importation of moduls

"""Main menu's reponsable class"""


class Menu:

    def __init__(self, data):
        self.data = data
        self.display_menu()

    def display_menu(self):
        # Display the menu with all choice
        print('---------------------------------'
              '\nBienvenue dans OpenfoodFacts data'
              '\n---------------------------------')
        print("\n-----------------------------------------------"
              "\n1 - Quel aliment souhaitez-vous remplacer ? ")
        print("2 - Retrouver mes aliments substitués.")
        print("3 - Réinitialiser la base de données")
        print("4 - Quitter le programme."
              "\n-----------------------------------------------")
        self.get_choice()

    def get_choice(self):
        # Ask a number and send to the corresponding choice
        self.choice = input(
            "\nEntrez le chiffre correspondant à votre choix "
            "puis pressez sur ENTER :\n")
        if self.choice == "1":
            print("------------------------------------------------"
                  "\nVous voulez trouver un aliment de substitution !"
                  "\n------------------------------------------------")
            self.data.display_category()
        elif self.choice == "2":
            print("\nVous voulez voir vos alIments substitués !")
        elif self.choice == "3":
            print("\nVous voulez réinitialiser votre base de données !")
        elif self.choice == "4":
            print("A bientôt ! \nFermeture du programme...")
            exit()
        else:
            print("\nvotre réponse est incorrecte !"
                  " Veuillez entrer un chiffre valide !")
            self.display_menu()