import gui
import classes

if __name__ == "__main__":
    ui = gui.init()
    boxes = classes.BoxSet()

    print(len(boxes.boxes))
    gui.visualize_boxes(ui, boxes)


    ui.mainloop() # Main window loop