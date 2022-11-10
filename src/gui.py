import tkinter as tk
from classes import BoxSet

def init():
    main = tk.Tk() # Initializes the main GUI window

    tk.Label(main, text = "Hello World!").grid(row = 0, column = 0)

    return main

def _clicked(id):
    print(id)

def visualize_boxes(window, boxes: BoxSet):
    
    btns = []
    box_x = len(boxes.boxes) // 2 # Num. of columns
    box_y = 2 # Num. of rows

    print(boxes.boxes)
    for y in range(box_y):
        for x in range(box_x):
            id = x + y*box_x
            btns.append(tk.Button(window, text="---", command=lambda id = id: _clicked(boxes.boxes[id].b_type)).grid(row = y, column = x))