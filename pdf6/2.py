import numpy

matrix1 = numpy.matrix([[1,4,5],[2,6,3],[0,9,8]])
matrix2 = numpy.matrix([[5,2,6],[3,7,8],[5,8,3]])

print("+: " + str(matrix1 + matrix2))
print("-: " + str(matrix1 - matrix2))
print("*: " + str(matrix1 * matrix2))
print("/: " + str(matrix1 / matrix2))
print("** 2: " + str(matrix1 ** 2))
print("%: " + str(matrix1 % matrix2))
print("Mnożenie przez skalar (2): " + str(matrix1 * 2))
print("Dzielenie przez skalar (2): " + str(matrix1 / 2))