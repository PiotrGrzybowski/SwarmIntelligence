import yaml

from algorithm import PartialSwarmOptimization
from room import Room
from thing import Thing

if __name__ == "__main__":
    room = Room(100, 100)

    with open('room.yml') as f:
        # use safe_load instead load
        data = yaml.safe_load(f)
        things = [Thing(**v) for v in data.values()]

        for thing in things:
            room.add_thing(thing)

        # room.set_thing_positions([0, 10, 25, 40])
        print(room.variables)
        print(room.evaluate())

        pso = PartialSwarmOptimization(room)

        pso.find_best_solution(10)

