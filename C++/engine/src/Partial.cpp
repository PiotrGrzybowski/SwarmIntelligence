//
// Created by piotr on 3/30/18.
//

#include "../include/Partial.h"
#include <vector>
#include <iostream>

double uniform_real(double min, double max) {
    double f = (double) rand() / RAND_MAX;
    return min + f * (max - min);
}

Partial::Partial(unsigned long dimension, double low, double up) : dimension(dimension) {
    position = initializePosition(low, up);
    velocity = initializeVelocity(low, up);
    bestPosition = std::valarray<double>(position);
}

void Partial::updatePosition(Function &fun) {
    position += velocity;

    if (fun(position) < fun(bestPosition)) {
        bestPosition = position;
    }
}

void Partial::updateVelocity(const std::valarray<double> &globalBest, double c1, double c2) {
    velocity = velocity + (bestPosition - position) * c1 * uniform_real(0, 1) + (globalBest - position) * c2 * uniform_real(0, 1);
}

unsigned long Partial::getDimension() const {
    return dimension;
}

const std::valarray<double> &Partial::getPosition() const {
    return position;
}

const std::valarray<double> &Partial::getBest_position() const {
    return bestPosition;
}

const std::valarray<double> &Partial::getVelocity() const {
    return velocity;
}

void Partial::process(const std::valarray<double> &globalBest, Function &fun, double c1, double c2) {
    updateVelocity(globalBest, c1, c2);
    updatePosition(fun);
}

std::valarray<double> Partial::initializePosition(double low, double up) {
    std::valarray<double> position(0.0, dimension);
    for (int i = 0; i < position.size(); i++) {
        position[i] = uniform_real(low, up);
    }
    return position;
}

std::valarray<double> Partial::initializeVelocity(double low, double up) {
    std::valarray<double> velocity(0.0, dimension);
    for (int i = 0; i < velocity.size(); i++) {

        velocity[i] = uniform_real(-fabs(up - low), fabs(up - low));
    }
    return velocity;
}

Partial::~Partial() = default;
