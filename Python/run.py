import yaml

from algorithm import PartialSwarmOptimization
from room import Room
from thing import Thing
from visualization_utils import RoomDrawer

if __name__ == "__main__":
    room = Room(400, 400)

    with open('room.yml') as f:
        # use safe_load instead load
        data = yaml.safe_load(f)
        things = [Thing(**v) for v in data.values()]
        print(things)

        for thing in things:
            room.add_thing(thing)

        room.set_thing_positions([100, 50, -75, -20])
        print(room.satisfy_constraints())

        pso = PartialSwarmOptimization(room, -300, 300)
        pso.find_best_solution(100)
        for p in pso.partials:
            print(room.evaluate_solution(p.solution))
        global_value = room.evaluate_solution(pso.global_solution.solution)
        global_solution = pso.global_solution.solution
        print("Solu")
        print(global_value)
        print(global_solution)
        room.set_thing_positions(global_solution)
        # pso.find_best_solution(10)

        drawer = RoomDrawer(room)
        drawer.show()