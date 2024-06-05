# Função recursiva pra converter de decimal para binário

def conversao_dec_bin(n):
    if (n == 0):
        return "0"
    else:
        return int(str(conversao_dec_bin(n//2)) + str(n%2))


print(conversao_dec_bin(13))
