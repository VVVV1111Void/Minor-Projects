
import tkinter as tk
from tkinter import ttk
class Calculator_OOP(tk.Tk):
    def update_widget(self, item):
        self.expression = self.expression + str(item)
        self.shown_equation.set(self.expression)

    def evaluate(self):
        self.expression = self.shown_equation.get()
        self.result = str(eval(self.expression))
        self.shown_equation.set(self.result)
        self.expression = ""

    def clear(self):
        self.expression = ""

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
        self.button_add = tk.Button(self, text=' + ', command=lambda: self.update_widget("+")).pack()
        self.button_minus = tk.Button(self, text=' - ', command=lambda: self.update_widget("-")).pack()
        self.button_multiply = tk.Button(self, text=' * ', command=lambda: self.update_widget("*")).pack()
        self.button_divide = tk.Button(self, text=' / ', command=lambda: self.update_widget("/")).pack()
        self.button_equals = tk.Button(self, text=' = ', command=self.evaluate).pack()
if __name__ == "__main__":
    app = Calculator_OOP(f'Calculator')
    app.mainloop()
