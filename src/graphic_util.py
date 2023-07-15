from tkinter import ttk, Tk

class Window:
    def __init__(self, pad: int, res: str, log: object):
        """
        Creates an empty tk window, setting it into frame.
        """
        self.root = Tk()
        self.root.geometry(res)
        self.frame = ttk.Frame(self.root, padding=pad)
        self.frame.grid()
        self.log = log
        self.log.write_event("Window created successfuly")    

    
    def add_label(self, column=0, row=0, text="test"):
        ttk.Label(self.frame, text=text).grid(column=column, row=row)
        self.log.write_event("Added label successfully")

    def add_button(self, column=0, row=1, text="test", command=None):
        if command is None:
            command = self.root.destroy
        ttk.Button(self.frame, text=text, command=command).grid(column=column, row=row)
        self.log.write_event(f"Added button successfuly, button function: {command}")

    def run(self):
        self.root.mainloop()
        