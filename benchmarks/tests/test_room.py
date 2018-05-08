import numpy as np
import unittest

from Python.geometric_utils import is_pair_in_collision, thing_collision_pairs, collision_penalty, \
    left_collision_penalty, right_collision_penalty, top_collision_penalty, bottom_collision_penalty
from Python.thing import Thing
from Python.visualization_utils import RoomDrawer
from benchmarks.room import Room


class TestRoom(unittest.TestCase):
    def test_border_penalty(self):
        room = Room(100, 100)
        thing1 = Thing("Table", 40, 40, False)
        room.add_thing(thing1)

        thing1.set_position(-50, 0)
        self.assertEqual(20, room.border_penalty(thing1))

        thing1.set_position(50, 0)
        self.assertEqual(20, room.border_penalty(thing1))

        thing1.set_position(0, -50)
        self.assertEqual(20, room.border_penalty(thing1))

        thing1.set_position(0, 50)
        self.assertEqual(20, room.border_penalty(thing1))

        thing1.set_position(-50, -50)
        self.assertEqual(20 * np.sqrt(2), room.border_penalty(thing1))

        thing1.set_position(-50, 50)
        self.assertEqual(20 * np.sqrt(2), room.border_penalty(thing1))

        thing1.set_position(50, -50)
        self.assertEqual(20 * np.sqrt(2), room.border_penalty(thing1))

        thing1.set_position(50, 50)
        self.assertEqual(20 * np.sqrt(2), room.border_penalty(thing1))

        thing1.set_position(-70, 0)
        self.assertEqual(40, room.border_penalty(thing1))

    def test_is_pair_in_collision(self):
        room = Room(100, 100)

        thing1 = Thing("Table", 20, 20, True)
        thing2 = Thing("Table", 20, 20, False)
        thing3 = Thing("Table", 20, 20, False)

        thing1.set_position(0, 0)
        thing2.set_position(-12, 12)
        thing3.set_position(15, 0)

        room.add_thing(thing1)
        room.add_thing(thing2)
        room.add_thing(thing3)

        self.assertTrue(is_pair_in_collision(thing1, thing2))
        self.assertTrue(is_pair_in_collision(thing1, thing3))
        self.assertFalse(is_pair_in_collision(thing2, thing3))

    def test_thing_collision_pairs(self):
        room = Room(100, 100)

        thing1 = Thing("Table", 20, 20, True)
        thing2 = Thing("Table", 20, 20, False)
        thing3 = Thing("Table", 20, 20, False)

        thing1.set_position(0, 0)
        thing2.set_position(-12, 12)
        thing3.set_position(15, 0)

        room.add_thing(thing1)
        room.add_thing(thing2)
        room.add_thing(thing3)

        self.assertEqual(2, len(thing_collision_pairs(room.things)))

    def test_collision_penalty(self):
        room = Room(200, 200)
        thing1 = Thing("Table", 40, 40, True)
        thing2 = Thing("Table", 20, 20, False)
        room.add_thing(thing1)
        room.add_thing(thing2)

        thing1.set_position(0, 0)
        thing2.set_position(0, 0)

        self.assertEqual(10, left_collision_penalty(thing1, thing2))
        self.assertEqual(10, right_collision_penalty(thing1, thing2))
        self.assertEqual(10, top_collision_penalty(thing1, thing2))
        self.assertEqual(10, bottom_collision_penalty(thing1, thing2))
        self.assertEqual(20 * np.sqrt(2), collision_penalty(thing1, thing2))
        self.assertEqual(20 * np.sqrt(2), room.total_collision_penalty())
        thing1.set_position(0, 0)
        thing2.set_position(20, 0)

        self.assertEqual(0, left_collision_penalty(thing1, thing2))
        self.assertEqual(10, right_collision_penalty(thing1, thing2))
        self.assertEqual(10, top_collision_penalty(thing1, thing2))
        self.assertEqual(10, bottom_collision_penalty(thing1, thing2))
        self.assertEqual(10 * np.sqrt(5), collision_penalty(thing1, thing2))
        self.assertEqual(10 * np.sqrt(5), room.total_collision_penalty())

        drawer = RoomDrawer(room)
        drawer.show()


if __name__ == '__main__':
    unittest.main()
