import numpy as np
import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)






    def add(self, val1, val2) -> float:
        yield val1 + val2

    def substract(self, val1, val2) -> float:
        yield val1 - val2
    
    def multiply(self, val1, val2) -> float:
        yield val1 * val2
    
    def divide(self, val1, val2) -> float:
        yield val1 / val2
    
    

if __name__ == "__main__":
    app = Calculator(f'Calculator')
    app.mainloop()
