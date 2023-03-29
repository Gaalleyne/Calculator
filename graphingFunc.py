from tkinter import *
#import tableMaker as new_table

class graphMenus(Tk):
    op_list = list(['+', '-', '*', '/', '(', ')'])

    def __init__(self, geometry):
        super().__init__()
        self.geometry(geometry)

    def click(self, func):
        current = self.entBar.get()

        if current == '0':
            self.entBar.delete(0, END)

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
            
            self.entBar.delete(0, END)
            self.entBar.insert(0, ' '.join(expr))
    
    def varClick(self, func):
        current = self.entBar.get()

        if current == '0':
            self.entBar.delete(0, END)

        self.entBar.insert(END, func)

    def special_action(self, request : str):
        
        if request == 'CLOSE':
            self.destroy()
            pass

    def save_and_finish(self):
        
        expr = self.entBar.get()

        with open('calc_equation.txt', 'w') as save_file:
            save_file.write(expr)

        self.destroy()
    
    def entry_line(self, x, y, eq, anchor="center"):
        self.entBar = Entry(self, width=40, borderwidth=5)
        self.entBar.place(anchor=anchor, relx=x, rely=y)
        self.entBar.insert(0, eq)

    def addButton(self, name, x, y, loc1, loc2):
        Button(self, text=name, padx=x, pady=y, command=lambda: self.click(name.lower())).place(anchor='center', relx=loc1, rely=loc2)

    def addOpButton(self, name, x, y, loc1, loc2):
        Button(self, text=name, padx=x, pady=y, command=lambda: self.opClick(name)).place(anchor='center', relx=loc1, rely=loc2)

    def addSpecButton(self, name, x, y, loc1, loc2):
        Button(self, text=name, padx=x, pady=y, command=lambda: self.special_action(name)).place(anchor='center', relx=loc1, rely=loc2)
        
    def addGraphButton(self, name, x, y, loc1, loc2):
        Button(self, text=name, padx=x, pady=y, command=lambda: self.save_and_finish()).place(anchor='center', relx=loc1, rely=loc2)

    def addLabel(self, name, font, fontsize, x, y, anchor="center"):
        Label(self, text=name, font=(font, fontsize)).place(anchor=anchor, relx=x, rely=y)