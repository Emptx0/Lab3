from forest import Forest, ForestRepository


def main():
    repository = ForestRepository('MushroomsList.txt')
    forest = Forest()
    repository.load_mushrooms_list(forest)


if __name__ == "__main__":
    main()
