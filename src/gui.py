import tkinter as tk


def init():
    main = tk.Tk() # Initializes the main GUI window

    tk.Label(main, text = "Hello World!").grid(row = 0, column = 0)


    main.mainloop() # Main window loop