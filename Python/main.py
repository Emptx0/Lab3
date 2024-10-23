from forest import Forest, ForestRepository
from ui import UI
from basket import Basket


def main():
    repository = ForestRepository('MushroomsList.txt')
    ui = UI()
    forest = Forest()
    repository.load_mushrooms_list(forest)
    basket = Basket()

    while True:
        ui.show_menu()
        choice = input()
        if choice == '1':
            ui.get_mushroom_from_user(forest, repository)
        elif choice == '2':
            ui.show_mushrooms(forest)
        elif choice == '3':
            ui.get_basket_from_user(basket, forest)
        elif choice == '4':
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
