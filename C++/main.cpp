#include <iostream>
#include <gtest/gtest.h>
#include <valarray>
#include "Swarm.h"


double f(const std::valarray<double> &array) {
    return array.sum();
}


double square(const std::valarray<double> &array) {
    return array[0] * array[0] - 30;
}

double bohachevskyFunction(const std::valarray<double> &array) {
    return pow(array[0], 2) + 2 * pow(array[1], 2) + (-0.3 * cos(3 * M_PI * array[0])) +
           (-0.4 * cos(4 * M_PI * array[1])) + 0.7;
}

double eggFunction(const std::valarray<double> &array) {
    double x1 = array[0];
    double x2 = array[1];

    return -(x2 + 47) * sin(sqrt(fabs(x2 + x1 / 2 + 47))) - x1 * sin(sqrt(fabs(x1 - (x2 + 47))));
}


double rastriginFunction(const std::valarray<double> &array) {
    int d = 5;
    double result = 10 * d;
    for(int i = 1; i < d+1; i++) {
//        std::cout << array[0] << " " << array[1] << " " << array[0] * array[1] << " " << - 10 * cos(2 * M_PI * array[i]) << std::endl;
        result = result + array[i] * array[i] - 10 * cos(2 * M_PI * array[i]);
    }
//    std::cout << "result = " << result << std::endl;
    return result;
}

int main(int argc, char *argv[]) {
//    testing::InitGoogleTest(&argc, argv);
//    int v = RUN_ALL_TESTS();
    srand(static_cast<unsigned int>(time(NULL)));

    Swarm swarm(5, -6, 6);

//    swarm.findMinimum(100, 5, rastriginFunction, -959.6407, 2, 2);
    swarm.findMinimum(1000, 500, rastriginFunction, 0, 1, 1);
//    std::cout << eggFunction(std::valarray<double>{512, 404}) << std::endl;
//    rastriginFunction(std::valarray<double>{0.01, 0.01});
    return 0;
}