import random

def jogar():
    print("****************")
    print("Bem vindo ao jogo de Adivinhação")
    print("**************** \n")

    numero_secreto = round(random.randrange(1, 101))
    tentativas = 0
    pontos = 1000
    rodada = 1
    nivel = 0


    print("Qual nivel de dificuldade?")
    print("Nivel (1) Fácil | (2) Médio | (3) Díficil \n")

    while True:
        nivel = int(input("Defina um nivel: "))
        if nivel >= 1 and nivel <= 3 :
            break
        else: 
            print("Escolha um nivel entre 1,2 e 3")
            

    if(nivel == 1):
        tentativas = 28
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas +1) :
        print("Tentativas: {} de {}. \n".format(rodada,tentativas))
        print(f"Você tem {pontos}")
        chute = input("Digite o numero Secreto: ")
        
        print("Você degitou", chute, sep=' ')

        chute = int(chute)

        acertou = (chute == numero_secreto)
        maior = (chute > numero_secreto)
        menor = (chute < numero_secreto)   
        if (chute < 1) or (chute > 100 ):
            
            print('Você deve deve jogar os numeros 1 a 100')
            continue


        if (acertou):
            print("Você acertou e fez {} pontos".format(pontos))   
            print("Fim de jogo!") 
            break 
        else:
            if(maior):
                print("Seu Chute é maior que o numero secreto")
            elif(menor):
                print("Seu Chute foi menor que o numero secreto")
                pontos_perdidos = numero_secreto - chute
                pontos = int(abs(pontos - pontos_perdidos))
                
        
    rodada ++1 
    
if(__name__) == "__main__":    
    jogar()
