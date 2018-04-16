import numpy as np
import cv2


def visualize_room(room):
    image = np.full((room.width, room.height), 255, dtype=int)
