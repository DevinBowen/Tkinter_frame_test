import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pandas as pd


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    # showinfo(
    #     title='Selected File',
    #     message=filename
    # )


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
        frame.grid(padx=10, pady=10)

        b = Button(frame, text="Graph")
        b2 = Button(frame, text="NO")
        b.grid(row=0, column=0, sticky="EW")
        b2.grid(row=0, column=1, sticky="EW")

        switch_page_button = Button(
            self,
            text="Switch to feet conversion",
            command=lambda: controller.show_frame(Chart)
        )
        switch_page_button.grid(column=0, row=1, columnspan=2, sticky="EW")


class Chart(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        frame = LabelFrame(self, padx=50, pady=50)
        frame.grid(padx=10, pady=10)

        b = Button(frame, text="Chart")
        b.grid(row=0, column=0, sticky="EW")

        open_button = Button(
            frame,
            text='Open a File',
            command=select_file
        )
        open_button.grid(row=1, column=0, sticky="EW")

        switch_page_button = Button(
            self,
            text="Switch to feet conversion",
            command=lambda: controller.show_frame(Graph)
        )
        switch_page_button.grid(column=0, row=1, columnspan=2, sticky="EW")


root = Graphy()
root.mainloop()


# ---TEST CODE---
print(pd.__version__)
