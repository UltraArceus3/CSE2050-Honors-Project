import tkinter as tk
from classes import BoxSet

_DEF_TXT = "----------"
pause = False

def init():
    main = tk.Tk() # Initializes the main GUI window

    main.resizable(False, False)
    #tk.Label(main, text = "Hello World!").grid(row = 0, column = 0)

    return main

def _clicked(id, boxes, btns):
    global pause
    def _reset_btns():
        [btn.config(text = _DEF_TXT) for id, btn in enumerate(btns) if boxes.boxes[id].b_type not in boxes._matched] # Resets button text back to default


    if pause:
        pause = False
        _reset_btns()
        

    print(boxes.boxes[int(id)])
    btns[id].config(text = boxes.boxes[id].b_type)

    res = boxes.on_click(id)

    if not(res[0]): # If player selects wrong box combination
        pause = True
    elif res[1] <= 0: # If there are no more required boxes to match (i.e. player matched type)
        boxes._matched.add(list(boxes._selected)[0])
        print(boxes._matched)
        boxes._selected = set()
        boxes._sel_len = 0
        _reset_btns()

    print(res)

def visualize_boxes(window, boxes: BoxSet):
    
    btns = []
    box_x = len(boxes.boxes) // 2 # Num. of columns
    box_y = 2 # Num. of rows

    for y in range(box_y):
        for x in range(box_x):
            id = x + y*box_x
            btns.append(tk.Button(window, text = _DEF_TXT, command = lambda id = id: _clicked(id, boxes, btns), width = 10, height = 5))
            btns[-1].grid(row = y, column = x)