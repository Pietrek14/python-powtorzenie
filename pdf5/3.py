import math
import numpy
import matplotlib.pyplot as plt

def function_plot(function, min, max, precision, legend):
    x = numpy.arange(min, max, precision).tolist()
    y = list(map(function, x))
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(legend, loc=4)
    plt.savefig("wykres.png")
    plt.show()

function_plot(math.sin, -10, 10, 0.1, "sin()")