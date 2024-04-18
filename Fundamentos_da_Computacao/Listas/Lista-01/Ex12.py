# Lista 1 - Exercício 12

base = float(input("Base do triângulo: "))
altura = float(input("Altura do triângulo: "))

if (base <= 0) or (altura <= 0):
    print("Foram inseridos dados inválidos!")

else:
    area = (base * altura)/2
    print("A área do triangulo é:", area)