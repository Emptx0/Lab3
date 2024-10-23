from mushrooms import MushroomContext, MushroomFactory


class Forest:
    def __init__(self):
        self._mushrooms = []

    def load_mushrooms_list(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                line = line.split(" ")
                context = MushroomContext(line[0], int(line[1]), int(line[2]))
                mushroom = MushroomFactory.create_mushroom(context)
                self._mushrooms.append(mushroom)

    def get_mushrooms(self):
        return self._mushrooms
