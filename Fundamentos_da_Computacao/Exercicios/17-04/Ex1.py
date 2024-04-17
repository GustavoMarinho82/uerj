pacientes = [] # [[idade, tipo de tratamento, pressao], ...]
maior_menos_30 = 0 # Maior pressão arterial dos menores que 30 anos

while (True):
    idade = int(input("Digite a idade do paciente (Digite uma idade negativa para finalizar o algoritmo): "))
    if (idade < 0):
        break

    tipo_tratamento = input("Digite o tipo de tratamento do paciente: ")
    pressao = int(input("Digite a pressão arterial do paciente: "))

    pacientes.append([idade, tipo_tratamento, pressao])

if (pacientes): #Checa se a lista tem algum elemento
    for [idade, _, pressao] in pacientes:
        if (idade<30) and (pressao>maior_menos_30):
            maior_menos_30 = pressao

    if (maior_menos_30 != 0):
        print(f"A maior pressão entre os pacientes com menos de 30 anos é de: {maior_menos_30}")
    
    else:
        print("Nenhum paciente possui menos de 30 anos")