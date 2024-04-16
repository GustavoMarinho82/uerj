palavra = "Ai minha voida"

print("============================================")
for i in palavra:
    print(i)

print("============================================")
for i in palavra[::-1]:
    print(i)

print("============================================") #.split() transforma a string em um array
for i in palavra.split(" "):
    print(i)

print("============================================")
print(palavra.replace("voida", "vida"))