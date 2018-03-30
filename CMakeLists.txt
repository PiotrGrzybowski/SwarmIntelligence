cmake_minimum_required(VERSION 3.10)
project(SwarmIntelligence)

set(CMAKE_CXX_STANDARD 17)

add_subdirectory(lib/googletest)

include_directories(include)
include_directories(lib/googletest/googlemock/include)
include_directories(lib/googletest/googletest/include)

add_executable(SwarmIntelligence main.cpp
        engine/src/Partial.cpp
        engine/include/Partial.h
        engine/src/Swarm.cpp engine/include/Swarm.h)

target_link_libraries(SwarmIntelligence gtest gtest_main)