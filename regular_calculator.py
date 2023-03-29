from tkinter import *

import calculatorGUI as calculator_base

if __name__ == '__main__':

    # Create Widgets
    new_Calc = calculator_base.Calculator('378x410')
    new_Calc.entry_line()
    new_Calc.title('Calculator')
    
    new_Calc.entBar.grid(row=0, column=0, columnspan=4)

    new_Calc.addButton('7', 40, 20, 3, 0)
    new_Calc.addButton('8', 40, 20, 3, 1)
    new_Calc.addButton('9', 40, 20, 3, 2)

    new_Calc.addButton('4', 40, 20, 4, 0)
    new_Calc.addButton('5', 40, 20, 4, 1)
    new_Calc.addButton('6', 40, 20, 4, 2)

    new_Calc.addButton('1', 40, 20, 5, 0)
    new_Calc.addButton('2', 40, 20, 5, 1)
    new_Calc.addButton('3', 40, 20, 5, 2)

    new_Calc.addButton('0', 40, 20, 6, 0)

    new_Calc.addOpButton('C', 39, 20, 1, 3)

    new_Calc.addOpButton('+', 39, 20, 5, 3)
    new_Calc.addOpButton('-', 40, 20, 4, 3)
    new_Calc.addOpButton('*', 40, 20, 3, 3)
    new_Calc.addOpButton('/', 40, 20, 2, 3)
    new_Calc.addOpButton('(', 40, 20, 2, 1)
    new_Calc.addOpButton(')', 40, 20, 2, 2)
    new_Calc.addOpButton('x\u00b2', 38, 20, 2, 0)

    new_Calc.addOpButton('+/-', 34, 20, 6, 2)
    new_Calc.addOpButton('.', 42, 20, 6, 1)

    new_Calc.addGraphButton('EQUATION', 15, 20, 1, 0)
    new_Calc.addGraphButton('GRAPH', 23, 20, 1, 1)
    new_Calc.addGraphButton('TABLE', 26, 20, 1, 2)

    new_Calc.addSolveButton('=', 39, 20, 6, 3)

    # event loop
    new_Calc.mainloop()