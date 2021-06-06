try:
    a = 1/0
except ZeroDivisionError:
    print("Nie mozna dzielic przez zero!")

try:
    b = open("nieistniejacyplik.aaaaaaaaaaaaaa")
except FileNotFoundError:
    print("Ten plik nie istnieje!")