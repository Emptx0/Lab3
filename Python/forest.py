from mushrooms import MushroomContext, MushroomFactory


class Forest:
    def __init__(self):
        self._mushrooms = []

    def get_mushrooms(self):
        return self._mushrooms


class ForestRepository:
    def __init__(self, filename):
        self._filename = filename

    def add_mushroom(self, name, eatable, treatment):
        with open(self._filename, 'a') as file:
            file.write(f"{name} {eatable} {treatment}\n")

    def load_mushrooms_list(self, forest):
        mushroom_list = forest.get_mushrooms()
        with open(self._filename, 'r') as file:
            for line in file:
                line = line.split(" ")
                context = MushroomContext(line[0], int(line[1]), int(line[2]))
                mushroom = MushroomFactory.create_mushroom(context)
                mushroom_list.append(mushroom)
