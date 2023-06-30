# Programa em Python com GUI usando o PySimpleGUI





import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        # Layout
        sg.theme('Reddit')
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(15,0), key='nome')],
            [sg.Text('Idade', size=(5,0)), sg.Input(size=(15,0), key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao'), sg.Radio('Não', 'cartoes', key='naoAceitaCartao')],
            [sg.Slider(range=(0,255), default_value=0, orientation='h', size=(15,20), key='sliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,15))]
        ]
        # Janela
        self.janela = sg.Window('Dados do Usuário').layout(layout)
        # Extrair os dados da tela
        

    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            # print(self.values)
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita yahoo: {aceita_yahoo}')
            print(f'aceita cartão: {aceita_cartao}')
            print(f'não aceita cartão: {nao_aceita_cartao}')
            print(f'velocidade script: {velocidade_script}')


tela = TelaPython()
tela.Iniciar()

# # Path: extras\tela.py

# # # #Projeto Desenvolvido por: jB Oliveira para o  #100DaysOfPython