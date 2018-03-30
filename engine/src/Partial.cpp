//
// Created by piotr on 3/30/18.
//

#include "../include/Partial.h"
#include <vector>

double ala(double min, double max)
{
    double f = (double)rand() / RAND_MAX;
    return min + f * (max - min);
}

Partial::Partial(unsigned long dimension, double low, double up, double c1, double c2) : dimension(dimension), c1(c1), c2(c2){
    position = initializePosition(low, up);
    velocity = initializeVelocity(low, up);
    bestPosition = std::valarray<double>(position);
}

void Partial::updatePosition(const std::function<double(std::valarray<double>)> &fun) {
    position += velocity;

    if(fun(position) < fun(bestPosition)) {
        bestPosition = position;
    }
}

void Partial::updateVelocity(const std::valarray<double> &globalBest) {
    std::valarray<double> local = (bestPosition - position) * c1 * ala(0, 1);
    std::valarray<double> global = (globalBest - position) * c2 * ala(0, 1);

    velocity = velocity + local + global;
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

void Partial::process(const std::valarray<double> &globalBest, const std::function<double(std::valarray<double>)> &fun) {
    updateVelocity(globalBest);
    updatePosition(fun);
}

std::valarray<double> Partial::initializePosition(double low, double up) {
    std::valarray<double> position(0.0, dimension);
    for(int i = 0; i < position.size(); i++) {
        position[i] = ala(low, up);
    }
    return position;
}

std::valarray<double> Partial::initializeVelocity(double low, double up) {
    std::valarray<double> velocity(0.0, dimension);
    for(int i = 0; i < velocity.size(); i++) {

        velocity[i] = ala(-fabs(up - low), fabs(up - low));
    }
    return velocity;
}

Partial::~Partial() = default;
