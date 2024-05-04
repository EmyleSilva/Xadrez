from tabuleiro import Tabuleiro
from cavalo import Cavalo
from torre import Torre
from bispo import Bispo


class Menu:
    # Atrbutos estáticos da classe
    opcao = 0
    t = Tabuleiro()
    info_peca = [0] * 3  # Armazena as posição_x, posição_y e cor para instanciar as peças
    info_movimento = [0] * 2  # Armazena o destino_x e destino_y para realizar um movimento

    @classmethod
    def ler_opcao(cls, quant_opcoes):
        cls.opcao = int(input("Opção: "))
        while cls.opcao < 1 or cls.opcao > quant_opcoes:
            print("Opção Inválida! Selecione uma opção entre 0 e", quant_opcoes)
            cls.opcao = int(input("Opção: "))

    @staticmethod
    def exibir_menu():
        print("1 - Adicionar Bispo.")
        print("2 - Adicionar Cavalo.")
        print("3 - Adicionar Torre.")
        print("4 - Movimentar Bispo.")
        print("5 - Movimentar Cavalo.")
        print("6 - Movimentar Torre.")
        print("7 - Exibir tabuleiro.")
        print("8 - Sair")

    @classmethod
    def adicionar_peca(cls):
        cls.info_peca[0] = int(input("Informe a posição de origem x: ")) - 1
        cls.info_peca[1] = int(input("Informe a posição de origem Y: ")) - 1
        cls.info_peca[2] = int(input("Informe a cor da peça (1 para 'Branco' ou 2 para 'Preto'): "))

    @classmethod
    def seleciona_cor(cls):
        cor = "Branco"

        if cls.info_peca[2] == 1:
            cor = "Branco"
        elif cls.info_peca[2] == 2:
            cor = "Preto"

        return cor

    @classmethod
    def adicionar_bispo(cls):
        cls.adicionar_peca()
        cor = cls.seleciona_cor()
        b: Bispo = Bispo(cls.info_peca[0], cls.info_peca[1], cor)
        cls.t.bispo = b

    @classmethod
    def adicionar_cavalo(cls):
        cls.adicionar_peca()
        cor = cls.seleciona_cor()
        c: Cavalo = Cavalo(cls.info_peca[0], cls.info_peca[1], cor)
        cls.t.cavalo = c

    @classmethod
    def adicionar_torre(cls):
        cls.adicionar_peca()
        cor = cls.seleciona_cor()
        t1: Torre = Torre(cls.info_peca[0], cls.info_peca[1], cor)
        cls.t.torre = t1

    @classmethod
    def realizar_movimento(cls):
        cls.info_movimento[0] = int(input("Destino_x: ")) - 1
        cls.info_movimento[1] = int(input("Destino_y: ")) - 1

    @classmethod
    def movimentar_bispo(cls):
        cls.realizar_movimento()
        print("Selecione o indice do bispo a ser movimentado: ")
        for bispo in cls.t.bispo:
            print(bispo.indice)
        indice = int(input("Indice: "))
        cls.t.movimentar_bispo(cls.info_movimento[0], cls.info_movimento[1], indice)

    @classmethod
    def movimentar_cavalo(cls):
        cls.realizar_movimento()
        print("Selecione o indice do cavalo a ser movimentado: ")
        for cavalo in cls.t.cavalo:
            print(cavalo.indice)
        indice = int(input("Indice: "))
        cls.t.movimentar_cavalo(cls.info_movimento[0], cls.info_movimento[1], indice)

    @classmethod
    def movimentar_torre(cls):
        cls.realizar_movimento()
        print("Selecione o indice da torre a ser movimentada: ")
        for torre in cls.t.torre:
            print(torre.indice)
        indice = int(input("Indice: "))
        cls.t.movimentar_cavalo(cls.info_movimento[0], cls.info_movimento[1], indice)

    @classmethod
    def exibir_tabuleiro(cls):
        print()
        cls.t.imprimir_tabuleiro()
        print()


# Rotina para o jogo
quantidade_opcoes = 8

while Menu.opcao != quantidade_opcoes:
    Menu.exibir_menu()
    Menu.ler_opcao(quantidade_opcoes)

    if Menu.opcao == 1:
        Menu.adicionar_bispo()
        Menu.exibir_tabuleiro()
    elif Menu.opcao == 2:
        Menu.adicionar_cavalo()
        Menu.exibir_tabuleiro()
    elif Menu.opcao == 3:
        Menu.adicionar_torre()
        Menu.exibir_tabuleiro()
    elif Menu.opcao == 4:
        Menu.movimentar_bispo()
        Menu.exibir_tabuleiro()
    elif Menu.opcao == 5:
        Menu.movimentar_cavalo()
        Menu.exibir_tabuleiro()
    elif Menu.opcao == 6:
        Menu.movimentar_torre()
        Menu.exibir_tabuleiro()
    elif Menu.opcao == 7:
        Menu.exibir_tabuleiro()
    else:
        print("Obrigada por jogar!")
        break

    input("Aperte qualquer tecla para continuar...")
    print()
