from random import randint

print('Boas vindas ao jogo do número secreto')

numero_secreto = randint(1, 10)
print(numero_secreto)
chute = None
tentativas = 1

while chute != numero_secreto:
    chute = int(input('Escolha um número entre 1 e 10:\n'))
    if chute == numero_secreto:
        break
    else:
        if chute > numero_secreto:
            print(f'O número secreto é menor que {chute}')
        else:
            print(f'O número secreto é maior que {chute}')
            
        tentativas+=1


palavra_correta = 'tentativas' if tentativas > 1  else 'tentativa'
print(f'Isso aí!!! Você descobriu o número secreto {numero_secreto} com {tentativas} {palavra_correta}')