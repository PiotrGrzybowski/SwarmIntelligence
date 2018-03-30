//
// Created by piotr on 3/30/18.
//

#ifndef SWARMINTELLIGENCE_SWARM_H
#define SWARMINTELLIGENCE_SWARM_H

#include "Partial.h"
#include <vector>
#include <functional>

class Swarm {
private:
    std::vector<Partial> partials;
    std::function<double()> evaluation;
    unsigned long dimension;
    unsigned long members;
    double low;
    double up;

public:
    Swarm(const std::function<double(const std::valarray<double> &array)> &evaluation, unsigned long dimension, unsigned long members, double low, double up);
};


#endif //SWARMINTELLIGENCE_SWARM_H
