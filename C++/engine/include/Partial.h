//
// Created by piotr on 3/30/18.
//

#ifndef SWARMINTELLIGENCE_PARTIAL_H
#define SWARMINTELLIGENCE_PARTIAL_H

#include <valarray>
#include <random>
#include <functional>
#include <cstdlib>

typedef const std::function<double(const std::valarray<double> &)> Function;

class Partial {
private:
    unsigned long dimension;

    std::valarray<double> position;
    std::valarray<double> bestPosition;
    std::valarray<double> velocity;

public:
    explicit Partial(unsigned long dimension, double low=-10, double up=10);
    virtual ~Partial();

    void process(const std::valarray<double> &globalBest, Function &fun, double c1, double c2);
    void updatePosition(Function &fun);
    void updateVelocity(const std::valarray<double> &globalBest, double c1, double c2);

    unsigned long getDimension() const;
    std::valarray<double> initializePosition(double low, double up);
    std::valarray<double> initializeVelocity(double low, double up);

    const std::valarray<double> &getPosition() const;
    const std::valarray<double> &getBest_position() const;
    const std::valarray<double> &getVelocity() const;
};


#endif //SWARMINTELLIGENCE_PARTIAL_H
