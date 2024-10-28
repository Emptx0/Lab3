#pragma once
#ifndef FOREST_H
#define FOREST_H

#include <vector>
#include "mushrooms.h"

class Forest {
private:
	std::vector<Mushroom*> mushrooms;
public:
	~Forest();
	std::vector<Mushroom*> getMushrooms();
	void setMushrooms(std::vector<Mushroom*>&);
};

class ForestRepository {
private:
	std::string filename;
public:
	ForestRepository(std::string);

	void addMushroomToForest(std::string, bool, int, Forest&);
	void loadMushroomsList(Forest&);
};

#endif

