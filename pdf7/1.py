dict1 = {
    "imie" : "Dawid",
    "nazwisko" : "Piotrowski",
    "wiek" : 15,
    "pesel" : "123456789",
    "numer_telefonu" : "669254564"
}

print("Długość słownika: ", len(dict1))
print("\nKlucze słownika:\n")
for key in dict1:
    print(key)
print("\nWartości słownika:\n")
for key in dict1:
    print(dict1[key])
print("")
print("Czy klucz \"imie\" jest w słowniku? ", "imie" in dict1)
print("Czy klucz \"kaczka\" jest w słowniku? ", "kaczka" in dict1)
print("Odwołanie do wartości z kluczem \"nazwisko\": ", dict1["nazwisko"])
dict1["numer_telefonu"] = "112"
dict1["Rok studiów"] = 1
#print(dict1)
del dict1["Rok studiów"]
#print(dict1)

print(dict1)
print(dict1.pop("imie"))
print(dict1)
print(dict1.popitem())
print(dict1)
dict1.clear()
print(dict1)