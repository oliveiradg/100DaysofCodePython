
# O DESAFIO DO DIA 12:  "Máquina de Café usando POO"

#
# 1. Descrição do projeto:
#    - O projeto consiste em criar uma máquina de café com as seguintes funcionalidades:
#      - Mostrar o menu de bebidas disponíveis.
#      - Receber o pedido do usuário.
#      - Receber o pagamento do usuário.
#      - Verificar se o pagamento é suficiente.
#      - Calcular o troco.
#      - Fazer o café.
#      - Entregar o café e o troco.
#      - Atualizar os recursos disponíveis.
#      - Reiniciar o processo.
#
# 2. Objetivos:
#    - Utilizar POO (Programação Orientada a Objetos) para criar uma máquina de café.
#    - Utilizar classes e métodos para criar uma máquina de café.
#    - Utilizar atributos para criar uma máquina de café.
#    - Utilizar o método construtor "__init__" para criar uma máquina de café.
#    - Utilizar o método "self" para criar uma máquina de café.
#    - Utilizar o método "def" para criar uma máquina de café.
#    - Utilizar o método "return" para criar uma máquina de café.
#    - Utilizar o método "print" para criar uma máquina de café.
#    - Utilizar o método "input" para criar uma máquina de café.
#    - Utilizar o método "if" para criar uma máquina de café.
#    - Utilizar o método "else" para criar uma máquina de café.
#    - Utilizar o método "while" para criar uma máquina de café.
#    - Utilizar o método "for" para criar uma máquina de café.
#    - Utilizar o método "break" para criar uma máquina de café.
#    - Utilizar o método "continue" para criar uma máquina de café.
#    - Utilizar o método "pass" para criar uma máquina de café.



# Solução:

#-----------------------------------------------------------
class MaquinaDeCafe:
    MENU = {
        "1": {"nome": "Café Expresso", "agua": 50, "cafe": 18, "preco": 2.5},
        "2": {"nome": "Café com Leite", "agua": 100, "cafe": 20, "leite": 50, "preco": 3.0},
        "3": {"nome": "Cappuccino", "agua": 100, "cafe": 20, "leite": 50, "preco": 3.5}
    }

    def __init__(self):
        self.agua = 1000  # quantidade de água em ml
        self.cafe = 500  # quantidade de café em gramas
        self.leite = 500  # quantidade de leite em ml
        self.dinheiro = 0  # valor total de dinheiro recebido

    def mostrar_menu(self):
        print("MENU:")
        for opcao, bebida in self.MENU.items():
            print(f"{opcao}. {bebida['nome']} - R${bebida['preco']}")

    def receber_pedido(self):
        while True:
            opcao = input("Digite o número da bebida desejada (ou 'q' para sair): ")
            if opcao == "q":
                break
            bebida = self.MENU.get(opcao)
            if bebida:
                if self.verificar_recursos(bebida):
                    pagamento = self.receber_pagamento(bebida)
                    if pagamento >= bebida["preco"]:
                        troco = pagamento - bebida["preco"]
                        self.dinheiro += bebida["preco"]
                        self.entregar_cafe(bebida)
                        self.atualizar_recursos(bebida)
                        print(f"Troco: R${troco:.2f}")
                    else:
                        print("Pagamento insuficiente. Pedido cancelado.")
                else:
                    print("Recursos insuficientes. Pedido cancelado.")
            else:
                print("Opção inválida. Tente novamente.")

    def verificar_recursos(self, bebida):
        if self.agua >= bebida.get("agua", 0) and self.cafe >= bebida.get("cafe", 0) and self.leite >= bebida.get("leite", 0):
            return True
        return False

    def receber_pagamento(self, bebida):
        while True:
            pagamento = float(input(f"Insira o valor de R${bebida['preco']}: "))
            if pagamento >= bebida["preco"]:
                return pagamento
            else:
                print("Valor insuficiente. Tente novamente.")

    def entregar_cafe(self, bebida):
        print(f"Preparando {bebida['nome']}...")
        print("Café pronto! Aproveite.")

    def atualizar_recursos(self, bebida):
        self.agua -= bebida.get("agua", 0)
        self.cafe -= bebida.get("cafe", 0)
        self.leite -= bebida.get("leite", 0)

    def reiniciar_processo(self):
        self.dinheiro = 0

    def iniciar_maquina(self):
        while True:
            print("\nMÁQUINA DE CAFÉ")
            print("Selecione uma opção:")
            print("1. Fazer pedido")
            print("2. Mostrar dinheiro arrecadado")
            print("3. Reiniciar máquina")
            print("4. Sair")
            opcao = input("Digite o número da opção desejada: ")

            if opcao == "1":
                self.mostrar_menu()
                self.receber_pedido()
            elif opcao == "2":
                print(f"Dinheiro arrecadado: R${self.dinheiro:.2f}")
            elif opcao == "3":
                self.reiniciar_processo()
                print("Máquina reiniciada.")
            elif opcao == "4":
                break
            else:
                print("Opção inválida. Tente novamente.")


# Exemplo de uso
maquina = MaquinaDeCafe()
maquina.iniciar_maquina()



#-----------------------------------------------------------
# Neste código, a classe MaquinaDeCafe representa a máquina de café e possui métodos para cada etapa do processo, como mostrar o menu, receber o pedido, receber o pagamento, entregar o café, atualizar os recursos, reiniciar o processo e iniciar a máquina.

# A máquina de café possui um menu pré-definido no atributo MENU, contendo as bebidas disponíveis com seus respectivos ingredientes e preços. O usuário pode escolher uma bebida pelo número do menu e realizar o pedido. A máquina verifica se há recursos suficientes e se o pagamento é suficiente para concluir o pedido, entregando o café e o troco, se necessário.

# O método iniciar_maquina() permite ao usuário interagir com a máquina, escolhendo opções como fazer um pedido, mostrar o dinheiro arrecadado, reiniciar a máquina ou sair do programa.



#Projeto Desenvolvido com ❤ por: jB Oliveira para os #100DaysOfPython