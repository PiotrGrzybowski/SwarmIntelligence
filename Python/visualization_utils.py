import numpy as np
import cv2

BLUE = (230, 230, 190)
ORANGE = (51, 153, 253)


class RoomDrawer:
    def __init__(self, room):
        self.room = room
        self.things = room.things
        self.offset = 50
        self.width = room.width + self.offset * 2
        self.height = room.height + self.offset * 2

        self.img = np.full((self.width, self.height, 3), 255, np.uint8)
        cv2.rectangle(self.img, (self.x_min, self.y_min), (self.x_max, self.y_max), BLUE, -1)
        cv2.circle(self.img, (self.width // 2, self.height // 2), int(self.room.get_max_carpet_radius()), ORANGE, -1)
        self.draw_things()
        cv2.arrowedLine(self.img, (self.width // 2, self.height), (self.width // 2, 0), (0, 0, 0), 1, tipLength=0.05)
        cv2.arrowedLine(self.img, (0, self.height // 2), (self.width, self.height // 2), (0, 0, 0), 1, tipLength=0.05)

    def show(self):
        cv2.imwrite('Room.jpg', self.img)

    def draw_thing(self, thing, i):
        color = (0, 0, 0) if thing.can_stay_on_carpet else (0, 0, 255)
        cv2.rectangle(self.img, self.point_transfer(thing.x_min, thing.y_min),
                      self.point_transfer(thing.x_max, thing.y_max), color, 1)

    def draw_things(self):
        for i, thing in enumerate(self.things):
            self.draw_thing(thing, i)

    @property
    def x_min(self):
        return self.offset

    @property
    def y_min(self):
        return self.offset

    @property
    def x_max(self):
        return self.width - self.offset

    @property
    def y_max(self):
        return self.height - self.offset

    def point_transfer(self, x, y):
        return int(x + self.width // 2), int(y + self.height // 2)
