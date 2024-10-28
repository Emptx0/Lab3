from mushrooms import MushroomContext, MushroomFactory


class Forest:
    def __init__(self):
        self._mushrooms = []

    def get_mushrooms(self):
        return self._mushrooms

    def set_mushrooms(self, mushrooms):
        self._mushrooms = mushrooms


class ForestRepository:
    def __init__(self, filename):
        self._filename = filename

    def add_mushroom_to_forest(self, name, eatable, treatment, forest: Forest):
        with open(self._filename, 'a') as file:
            file.write(f"\n{name} {eatable} {treatment}")
        self.load_mushrooms_list(forest)

    def load_mushrooms_list(self, forest):
        forest.set_mushrooms([])
        mushroom_list = []
        with open(self._filename, 'r') as file:
            for line in file:
                line = line.split(" ")
                context = MushroomContext(line[0], int(line[1]), int(line[2]))
                mushroom = MushroomFactory.create_mushroom(context)
                mushroom_list.append(mushroom)
        forest.set_mushrooms(mushroom_list)
