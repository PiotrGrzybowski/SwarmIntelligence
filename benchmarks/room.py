import yaml

from benchmark import Benchmark
from shapely.geometry import box


class Room(Benchmark):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.things = []
        self.center = (0, 0)
        # self.doors = []
        # self.windows = []

    def add_door(self, door):
        pass

    def add_window(self, window):
        pass

    def add_thing(self, thing):
        self.things.append(thing)

    def evaluate(self, *args, **kwargs):
        pass

    def is_in_domain(self, *args, **kwargs):
        pass

    @property
    def dimensions(self):
        raise NotImplementedError()

    def load_from_yml(self, path):
        with open(path) as f:
            data = yaml.safe_load(f)
            for v in data.values():
                self.add_thing(box(-v['width'], -v['height'], v['width'], v['height']))