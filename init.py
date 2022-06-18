
import tkinter as tk
from tkinter import ttk
class Calculator_OOP(tk.Tk):
    def update_widget(self, item):
        self.shown_equation.set(self.shown_equation.get() + str(item))
# Gets the current equation then adds the item

    def evaluate(self):
        try:
            self.result = str(eval(self.shown_equation.get()))
            self.shown_equation.set(self.result)
        except:
            print('Error!')

    def clear(self):
        self.shown_equation.set("")

    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry('250x550')

        self.mainframe = ttk.Frame(self, padding='3 3 12 12')
        self.mainframe.pack()
        # self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
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
        self.button_clears = tk.Button(self, text= ' C ', command=self.clear).pack()
if __name__ == "__main__":
    app = Calculator_OOP(f'Calculator')
    app.mainloop()
