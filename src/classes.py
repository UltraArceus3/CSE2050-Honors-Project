from dataclasses import dataclass

@dataclass
class Box:
    b_type: str = None

@dataclass
class BoxSet:
    types: list = ["Red", "Blue", "Green", "Yellow", "Orange"]
    num_of_boxes: int = 2

    def __post_init__(self):
        boxes = []