//
// Created by piotr on 3/30/18.
//

#include <values.h>
#include "../include/Swarm.h"

Swarm::Swarm(unsigned long dimension, double low, double up) : dimension(dimension), low(low), up(up) {
    globalMinimum = std::valarray<double> (MAXFLOAT, dimension);
}

void Swarm::initializePartials(unsigned long members) {
    partials.clear();
    for(int i = 0; i < members; i++) {
//        partials.push_back(Partial(dimension, low, up));
        partials.emplace_back(dimension, low, up);
    }
}


void Swarm::initializeGlobalMinimum(Function &fun) {
    for (auto &partial : partials) {
        checkIfFoundBetterMinimum(fun, partial);
    }
}

void Swarm::checkIfFoundBetterMinimum(const Function &fun, const Partial &partial) {
    if(fun(partial.getBest_position()) < fun(globalMinimum)) {
        globalMinimum = std::valarray<double>(partial.getBest_position());
    }
}

std::valarray<double> Swarm::findMinimum(int iterations, unsigned long members, Function &fun, double minimum, double c1, double c2) {
    std::cout << "Finding minimum" << std::endl;
    initializePartials(members);
    initializeGlobalMinimum(fun);
    std::cout << "X = (" << globalMinimum[0] << ", " << globalMinimum[1] << "), " << "f(X)= " << fun(globalMinimum) << " dx = " << fabs(minimum - fun(globalMinimum)) << std::endl;

    for(int i = 0; i < iterations; i++) {
        std::cout << "i = " << i << std::endl;

        for(Partial &partial: partials) {
            partial.process(globalMinimum, fun, c1, c2);

            checkIfFoundBetterMinimum(fun, partial);
        }
        std::cout << "X = (" << globalMinimum[0] << ", " << globalMinimum[1] << "), " << "f(X)= " << fun(globalMinimum) << " dx = " << fabs(minimum - fun(globalMinimum)) << std::endl;
    }

    return globalMinimum;
}
