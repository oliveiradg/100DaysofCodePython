# O DESAFIO DO DIA 05:  "PyPassword Generator"

# 1. Descrição do projeto:
#    - O projeto consiste em criar um gerador de senhas chamado "PyPassword Generator".
#    - O programa solicita ao usuário a quantidade de letras, símbolos e números desejados na senha.

# 2. Níveis do projeto:
#    - Nível fácil:
#      - A senha é gerada em sequência, primeiro as letras, depois os símbolos e por último os números.
#    - Nível difícil:
#      - A ordem dos caracteres é completamente aleatória, intercalando letras, símbolos e números.

# 3. Componentes fornecidos:
#    - Uma lista de letras maiúsculas e minúsculas.
#    - Uma lista de números.
#    - Uma lista de símbolos comumente usados em senhas.
#    - Inputs para receber a quantidade desejada de letras, símbolos e números.

# 4. Implementação do nível fácil:
#    - Utilização de um loop "for" para percorrer a quantidade desejada de letras, símbolos e números.
#    - Utilização da função "random.choice()" para escolher um caractere aleatório da lista correspondente.
#    - Concatenação dos caracteres selecionados para formar a senha final.

# 5. Implementação do nível difícil:
#    - Aleatoriedade na ordem dos caracteres, intercalando letras, símbolos e números.
#    - Necessidade de pesquisa adicional para implementar essa aleatoriedade.

# 6. Sugestões de abordagem:
#    - Iniciar pelo nível fácil e depois avançar para o nível difícil.
#    - Experimentar o código, testar diferentes quantidades de letras, símbolos e números.
#    - Buscar informações adicionais quando necessário para implementar a aleatoriedade no nível difícil.

# Esse resumo por tópicos abrange os principais aspectos do projeto final "PyPassword Generator". Ele envolve a geração de senhas aleatórias com base nas quantidades informadas pelo usuário, utilizando loops, a função "random.choice()" e a concatenação de strings.

# SOLUÇÃO:
# Nível fácil:
# 1. Importar o módulo "random".
import random
# 2. Criar uma lista com as letras maiúsculas e minúsculas.
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
            "J", "K", "L", "M", "N", "O", "P", "Q", "R",
            "S", "T", "U", "V", "W", "X", "Y", "Z", "a",
            "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s",
            "t", "u", "v", "w", "x", "y", "z"]
# 3. Criar uma lista com os números.
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# 4. Criar uma lista com os símbolos.
simbolos = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
# 5. Solicitar ao usuário a quantidade de letras, símbolos e números desejados.
print("Bem-vindo ao PyPassword Generator!")
nr_letras = int(input("Quantas letras você deseja na sua senha?\n"))
nr_simbolos = int(input(f"Quantos símbolos você deseja na sua senha?\n"))
nr_numeros = int(input(f"Quantos números você deseja na sua senha?\n"))
# 6. Criar uma variável para armazenar a senha.
senha = ""
# 7. Utilizar um loop "for" para percorrer a quantidade desejada de letras, símbolos e números.
for letra in range(1, nr_letras + 1):
    # 8. Utilizar a função "random.choice()" para escolher um caractere aleatório da lista correspondente.
    senha += random.choice(letras)
for simbolo in range(1, nr_simbolos + 1):
    senha += random.choice(simbolos)
for numero in range(1, nr_numeros + 1):
    senha += random.choice(numeros)
# 9. Exibir a senha gerada.
print(f"Sua senha é: {senha}")


#Projeto Desenvolvido com ❤ por: jB Oliveira para o Quinto dia dos #100DaysOfPython
