from room import Room
from thing import Thing

if __name__ == "__main__":
    room = Room(100, 100)
    chair = Thing('Chair', 10, 10, 20, 20, False)
    table = Thing('Table', 10, 10, 40, 50, False)

    room.add_thing(chair)
    room.add_thing(table)

    print(room.variables())
    print(chair.calculate_distance_from_point((0, 0)))