# O DESAFIO DO DIA 03

# Ilha do Tesouro
# Instruções
# Faça seu próprio jogo "Escolha sua própria aventura". Use condicionais como if, elsee elifinstruções para definir a lógica e o caminho da história em seu programa.

# Para escrever seu código de acordo com minha história, você pode usar este fluxograma do draw.io para ajudá-lo.

# No entanto, acho que a parte divertida é escrever sua própria história 😊

# 🧞‍♂️ 🐊 🧙‍♂️ 🧟 🧚‍♂️ 🧝‍♂️ 🥷 🤖 👽 🙀

# Dito isso, se você quiser continuar com meu exemplo, sinta-se à vontade para usar os trechos de texto abaixo...

# Trechos de texto do meu exemplo
# 'Você está em uma encruzilhada. Onde você quer ir? Digite "esquerda" ou "direita"'
# 'Você veio a um lago. Há uma ilha no meio do lago. Digite "wait" para aguardar um barco. Digite "swim" para atravessar a nado.'
# "Você chega ileso na ilha. Há uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. Qual cor você escolhe?"
# "É uma sala cheia de fogo. Game Over."
# "Você encontrou o tesouro! Você ganhou!"
# "Você entra em uma sala de bestas. Game Over."
# "Você escolheu uma porta que não existe. Game Over."
# "Você é atacado por uma truta furiosa. Fim de jogo."
# "Você caiu em um buraco. Fim de jogo."
# Caracteres de escape
# Se você quiser usar vários conjuntos de aspas dentro de uma única string, talvez seja necessário "escapar" alguns deles usando a barra invertida \. Você pode ver isso na minha primeira frase: 'Você está em uma encruzilhada...'. Mais sobre como escapar de personagens aqui.

# Extensões
# Pense em como você pode escrever seu programa para tornar as respostas de um jogador menos sensíveis a maiúsculas e minúsculas. Em outras palavras, seu código deve funcionar independentemente de o usuário responder "esquerda" ou "esquerda".

# Você também pode adicionar sua própria arte ASCII . Apenas lembre-se de adicionar três aspas simples '''no início e no final de sua arte para transformá-la em uma string de várias linhas.



# Solução:
# Entrada:
# 1. Você está em uma encruzilhada. Onde você quer ir? Digite "esquerda" ou "direita"
# 2. Você veio a um lago. Há uma ilha no meio do lago. Digite "wait" para aguardar um barco. Digite "swim" para atravessar a nado.
# 3. Você chega ileso na ilha. Há uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. Qual cor você escolhe?
# 4. É uma sala cheia de fogo. Game Over.
# 5. Você encontrou o tesouro! Você ganhou!
# 6. Você entra em uma sala de bestas. Game Over.
# 7. Você escolheu uma porta que não existe. Game Over.
# 8. Você é atacado por uma truta furiosa. Fim de jogo.
# 9. Você caiu em um buraco. Fim de jogo.
# Saída:
# 1. Você está em uma encruzilhada. Onde você quer ir? Digite "esquerda" ou "direita"
# 2. Você veio a um lago. Há uma ilha no meio do lago. Digite "wait" para aguardar um barco. Digite "swim" para atravessar a nado.
# 3. Você chega ileso na ilha. Há uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. Qual cor você escolhe?
# 4. É uma sala cheia de fogo. Game Over.
# 5. Você encontrou o tesouro! Você ganhou!
# 6. Você entra em uma sala de bestas. Game Over.
# 7. Você escolheu uma porta que não existe. Game Over.
# 8. Você é atacado por uma truta furiosa. Fim de jogo.
# 9. Você caiu em um buraco. Fim de jogo.

#code:

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Bem vindo a Ilha do Tesouro.")
print("Sua missão é encontrar o tesouro.")
direcao = input("Você está em uma encruzilhada. Onde você quer ir? Digite 'esquerda' ou 'direita'\n").lower()
if direcao == "esquerda":
    lago = input("Você veio a um lago. Há uma ilha no meio do lago. Digite 'esperar' para aguardar um barco. Digite 'nadar' para atravessar a nado.\n").lower()
    if lago == "esperar":
        porta = input("Você chega ileso na ilha. Há uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. Qual cor você escolhe?\n").lower()
        if porta == "amarela":
            print("Você encontrou o tesouro! Você ganhou!")
        elif porta == "vermelha":
            print("É uma sala cheia de fogo. Game Over.")
        elif porta == "azul":
            print("Você entra em uma sala de bestas. Game Over.")
        else:
            print("Você escolheu uma porta que não existe. Game Over.")
    else:
        print("Você é atacado por uma truta furiosa. Fim de jogo.")
else:
    print("Você caiu em um buraco. Fim de jogo.")

##########################


#Projeto Desenvolvido por: jB Oliveira para o terceiro dia dos #100DaysOfPython