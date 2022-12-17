import tkinter as tk
from classes import BoxSet, Session




def init():
    win = tk.Tk() # Initializes the main GUI window

    win.title("Memory Game")
    win.resizable(False, False)
    tk.Label(win, text = "Memory Game by Rany Kamel", font=("Arial", 10)).grid(row = 0, column = 0, columnspan=100, sticky=tk.EW)

    ui_txt = tk.Label(win, text = "...")
    points = tk.Label(win, text = "Points: 0")
    ui_txt.grid(row = 1, column = 0, columnspan=100, sticky=tk.EW)
    points.grid(row = 2, column = 0, columnspan=100, sticky=tk.EW)

    tk.Button(win, text = "Reset", command= lambda ui = win : _reset(main)).grid(row = 0, column = 0, sticky=tk.NW)

    main = Session(WINDOW = win, UI_TXT = [ui_txt, points])

    main.UI_TXT[1].config(text = f"Points: {main.POINTS}")
    return main

def _reset(sess):
    sess._PAUSE = False
    
    sess.POINTS = 20
    
    sess.UI_TXT[0].config(text = "...", bg = sess.WINDOW.cget("bg"))
    sess.UI_TXT[1].config(text = f"Points: {sess.POINTS}")

    boxes = BoxSet()

    print(len(boxes.boxes))
    visualize_boxes(sess, boxes)

def on_click(id, boxes, btns, sess):
    global _PAUSE

    

    def _reset_btns():
        # Resets button text back to default
        [btn.config(text = boxes._DEF_TXT, bg = sess.WINDOW.cget("bg")) for id, btn in enumerate(btns) if boxes.boxes[id].b_type not in boxes._matched]
        sess.UI_TXT[0].config(text = "...")

    if btns[id]['text'] != boxes._DEF_TXT and len(boxes._selected) > 0: # Prevents already selected boxes from being re-selected
        return

    if sess.POINTS <= 0:
        return

    if btns[id].cget("bg") == boxes._COLORS["correct"]:
        return

    if sess._PAUSE:
        sess._PAUSE = False
        _reset_btns()
        
    print(boxes.boxes[id])
    sess.UI_TXT[0].config(bg = sess.WINDOW.cget("bg"))
    btns[id].config(text = boxes.boxes[id].b_type, bg = boxes._COLORS["selected"])
    sess.UI_TXT[0].config(text = f"SELECTED: {boxes.boxes[id].b_type}")

    res = boxes._clicked(id)

    if not(res[0]): # If player selects wrong box combination
        sess._PAUSE = True
        sess.POINTS -= 1
        sess.UI_TXT[0].config(text = "INCORRECT!", bg = "red")

        [btn.config(bg = boxes._COLORS["incorrect"]) for btn in btns if btn.cget("bg") == boxes._COLORS["selected"]]

        if sess.POINTS <= 0:
            _reset_btns()
            sess.UI_TXT[0].config(text = "you lost... press the reset button to start over.")

    elif res[1] <= 0: # If there are no more required boxes to match (i.e. player matched type)
        sess._PAUSE = True
        
        boxes._matched.add(list(boxes._selected)[0])
        
        sess.POINTS += 1
        sess.UI_TXT[0].config(text = "CORRECT!!!", bg = "light green")

        [btn.config(bg = boxes._COLORS["correct"]) for btn in btns if btn.cget("bg") == boxes._COLORS["selected"]]
        #btns[id].config(bg="light green")

        print(boxes._matched)
        boxes._selected = set()
        boxes._sel_len = 0
        
    if boxes._types_left == 0:
        sess.PAUSE = True
        sess.UI_TXT[0].config(text = "YOU WON" + "!" * len(boxes.types), bg = "lime")

    sess.UI_TXT[1].config(text = f"Points: {sess.POINTS}")
    print(res)

def visualize_boxes(session, boxes: BoxSet):
    
    btns = []
    box_x = len(boxes.boxes) // 2 # Num. of columns
    box_y = 2 # Num. of rows

    for y in range(box_y):
        for x in range(box_x):
            id = x + y*box_x
            btns.append(tk.Button(session.WINDOW, text = boxes._DEF_TXT, command = lambda id = id: on_click(id, boxes, btns, session), 
                                  width = 10, height = 5))
            btns[-1].grid(row = y + 3, column = x)