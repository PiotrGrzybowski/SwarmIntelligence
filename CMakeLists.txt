cmake_minimum_required(VERSION 3.6.3)
project(SwarmIntelligence)

set(CMAKE_CXX_STANDARD 11)

add_subdirectory(C++/lib/googletest)

include_directories(C++/engine/include)
include_directories(C++/lib/googletest/googlemock/include)
include_directories(C++/lib/googletest/googletest/include)

add_executable(SwarmIntelligence C++/main.cpp
        C++/engine/src/Partial.cpp
        C++/engine/include/Partial.h
        C++/engine/src/Swarm.cpp C++/engine/include/Swarm.h C++/tests/test_partial.cpp)

target_link_libraries(SwarmIntelligence gtest gtest_main)