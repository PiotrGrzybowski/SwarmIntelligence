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

        pso = PartialSwarmOptimization(room, -100, 100)
        pso.find_best_solution(partials=20, iterations=100)

        room.set_thing_positions(pso.global_solution)
        drawer = RoomDrawer(room)
        drawer.show()