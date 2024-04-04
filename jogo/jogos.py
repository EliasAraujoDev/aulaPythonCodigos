import jogoforca
import jogoAdivinhacao

print("****************")
print("Escolha O seu jogo")
print("**************** \n")

print("(1)forca (2) Adivinhação\n")

jogo = int(input("Qual Jogo você quer jogar:"))

if (jogo == 1):
    print("Jogo da Forca\n")
    jogoforca.jogar()
elif(jogo == 2): 
    print("Jogo de adivinhação.\n")
    jogoAdivinhacao.jogar()

