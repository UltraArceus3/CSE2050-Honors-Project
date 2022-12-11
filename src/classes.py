from dataclasses import dataclass
import random
from tkinter import Tk, Label

@dataclass
class Box:
    b_type: str = None

@dataclass
class BoxSet:
    _DEF_TXT = "----------"
    _COLORS = {
        "selected": "lemon chiffon",
        "correct": "light green",
        "incorrect": "red"
    }

    types = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Brown", "Pink"]
    _types_left = len(types)
    num_of_boxes = 2

    _sel_len = 0 # stores number of items selected, as set can't
    _matched = set()
    # sets are used instead of lists as useful operations can be done in O(1)

    def __post_init__(self):
        # set for storing selected elements
        self._selected = set()
        # Creates list of boxes num_of_boxes number of times
        self.boxes = [Box(x) for _ in range(self.num_of_boxes) for x in self.types]
        # Shuffles the boxes
        random.shuffle(self.boxes)

    def _clicked(self, id):
        if self.boxes[id].b_type in self._matched: # Prevents already matched boxes from being selected again
            return (True, self.num_of_boxes - self._sel_len)

        self._selected.add(self.boxes[id].b_type)
        self._sel_len += 1

        # If more than 1 type of element selected, incorrect match, reset selection
        if len(self._selected) > 1:
            self._selected = set()
            self._sel_len = 0

            return (False, self.num_of_boxes)
        
        else:
            if self.num_of_boxes - self._sel_len == 0:
                self._types_left -= 1
                print(self._types_left)
            return (True, self.num_of_boxes - self._sel_len)


@dataclass
class Session:
    _PAUSE = False
    WINDOW: Tk
    UI_TXT: Label
    POINTS = 20
