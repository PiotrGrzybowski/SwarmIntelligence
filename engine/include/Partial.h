//
// Created by piotr on 3/30/18.
//

#ifndef SWARMINTELLIGENCE_PARTIAL_H
#define SWARMINTELLIGENCE_PARTIAL_H

#include <valarray>
#include <random>
#include <functional>
#include <cstdlib>

class Partial {
private:
    unsigned long dimension;
    double c1;
    double c2;
    double low;
    double up;
    std::valarray<double> position;
    std::valarray<double> bestPosition;
    std::valarray<double> velocity;

public:
    explicit Partial(unsigned long dimension, double low=-10, double up=10, double c1=1, double c2=1);
    virtual ~Partial();

    void process(const std::valarray<double> &globalBest, const std::function<double(std::valarray<double>)> &fun);
    void updatePosition(const std::function<double(std::valarray<double>)> &fun);
    void updateVelocity(const std::valarray<double> &globalBest);

    unsigned long getDimension() const;
    std::valarray<double> initializePosition(double low, double up);
    std::valarray<double> initializeVelocity(double low, double up);
    const std::valarray<double> &getPosition() const;
    const std::valarray<double> &getBest_position() const;
    const std::valarray<double> &getVelocity() const;
};


#endif //SWARMINTELLIGENCE_PARTIAL_H
