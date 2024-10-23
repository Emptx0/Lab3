from forest import Forest


def main():
    forest = Forest()
    forest.load_mushrooms_list('MushroomsList.txt')

    mushrooms = forest.get_mushrooms()

if __name__ == "__main__":
    main()
