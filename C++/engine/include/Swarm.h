//
// Created by piotr on 3/30/18.
//

#ifndef SWARMINTELLIGENCE_SWARM_H
#define SWARMINTELLIGENCE_SWARM_H

#include "Partial.h"
#include <vector>
#include <functional>
#include <iostream>

//typedef std::function<double(std::valarray<double>&)> Function;

class Swarm {
private:
    std::valarray<double> globalMinimum;
    std::vector<Partial> partials;
    unsigned long dimension;
    double low;
    double up;

public:
    Swarm(unsigned long dimension, double low, double up);

    std::valarray<double> findMinimum(int iterations, unsigned long members, Function &fun, double minimum, double c1, double c2);

    void initializePartials(unsigned long members);
    void initializeGlobalMinimum(Function &fun);

    void checkIfFoundBetterMinimum(const Function &fun, const Partial &partial);
};


#endif //SWARMINTELLIGENCE_SWARM_H
