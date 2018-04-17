import yaml

from algorithm import PartialSwarmOptimization
from room import Room
from thing import Thing
from visualization_utils import RoomDrawer

if __name__ == "__main__":
    room = Room(400, 400)

    with open('room.yml') as f:
        data = yaml.safe_load(f)
        things = [Thing(**v) for v in data.values()]

        for thing in things:
            room.add_thing(thing)

        pso = PartialSwarmOptimization(room, -300, 300)
        pso.find_best_solution(partials=100, iterations=10)

        global_value = room.evaluate_solution(pso.global_solution)
        print(pso.global_solution)
        room.set_thing_positions(pso.global_solution)
        print(type(pso.global_solution))
        drawer = RoomDrawer(room)
        drawer.show()