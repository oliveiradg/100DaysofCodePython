# O DESAFIO DO DIA 04

# O desafio proposto é criar um jogo de "Tesoura de Papel de Pedra" no qual o jogador joga contra o computador. O objetivo é implementar a lógica do jogo e permitir que o jogador faça uma escolha entre pedra, papel ou tesoura, enquanto o computador faz uma escolha aleatória. Com base nas regras do jogo (pedra ganha da tesoura, tesoura ganha do papel e papel ganha da pedra), o programa deve determinar se o jogador ganhou, perdeu ou houve um empate.

# O desafio é dividido em etapas. Primeiro, é necessário gerar a escolha do jogador através de um input, onde o jogador deve digitar um número correspondente à sua escolha (0 para pedra, 1 para papel ou 2 para tesoura). Em seguida, é gerada a escolha aleatória do computador usando a biblioteca random e a função randint.

# Após obter as escolhas do jogador e do computador, é preciso comparar essas escolhas para determinar o resultado do jogo. São utilizadas declarações if, elif e else para verificar diferentes combinações de escolhas e determinar se o jogador ganhou, perdeu ou empatou.

# Durante a implementação, é importante testar o código à medida que ele é desenvolvido para identificar erros e fazer ajustes necessários. Além disso, é mencionado que é possível lidar com casos de escolhas inválidas dos jogadores, como digitar um número fora do intervalo 0-2.

# O objetivo final é criar um jogo funcional de "Tesoura de Papel de Pedra" que siga as regras do jogo e apresente o resultado corretamente. O desafio encoraja os participantes a pensar em etapas menores para resolver o problema, como gerar um número aleatório ou criar um fluxograma, e a usar os conhecimentos adquiridos anteriormente para completar o desafio.

# Ao finalizar o desafio, o código deve ser testado e verificado em relação ao jogo de "Tesoura de Papel de Pedra" demonstrado na aula. A solução proposta envolve a implementação da lógica do jogo e a consideração de casos especiais, como empates e escolhas inválidas, para garantir o funcionamento correto do programa.


# Solução do desafio do dia 04


# Pedra, Papel e Tesoura
# Instruções
# Faça um jogo de Pedra, Papel e Tesoura contra o computador.
#
# Exemplo de fluxo de jogo:
# 
# 1. Você escolhe Pedra, Papel ou Tesoura?
# > Pedra
# 2. Computador escolhe Papel
# 3. Papel embrulha Pedra. Você perdeu!
#
# Regras:
# - Pedra ganha da Tesoura
# - Tesoura ganha do Papel
# - Papel ganha da Pedra
#   
# Resolução:

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("O que você escolhe? \n\n Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("O Computador escolheu:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("Você digitou um número inválido, você perdeu!") 
elif user_choice == 0 and computer_choice == 2:
  print("Você Venceu")
elif computer_choice == 0 and user_choice == 2:
  print("Você Perdeu")
elif computer_choice > user_choice:
  print("Você Perdeu")
elif user_choice > computer_choice:
  print("Você Venceu")
elif computer_choice == user_choice:
  print("É um empate")


# O que foi aprendido:
# Neste desafio, aprendemos a usar a biblioteca random para gerar números aleatórios e a função randint para gerar um número inteiro aleatório dentro de um intervalo. Também aprendemos a usar listas para armazenar e acessar imagens do jogo e a usar declarações if, elif e else para verificar diferentes combinações de escolhas e determinar o resultado do jogo.    

# O que foi ensinado:
# Neste desafio, aprendemos a usar a biblioteca random para gerar números aleatórios e a função randint para gerar um número inteiro aleatório dentro de um intervalo. Também aprendemos a usar listas para armazenar e acessar imagens do jogo e a usar declarações if, elif e else para verificar diferentes combinações de escolhas e determinar o resultado do jogo.


#Projeto Desenvolvido por: jB Oliveira para o terceiro dia dos #100DaysOfPython
