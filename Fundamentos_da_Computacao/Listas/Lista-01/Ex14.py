# Lista 1 - Exercício 14
import random

Bois = []
maior = menor = 0

for i in range(91):
    Bois.append(random.randint(220, 300))

    if (Bois[i] >= Bois[maior]):
        maior = i

    if (Bois[i] <= Bois[menor]):
        menor = i

print(f"Id e peso do menor boi: {menor} - {Bois[menor]}kg")
print(f"Id e peso do maior boi: {maior} - {Bois[maior]}kg")
print(f"Se os maiores bois tiverem o mesmo peso, o maior será o último que foi checado (ele também será o que tem o maior id)")