# Ordenar um vetor de binários usando selection sort
# Convertendo e desconvertendo de binário para decimal

# FUNÇÕES ===========================================================#
def bin_para_dec(n_bin):
    n_dec = 0
    
    for x in range((len(n_bin)-1), -1, -1):
        if (n_bin[x] == "1"):
            n_dec += 2**(len(n_bin) - int(x) - 1)
            
    return n_dec
    
def dec_para_bin(n_dec):
    n_bin = ""
    
    while (n_dec != 0):
        n_bin += str(n_dec % 2)
        n_dec //= 2
    
    return n_bin[::-1]
    
def selection_sort_caseiro(vetor):
    for x in range(0, len(vetor)):
        index_menor = x
    
        for y in range(x+1, len(vetor)):
            if(vetor[y] < vetor[index_menor]):
                index_menor = y
    
        valor_auxliar = vetor[x]
        vetor[x] = vetor[index_menor]
        vetor[index_menor] = valor_auxliar
#====================================================================#

vetor_bin = ["101", "010", "110", "100", "001", "111", "011"]
vetor_dec = [0]*7
vetor_final = [""]*7

for x in range(0, len(vetor_bin)):
    vetor_dec[x] = bin_para_dec(vetor_bin[x])
    
selection_sort_caseiro(vetor_dec)

for x in range(0, len(vetor_bin)):
    vetor_final[x] = "{:>03}".format(dec_para_bin(vetor_dec[x]))
    
print("Vetor binário:", vetor_bin)
print("Vetor decimal (ordenado):", vetor_dec)
print("Vetor final:", vetor_final)
