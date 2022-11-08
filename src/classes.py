from dataclasses import dataclass
import random

@dataclass
class Box:
    b_type: str = None

@dataclass
class BoxSet:
    types = ["Red", "Blue", "Green", "Yellow", "Orange"]
    num_of_boxes = 2

    def __post_init__(self):
        # Creates list of boxes num_of_boxes number of times
        self.boxes = [Box(x) for _ in range(self.num_of_boxes) for x in self.types]
        # Shuffles the boxes
        random.shuffle(self.boxes)