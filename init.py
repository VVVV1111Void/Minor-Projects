import numpy as np
import tkinter as tk
from tkinter import ttk
class Calculator_OOP(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry('250x550')

        self.mainframe = ttk.Frame(self, padding='3 3 12 12')
        self.mainframe.pack()
        # self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        self.expression = ""
        self.shown_equation = tk.StringVar()
        self.equation_field = tk.Entry(self, textvariable=self.shown_equation)
        self.equation_field.pack()
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
    def update(self, number):
        return (self.expression + number)

    def evaluate(self, equation):
        return str(eval(expression))
    def clear(self):
        self.expression = ""

if __name__ == "__main__":
    app = Calculator_OOP(f'Calculator')
    app.mainloop()
