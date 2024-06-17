# Escreva uma função que recebe 2 números inteiros e 1 operador. A função deve funcionar como uma calculadora e realizar a operação. 
# Se ocorrer divisão por zero, utilize try, except e finally.

def calcular(n1, n2, operador):
    try:
        match operador:
            case "+": resultado = (n1 + n2)
            case "-": resultado = (n1 - n2)
            case "*" | "x": resultado = (n1 * n2)
            case "/": resultado = (n1 / n2)
            case "//": resultado = (n1 // n2)
            case _: resultado = 0
    except:
        print("ERRO: Divisão por zero!")
        resultado = 0
        
    finally:
        return resultado
    
    
print("2 + 3 =", calcular(2, 3, "+"))
print("2 - 3 =", calcular(2, 3, "-"))
print("2 * 3 =", calcular(2, 3, "*"))
print("2 / 3 =", calcular(2, 3, "/"))
print("5 // 3 =", calcular(5, 2, "//"))

print("1 / 0 =", calcular(1, 0, "/"))