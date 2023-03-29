import matplotlib.pyplot as plt
from aggieCalcOperations import solve
import numpy as np

def draw():
    x = np.linspace(-10, 10, 21)
    y = list()
 
    with open('calc_equation.txt', 'r') as eq_file:
        eq_to_graph = eq_file.readlines()[0].split()
        
        for num in x:
            y.append(solve(eq_to_graph[:], num))

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.plot(x,y, 'g', label='Line: y= ' + ' '.join(eq_to_graph))
    plt.legend(loc="upper right")

    plt.show()