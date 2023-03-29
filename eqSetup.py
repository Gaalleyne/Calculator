from tkinter import *

import graphingFunc as graphFunc

def displayEq():

    # Create Widgets
    new_Graph = graphFunc.graphMenus('390x410')
    new_Graph.title('Calculator')

    new_Graph.addLabel("Graphing Equations", "Arial", 25, 0.5, 0, "n")

    new_Graph.addLabel("Y =", "Arial", 10, 0.1, (0.15))
    new_Graph.entry_line(0.5, (0.15), '0')

    new_Graph.addButton('7', 30, 15, 0.29, 0.4)
    new_Graph.addButton('8', 30, 15, 0.49, 0.4)
    new_Graph.addButton('9', 30, 15, 0.69, 0.4)

    new_Graph.addButton('4', 30, 15, 0.29, 0.5325)
    new_Graph.addButton('5', 30, 15, 0.49, 0.5325)
    new_Graph.addButton('6', 30, 15, 0.69, 0.5325)

    new_Graph.addButton('1', 30, 15, 0.29, 0.6625)
    new_Graph.addButton('2', 30, 15, 0.49, 0.6625)
    new_Graph.addButton('3', 30, 15, 0.69, 0.6625)

    new_Graph.addButton('0', 30, 15, 0.29, 0.795)

    new_Graph.addOpButton('+', 28, 15, 0.89, 0.6625)
    new_Graph.addOpButton('-', 30, 15, 0.89, 0.5325)
    new_Graph.addOpButton('*', 30, 15, 0.89, 0.4)
    new_Graph.addOpButton('/', 30, 15, 0.89, 0.265)
    new_Graph.addOpButton('(', 30, 15, 0.49, 0.265)
    new_Graph.addOpButton(')', 30, 15, 0.69, 0.265)
    new_Graph.addOpButton('+/-', 24, 15, 0.49, 0.795)
    new_Graph.addOpButton('.', 32, 15, 0.69, 0.795)
    new_Graph.addOpButton('x\u00b2', 29, 15, 0.29, 0.265)

    new_Graph.addOpButton('C', 29, 15, 0.1, 0.265)

    new_Graph.addSpecButton('CLOSE', 13, 15, 0.1, 0.795)
    new_Graph.addSpecButton('2ND', 22, 15, 0.1, 0.4)

    new_Graph.addGraphButton('FINISH', 13, 15, 0.89, 0.795)

    new_Graph.addButton('X', 29, 15, 0.1, 0.5325)
    new_Graph.addButton('Y', 29, 15, 0.1, 0.6625)

    # event loop
    new_Graph.mainloop()