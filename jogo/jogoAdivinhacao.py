print("****************")
print("Bem vindo ao jogo de Adivinhação")
print("****************")

numero_secreto = 49
chute = input("Digite o numero Secreto: ")


print("Você degitou", chute, sep=' ')

chute = int(chute)

acertou = (chute == numero_secreto)
maior = (chute > numero_secreto)
menor = (chute < numero_secreto)


if (acertou):
    print("Você acertou")
else:
    if(maior):
        print("Seu Chute é maior que o numero secreto")
    elif(menor):
        print("Seu Chute foi menor que o numero secreto")
    
print("Fim de jogo!")