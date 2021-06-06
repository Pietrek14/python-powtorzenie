import math

def function_in_table(function, args):
    vals = [function(arg) for arg in args]
    for i in range(0, len(args)):
        print(args[i], " | ", vals[i])
        if i != len(args) - 1:
            print("-------------------------------------")

function_in_table(math.sin, [0, 1, 45, 90])