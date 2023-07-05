# Desenhando um coração na tela
# Fonte: https://www.pythonprogressivo.net/2018/02/Como-desenhar-um-coracao-com-Python.html


# desafio
# desenhar um coração na tela
# usar a biblioteca turtle
# usar a função done() para manter a janela aberta
# usar a função pensize() para definir a espessura da linha
# usar a função color() para definir a cor da linha
# usar a função begin_fill() para iniciar o preenchimento
# usar a função end_fill() para finalizar o preenchimento

#solução

from turtle import *

color('red')
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()
done()


#o que foi aprendido:
# importar biblioteca
# usar funções da biblioteca
# usar funções da biblioteca com parâmetros

# # # #Projeto Desenvolvido por: jB Oliveira para o  #100DaysOfPython