'''
1. Feladat
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot és ezeket tárolja el egy listában! A program számolja össze, és képernyőre írja ki a listában tárolt páros számok számát, valamint a lista elemeit!
'''


import random
lista = []
for i in range(5):
  veletlen = random.randint(1, 10)
  lista.append(veletlen)

paroslista = []
for i in lista:
  if i % 2 == 0:
    paroslista.append(i)
  

print(f"A páros számok száma:{len(paroslista)}")
print(lista)