#include "ui.h"

void UI::getMushroomFromUser(Forest& forest, ForestRepository& repo) {
	system("cls");
	std::string name;
	bool eatable;
	int treatment;

	std::cout << "Enter mushroom name: ";
	std::cin >> name;
	std::cout << "Is mushroom eatable? (1/0): ";
	std::cin >> eatable;
	std::cout << "Enter heat treatment time for mushroom in minutes: ";
	std::cin >> treatment;

	repo.addMushroomToForest(name, eatable, treatment, forest);
}

void UI::getBasketFromUser(Basket& basket, Forest& forest) {
	system("cls");
	std::vector<Mushroom*> mushroomList = forest.getMushrooms();
	std::cout << "Enter 'd' if done" << std::endl << "Enter mushroom:" << std::endl;

	while (true) {
		std::string name;
		std::cin >> name;
		if (name == "d") {
			break;
		}
		else {
			int counter = 0;
			for (auto mushroom : mushroomList) {
				if (name == mushroom->getName()) {
					basket.addItem(mushroom);
					counter++;
					break;
				}
			}
			if (counter == 0) {
				std::cout << "Mushroom not found" << std::endl;
			}
		}
	}
	basket.calculateResult();
}

void UI::showMushrooms(Forest& forest) {
	system("cls");
	std::cout << "NAME  |  EATABLE  |  TREATMENT" << std::endl;
	for (auto mushroom : forest.getMushrooms()) {
		std::cout << *mushroom << std::endl;
	}
	system("pause");
}

void UI::showMenu() {
	system("cls");
	std::cout << "1. Add mushroom" << std::endl;
	std::cout << "2. Show mushrooms in forest" << std::endl;
	std::cout << "3. Calculate eatable percent and treatment time" << std::endl;
	std::cout << "4. Exit" << std::endl;
}