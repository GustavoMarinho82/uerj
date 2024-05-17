# Ordenar um vetor de binários usando selection sort
# Convertendo e desconvertendo de binário para decimal

vetor_bin = ["101", "010", "110", "100", "001", "111", "011"]
vetor_dec = [0]*7
vetor_final = [""]*7

# BIN PARA DEC ======================================================#
for x in range(0, len(vetor_bin)):
    n_bin = vetor_bin[x]
    
    for y in range((len(n_bin)-1), -1, -1):
        if (n_bin[y] == "1"):
            vetor_dec[x] += 2**(len(n_bin) - int(y) - 1)
#====================================================================#

# SELECTION SORT ====================================================#
for x in range(0, len(vetor_dec)):
    index_menor = x
    
    for y in range(x+1, len(vetor_dec)):
        if(vetor_dec[y] < vetor_dec[index_menor]):
            index_menor = y
    
    valor_auxliar = vetor_dec[x]
    vetor_dec[x] = vetor_dec[index_menor]
    vetor_dec[index_menor] = valor_auxliar
#====================================================================#

# DEC PARA BIN ======================================================#
for x in range(0, len(vetor_final)):
    n_dec = vetor_dec[x]
    
    while (n_dec != 0):
        vetor_final[x] += str(n_dec % 2)
        n_dec //= 2
    
    vetor_final[x] = "{:>03}".format(vetor_final[x][::-1])
#====================================================================#

print("Vetor binário:", vetor_bin)
print("Vetor decimal (ordenado):", vetor_dec)
print("Vetor final:", vetor_final)
