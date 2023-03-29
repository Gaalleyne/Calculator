from tkinter import *
from plug_n_chug import createTable as cT

def display_table():
    
    new_Graph = Tk()
    new_Graph.geometry('450x450')
    new_Graph.title('Calculator')
    expr = open('calc_equation.txt', 'r')
    
    equation = str(expr.readlines()[0])

    Label(new_Graph, text='x', borderwidth=1, relief='solid', width=14, height=4).grid(row=0,column=0)
    Label(new_Graph, text='f(x)', borderwidth=1, relief='solid', width=14, height=4).grid(row=0,column=1)
    Label(new_Graph, text='x\u2081', borderwidth=1, relief='solid', width=14, height=4).grid(row=0,column=2)
    Label(new_Graph, text='f\u2081(x)', borderwidth=1, relief='solid', width=14, height=4).grid(row=0,column=3)

    Button(new_Graph, text='EQ_CLR', borderwidth=1, width=14, height=6, command=lambda: eq_destroy(new_Graph)).grid(row=5, column=0)
    Button(new_Graph, text='CLOSE', borderwidth=1, width=14, height=6, command=lambda: new_Graph.destroy()).grid(row=5, column=1)
    Button(new_Graph, text='CLEAR', borderwidth=1, width=14, height=6, command=lambda: clearTable(x1,x2,x3,x4,y1,y2,y3,y4,add_num)).grid(row=5, column=2)
    Button(new_Graph, text='ENTER', borderwidth=1, width=14, height=6, command=lambda: editTable(x1,x2,x3,x4,y1,y2,y3,y4,equation,add_num)).grid(row=5, column=3)
    add_num = Entry(new_Graph, borderwidth=1, relief='solid', width=17)
    add_num.insert(0, '0')

    for i in range(4):
        Label(new_Graph, text=str(i), borderwidth=1, relief='solid', width=14, height=4).grid(row=i+1,column=0)
        Label(new_Graph, text=str(round(cT(equation, i),5)), borderwidth=1, relief='solid', width=14, height=4).grid(row=i+1,column=1)

    x1 = Label(new_Graph, borderwidth=1, relief='solid', width=14, height=4)
    x2 = Label(new_Graph, borderwidth=1, relief='solid', width=14, height=4)
    x3 = Label(new_Graph, borderwidth=1, relief='solid', width=14, height=4)
    x4 = Label(new_Graph, borderwidth=1, relief='solid', width=14, height=4)

    y1 = Label(new_Graph, text='_', borderwidth=1, relief='solid', width=14, height=4)
    y2 = Label(new_Graph, text='_', borderwidth=1, relief='solid', width=14, height=4)
    y3 = Label(new_Graph, text='_', borderwidth=1, relief='solid', width=14, height=4)
    y4 = Label(new_Graph, text='_', borderwidth=1, relief='solid', width=14, height=4)

    x1.grid(row=1, column=2)
    x2.grid(row=2, column=2)
    x3.grid(row=3, column=2)
    x4.grid(row=4, column=2)
    y1.grid(row=1, column=3)
    y2.grid(row=2, column=3)
    y3.grid(row=3, column=3)
    y4.grid(row=4, column=3)
    add_num.grid(row=6, column=3)

    new_Graph.mainloop()

def editTable(x1 : Label, x2 : Label, x3 : Label, x4 : Label, y1 : Label, y2 : Label, y3 : Label, y4 : Label, expr : str, entBar : Entry):
    x_num_to_add = int(entBar.get())
    y_num_to_add = round(cT(expr, x_num_to_add), 5)

    if (x1.cget("text") == ''):
        x1.config(text=str(x_num_to_add))
        y1.config(text=str(y_num_to_add))

    elif (x2.cget("text") == ''):
        x2.config(text=str(x_num_to_add))
        y2.config(text=str(y_num_to_add))

    elif (x3.cget("text") == ''):
        x3.config(text=str(x_num_to_add))
        y3.config(text=str(y_num_to_add))

    elif (x4.cget("text") == ''):
        x4.config(text=str(x_num_to_add))
        y4.config(text=str(y_num_to_add))

    else:
        entBar.delete(0,END)
        entBar.insert(0, 'FULL!')

def clearTable(x1 : Label, x2 : Label, x3 : Label, x4 : Label, y1 : Label, y2 : Label, y3 : Label, y4 : Label, entBar : Entry):
    x1.config(text='')
    x2.config(text='')
    x3.config(text='')
    x4.config(text='')

    y1.config(text='_')
    y2.config(text='_')
    y3.config(text='_')
    y4.config(text='_')

    entBar.delete(0, END)
    entBar.insert(0, '0')

def eq_destroy(win : Tk):
    with open('calc_equation.txt', 'w') as eq_file:
        eq_file.write('0')
    win.destroy()