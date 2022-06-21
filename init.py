
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
        #self.geometry('250x550')

        self.mainframe = ttk.Frame(self, padding='3 3 12 12')
        self.mainframe.grid(column=1, row=1)

        # self.mainframe.grid(column=00, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.shown_equation = tk.StringVar()
        self.equation_field = tk.Entry(self.mainframe, textvariable=self.shown_equation)
        self.equation_field.grid(columnspan=20, row=0)

        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)

        # These Buttons do stuff
        self.add = tk.Button(self.mainframe, text=' + ', command=lambda: self.update_widget("+"))
        self.add.grid(column=3,row=2)
        self.minus = tk.Button(self.mainframe, text=' - ', command=lambda: self.update_widget("-"))
        self.minus.grid(column=4,row=2)
        self.multiply = tk.Button(self.mainframe, text=' * ', command=lambda: self.update_widget("*"))
        self.multiply.grid(column=5,row=2)
        self.divide = tk.Button(self.mainframe, text=' / ', command=lambda: self.update_widget("/"))
        self.divide.grid(column=3,row=3)
        self.equals = tk.Button(self.mainframe, text=' = ', command=self.evaluate)
        self.equals.grid(column=4,row=3)
        self.clears = tk.Button(self.mainframe, text= ' C ', command=self.clear)
        self.clears.grid(column=5,row=3)
        # Extra buttons

        self.button_1 = tk.Button(self.mainframe, text='1', command=lambda: self.update_widget("1"))
        self.button_1.grid(column=0,row=2)

        self.button_2 = tk.Button(self.mainframe, text='2', command=lambda: self.update_widget("2"))
        self.button_2.grid(column=1,row=2)

        self.button_3 = tk.Button(self.mainframe, text='3', command=lambda: self.update_widget("3"))
        self.button_3.grid(column=2,row=2)

        self.button_4 = tk.Button(self.mainframe, text='4', command=lambda: self.update_widget("4"))
        self.button_4.grid(column=0,row=3)

        self.button_5 = tk.Button(self.mainframe, text='5', command=lambda: self.update_widget("5"))
        self.button_5.grid(column=1,row=3)

        self.button_6 = tk.Button(self.mainframe, text='6', command=lambda: self.update_widget("6"))
        self.button_6.grid(column=2,row=3)

        self.button_7 = tk.Button(self.mainframe, text='7', command=lambda: self.update_widget("7"))
        self.button_7.grid(column=0,row=4)

        self.button_8 = tk.Button(self.mainframe, text='8', command=lambda: self.update_widget("8"))
        self.button_8.grid(column=1,row=4)

        self.button_9 = tk.Button(self.mainframe, text='9', command=lambda: self.update_widget("9"))
        self.button_9.grid(column=2,row=4)

        self.button_0 = tk.Button(self.mainframe, text='0', command=lambda: self.update_widget("0"))
        self.button_0.grid(column=3,row=4)
if __name__ == "__main__":
    app = Calculator_OOP(f'Calculator')
    app.mainloop()
