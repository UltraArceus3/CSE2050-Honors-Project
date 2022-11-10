from dataclasses import dataclass
import random

@dataclass
class Box:
    b_type: str = None

@dataclass
class BoxSet:
    types = ["Red", "Blue", "Green", "Yellow", "Orange"]
    num_of_boxes = 2
    _selected = set() # set for storing selected elements
    _sel_len = 0 # stores number of items selected, as set can't
    # sets are used instead of lists as useful operations can be done in O(1)

    def __post_init__(self):
        # Creates list of boxes num_of_boxes number of times
        self.boxes = [Box(x) for _ in range(self.num_of_boxes) for x in self.types]
        # Shuffles the boxes
        random.shuffle(self.boxes)

    def on_click(self, id):
        self._selected.add(id)
        self._sel_len += 1

        # If more than 1 type of element selected, incorrect match, reset selection
        if len(self._selected) > 1:
            self._selected = set()
            self._sel_len = 0

            return (False, self.num_of_boxes)
        
        else:
            return (True, self.num_of_boxes - self._sel_len)

                
