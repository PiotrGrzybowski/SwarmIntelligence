//
// Created by piotr on 3/30/18.
//

#include "../include/Swarm.h"

Swarm::Swarm(const std::function<double(const std::valarray<double> &array)> &evaluation, unsigned long dimension,
             unsigned long members, double low, double up) {
    std::vector<Partial> partials;
    for(int i = 0; i < members; i++) {
        partials.emplace_back(dimension, low, up);
    }

    this -> partials = partials;

}
