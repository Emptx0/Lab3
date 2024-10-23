from forest import Forest, ForestRepository
from basket import Basket


class UI:
    def get_mushroom_from_user(self, forest: Forest, repo: ForestRepository):
        name = input("Enter mushroom name: ")
        eatable = input("Is mushroom eatable? (1/0): ")
        treatment = input("Enter heat treatment time for mushroom in minutes: ")
        repo.add_mushroom_to_forest(name, eatable, treatment, forest)

    def get_basket_from_user(self, basket: Basket, forest: Forest):
        mushroom_list = forest.get_mushrooms()
        print("\nEnter 'd' if done\nEnter mushrooms:\n")
        while True:
            name = input()
            if name == 'd':
                break
            else:
                counter = 0
                for mushroom in mushroom_list:
                    if name == mushroom.get_name():
                        basket.add_item(mushroom)
                        counter += 1
                        break
                if counter == 0:
                    print("Mushroom not found")
        basket.calculate_result()

    def show_mushrooms(self, forest: Forest):
        print("NAME  |  EATABLE  |  TREATMENT")
        for mushroom in forest.get_mushrooms():
            print(mushroom)

    def show_menu(self):
        print("\n1. Add mushroom")
        print("2. Show mushrooms in forest")
        print("3. Calculate eatable percent and treatment time")
        print("4. Exit")
