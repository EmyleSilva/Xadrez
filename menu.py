from tabuleiro import Tabuleiro
from cavalo import Cavalo
from torre import Torre
from bispo import Bispo


class Menu:
    # Atrbutos estáticos da classe
    opcao = 0
    t = Tabuleiro()

    @classmethod
    def ler_opcao(cls, quant_opcoes):
        cls.opcao = int(input("Opção: "))
        while cls.opcao < 1 or cls.opcao > quant_opcoes:
            print(f"Opção Inválida! Selecione uma opção entre 0 e {quant_opcoes}.")
            cls.opcao = int(input("Opção: "))

    @staticmethod
    def exibir_menu():
        print("1 - Adicionar Bispo.")
        print("2 - Adicionar Cavalo.")
        print("3 - Adicionar Torre.")
        print("4 - Movimentar Peça.")
        print("5 - Exibir tabuleiro.")
        print("6 - Sair")

    @classmethod
    def adicionar_peca(cls):
        posicao_x = int(input("Informe a posição de origem x: ")) - 1
        posicao_y = int(input("Informe a posição de origem Y: ")) - 1
        cor = int(input("Informe a cor da peça (1 para 'Branco' ou 2 para 'Preto'): "))
        cor = cls.seleciona_cor(cor)

        if cls.opcao == 1:
            cls.t.pecas = Bispo(posicao_x, posicao_y, cor)
        elif cls.opcao == 2:
            cls.t.pecas = Cavalo(posicao_x, posicao_y, cor)
        else:
            cls.t.pecas = Torre(posicao_x, posicao_y, cor)

    @classmethod
    def seleciona_cor(cls, cor_numero):
        if cor_numero == 1:
            return "Branco"
        elif cor_numero == 2:
            return "Preto"

        return "Branco"

    @classmethod
    def recuperar_peca(cls, posicao_atual_x, posicao_atual_y):
        peca = cls.t.matriz_posicao[posicao_atual_x][posicao_atual_y]

        while peca == 0:
            print("Posição Inválida! Não existe peça na posição indicada", end=". ")
            print("Informe uma posição válida!")
            posicao_atual_x = int(input("Posição X: ")) - 1
            posicao_atual_y = int(input("Posição Y: ")) - 1
            peca = cls.t.matriz_posicao[posicao_atual_x][posicao_atual_y]
        return peca

    @classmethod
    def realizar_movimento(cls):
        print("Informe as coordenadas da peça que você deseja movimentar: ")
        atual_x = int(input("Posição X: ")) - 1
        atual_y = int(input("Posição Y: ")) - 1

        peca = cls.recuperar_peca(atual_x, atual_y)

        print("Mover a peça para: ")
        destino_x = int(input("Destino X: ")) - 1
        destino_y = int(input("Destino Y: ")) - 1

        cls.t.movimentar_peca(destino_x, destino_y, peca.id)


    @classmethod
    def exibir_tabuleiro(cls):
        print()
        cls.t.imprimir_tabuleiro()
        print()


# Rotina para o jogo
quantidade_opcoes = 6

while Menu.opcao != quantidade_opcoes:
    Menu.exibir_menu()
    Menu.ler_opcao(quantidade_opcoes)

    if 1 <= Menu.opcao <= 3:
        Menu.adicionar_peca()
        Menu.exibir_tabuleiro()
    elif Menu.opcao == 4:
        Menu.realizar_movimento()
        Menu.exibir_tabuleiro()
    elif Menu.opcao == 5:
        Menu.exibir_tabuleiro()
    else:
        print("Obrigada por jogar!")
        break

    input("Aperte qualquer tecla para continuar...")
    print()