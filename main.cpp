#include <iostream>
#include <gtest/gtest.h>
#include <valarray>
#include "engine/include/Partial.h"
#include "engine/include/Swarm.h"

double f(const std::valarray<double> &array) {
    return array.sum();
}

int main(int argc, char* argv[]) {
    testing::InitGoogleTest(&argc, argv);
    int v = RUN_ALL_TESTS();
    srand (static_cast<unsigned int>(time(NULL)));

    Swarm s(f, 5, 50, -10.0, 10.0);

    return 0;
}