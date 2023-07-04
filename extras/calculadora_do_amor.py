# Calculadora do Amor
# Desafio:
#
# Crie um programa que calcule a compatibilidade entre duas pessoas. O programa deve exibir uma mensagem dependendo da pontuação obtida. Use a função count() para obter a pontuação de cada nome. Use a declaração if para verificar a pontuação e exibir uma mensagem dependendo da pontuação obtida.
#
# Dica: Você pode usar a função count() para obter a pontuação de cada nome. Por exemplo, se o nome for "Ana", a função count() retornará 2, pois a letra "a" aparece duas vezes no nome "Ana".
#
#
#
# resolução:
#

print("### Bem-vindo à Calculadora do Amor! ### \n")
print("Este programa irá calcular a compatibilidade entre você e a pessoa amada. \n")
print("Para isso, digite o seu nome e o nome da pessoa amada. \n")  




name1 = input("Qual o seu nome? \n")
name2 = input("Qual é o nome dele(a)? \n")


combined_names = name1 + name2
lower_names = combined_names.lower()
v = lower_names.count("v")
e = lower_names.count("e")
r = lower_names.count("r")
d = lower_names.count("d")
a = lower_names.count("a")
d = lower_names.count("d")
e = lower_names.count("e")
i = lower_names.count("i")
r = lower_names.count("r")
o = lower_names.count("o")
first_digit = v + e + r + d + a + d + e + i + r + o

a = lower_names.count("a")
m = lower_names.count("m")
o = lower_names.count("o")
r = lower_names.count("r")
second_digit = a + m + o + r

score = int(str(first_digit) + str(second_digit))

print('\n\n.\n.')

if (score <= 49):
  print(f"### Sua pontuação é {score}%, Vocês juntos são como coca e mentos. ###")
elif (score >= 50) and (score <= 90):
  print(f" ### Sua pontuação é {score}%, Vocês são Almas Gêmeas. ###")
else:
  print(f"### Sua pontuação é {score}%. ###")
  

name1 = input("Qual o seu nome? \n")
name2 = input("Qual é o nome dele(a)? \n")


combined_names = name1 + name2
lower_names = combined_names.lower()
v = lower_names.count("v")
e = lower_names.count("e")
r = lower_names.count("r")
d = lower_names.count("d")
a = lower_names.count("a")
d = lower_names.count("d")
e = lower_names.count("e")
i = lower_names.count("i")
r = lower_names.count("r")
o = lower_names.count("o")
first_digit = v + e + r + d + a + d + e + i + r + o

a = lower_names.count("a")
m = lower_names.count("m")
o = lower_names.count("o")
r = lower_names.count("r")
second_digit = a + m + o + r

score = int(str(first_digit) + str(second_digit))

print('\n\n.\n.\n.')

if (score <= 49):
  print(f"### Sua pontuação é {score}%, Vocês juntos são como coca e mentos. ###")
elif (score >= 50) and (score <= 90):
  print(f" ### Sua pontuação é {score}%, Vocês são Almas Gêmeas. ### \n\n")
else:
  print(f"### Sua pontuação é {score}%. ###")

print('\n\n.\n.\n.')
#
#
#
#

# O que foi aprendido:

# Neste projeto, aprendemos a usar a função count() para obter a pontuação de cada nome. Você também aprendeu a usar a declaração if para verificar a pontuação e exibir uma mensagem dependendo da pontuação obtida.
#
# Aprendemos a usar a função lower() para converter os nomes para letras minúsculas. Isso é importante, pois a função count() diferencia letras maiúsculas de letras minúsculas. Por exemplo, a função count() retornará 1 se o nome for "Ana" e 0 se o nome for "ana".
#
# Por fim, aprendemos a usar a função int() para converter a pontuação em um número inteiro. Isso é importante, pois a função count() retorna um número inteiro, mas a função str() retorna uma string. Para usar a função count() para obter a pontuação de cada nome, você precisa converter a pontuação em um número inteiro.
#
# 
#Projeto Desenvolvido por: jB Oliveira para o  #100DaysOfPython
#

  

