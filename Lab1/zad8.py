lista = []
a = 0
while  a != "q":
    a = input()
    if a != "q":
        lista.append(a)
lista = tuple(lista)
print(lista)