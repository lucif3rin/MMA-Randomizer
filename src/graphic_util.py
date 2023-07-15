from logging import Log
from tkinter import ttk, Tk

class Window:
    def __init__(self, pad: int, res: str, log: Log):
        """
        Creates an empty tk window, setting it into frame.
        """
        self.root = Tk()
        self.root.geometry(res)
        self.frame = ttk.Frame(self.root, padding=pad)
        self.frame.grid()
        self.log = log
        self.log.write_event("Window created successfuly")    

    
    def add_button(self, column=0, row=0, text="test"):
        ttk.Label(self.frame, text=text).grid(column=column, row=row)

    def run(self):
        self.root.mainloop()
        