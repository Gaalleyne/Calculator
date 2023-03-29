from tkinter import *
from tokenize import String
import aggieCalcOperations as calc
import graphSetup as display_Graph
import eqSetup as graphEqMenu
import tableSetup as graphTable

class Calculator(Tk):
    op_list = list(['+', '-', '*', '/', '(', ')'])

    def __init__(self, geometry):
        super().__init__()
        self.geometry(geometry)

    # Events
    def click(self, func):

        current = self.entBar.get()
        isOp = False

        if current == '0':
            self.entBar.delete(0, END)
            self.entBar.insert(0, int(func))

        elif ('=' in current):
            for op in self.op_list:
                if op in current:
                    isOp = True
            
            if isOp:
                self.entBar.delete(0, 1)
            else:
                self.entBar.delete(0, END)

            self.entBar.insert(END, func)

        else:
            self.entBar.insert(END, func)

    def opClick(self, func : str):
        expr = self.entBar.get().split()

        if 'C' in func:
            self.entBar.delete(0, END)
            self.entBar.insert(0, '0')

        else:

            if '.' in func:
                if '.' not in expr[-1]:
                    expr[-1] = expr[-1] + '.'

            elif '+/-' in func:
                if float(expr[-1]) > 0:
                    expr[-1] = '-' + expr[-1]
                else:
                    expr[-1] = expr[-1][1:]
            
            elif '(' in func:
                if len(expr) == 1 and expr[0] == '0':
                    expr.clear()
                expr.append(func + ' ')

            elif not(func[1:].isdecimal()) and not(func in self.op_list):
                expr.append(func[1:] + ' ')

            else:
                expr.append(func + ' ')
            
            self.entBar.delete(0,END)
            self.entBar.insert(0, ' '.join(expr))

    def entry_line(self):
        self.entBar = Entry(self, width=55, borderwidth=5)
        self.entBar.insert(0, '0')
    
    def solve(self):
        expr = self.entBar.get().split()
        result = calc.solve(expr)
        self.entBar.delete(0, END)
        self.entBar.insert(0, '= ' + str(result))
    
    def sysGraph(self, task):

        if task == 'EQUATION':
            graphEqMenu.displayEq()

        elif task == 'TABLE':
            graphTable.display_table()

        elif task == 'GRAPH':
            display_Graph.draw()

        else:
            pass

    def addButton(self, name, x, y, loc1, loc2):
        Button(self, text=name, padx=x, pady=y, command=lambda: self.click(name)).grid(row=loc1, column=loc2)

    def addOpButton(self, name, x, y, loc1, loc2):
        Button(self, text=name, padx=x, pady=y, command=lambda: self.opClick(name)).grid(row=loc1, column=loc2)

    def addSolveButton(self, name, x, y, loc1, loc2):
        Button(self, text=name, padx=x, pady=y, command=lambda: self.solve()).grid(row=loc1, column=loc2)
    
    def addGraphButton(self, name, x, y, loc1, loc2):
        Button(self, text=name, padx=x, pady=y, command=lambda: self.sysGraph(name)).grid(row=loc1, column=loc2)
