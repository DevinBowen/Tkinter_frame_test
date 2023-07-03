import tkinter as tk
from tkinter import ttk
from tkinter import *


class Graphy(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Graphy")
        self.frames = dict()

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        for FrameClass in (Graph, Chart):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        self.show_frame(Graph)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


class Graph(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        frame = LabelFrame(self, padx=50, pady=50)
        frame.pack(padx=10, pady=10)

        b = Button(frame, text="Graph")
        b2 = Button(frame, text="NO")
        b.grid(row=0, column=0)
        b2.grid(row=0, column=1)


class Chart(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        frame = LabelFrame(self, padx=50, pady=50)
        frame.pack(padx=10, pady=10)

        b = Button(frame, text="Chart")
        b.grid(row=0, column=0)


root = Graphy()
root.mainloop()
