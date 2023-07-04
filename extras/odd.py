
#Desafio :

# Crie um programa que exiba uma mensagem dependendo da hora do dia. O programa deve exibir a mensagem:
#
# Este minuto pode ser um pouco azarado
# Este é um minuto da sorte!
# dependendo se o minuto atual é um número ímpar ou par. Use a função datetime.today() para obter a data e hora atuais e a função minute() para obter o minuto atual. Use a declaração if para verificar se o minuto atual é um número ímpar e a declaração else para exibir uma mensagem se o minuto atual não for um número ímpar.
#




from datetime import datetime

odds = [
    1, 3, 5, 7, 9, 11, 
    13, 15, 17, 19, 21,
    23, 25, 27, 29, 31,
    33, 35, 37, 39, 41,
    43, 45, 47, 49, 51,
    53, 55, 57, 59
]

right_this_minute = datetime.today().minute
if right_this_minute in odds :
    print('Este minuto pode ser um pouco azarado')
else :
    print('Este é um minuto da sorte!')    


    # Explicação:
    #
    # A função datetime.today() retorna um objeto datetime com a data e hora atuais.
    # A função minute() retorna o minuto atual do objeto datetime.
    # A função print() exibe o texto na tela.
    # A função in verifica se o valor da variável right_this_minute está na lista odds.
    # A lista odds contém os números ímpares de 1 a 59.
    # A declaração if verifica se o valor da variável right_this_minute está na lista odds.
    # A declaração else é executada se o valor da variável right_this_minute não estiver na lista odds.
   
    # O que esse programa faz:
    #
    # O programa verifica se o minuto atual é um número ímpar. Se for, o programa exibe a mensagem Este minuto pode ser um pouco azarado. Se não for, o programa exibe a mensagem Não é um minuto estranho.
    # Dependendo da hora do dia, você pode ver a mensagem:
    #
    # Este minuto pode ser um pouco azarado
    # Este é um minuto da sorte!

    # o que foi aprendido:
    #
    # Neste desafio, aprendemos a usar a função datetime.today() para obter a data e hora atuais e a função minute() para obter o minuto atual. Também aprendemos a usar a declaração if para verificar se o minuto atual é um número ímpar e a declaração else para exibir uma mensagem se o minuto atual não for um número ímpar.
    #
    # 