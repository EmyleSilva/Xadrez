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
        print("4 - Movimentar Bispo.")
        print("5 - Movimentar Cavalo.")
        print("6 - Movimentar Torre.")
        print("7 - Exibir tabuleiro.")
        print("8 - Sair")

    @classmethod
    def adicionar_peca(cls):
        posicao_x = int(input("Informe a posição de origem x: ")) - 1
        posicao_y = int(input("Informe a posição de origem Y: ")) - 1
        cor = int(input("Informe a cor da peça (1 para 'Branco' ou 2 para 'Preto'): "))
        cor = cls.seleciona_cor(cor)

        if cls.opcao == 1:
            cls.t.bispo = Bispo(posicao_x, posicao_y, cor)
        elif cls.opcao == 2:
            cls.t.cavalo = Cavalo(posicao_x, posicao_y, cor)
        else:
            cls.t.torre = Torre(posicao_x, posicao_y, cor)

    @classmethod
    def seleciona_cor(cls, cor_numero):
        if cor_numero == 1:
            return "Branco"
        elif cor_numero == 2:
            return "Preto"

        return "Branco"

    @classmethod
    def valida_recuperacao(cls, tipo):
        print(f'Peça inválida! Não existe {tipo} na posição indicada', end=". ")
        print("Informe uma posição válida!")
        posicao_atual_x = int(input("Posição X: ")) - 1
        posicao_atual_y = int(input("Posição Y: ")) - 1
        return cls.t.matriz_posicao[posicao_atual_x][posicao_atual_y]

    @classmethod
    def recuperar_peca(cls, posicao_atual_x, posicao_atual_y, tipo):
        peca = cls.t.matriz_posicao[posicao_atual_x][posicao_atual_y]

        if tipo == "bispo":
            while not isinstance(peca, Bispo):
                peca = cls.valida_recuperacao(tipo)
            return peca

        if tipo == "cavalo":
            while not isinstance(peca, Cavalo):
                peca = cls.valida_recuperacao(tipo)
            return peca

        while not isinstance(peca, Torre):
            peca = cls.valida_recuperacao(tipo)
        return peca

    @classmethod
    def realizar_movimento(cls):
        if cls.opcao == 4 and len(cls.t.bispo) > 0:
            tipo = "bispo"
        elif cls.opcao == 5 and len(cls.t.cavalo) > 0:
            tipo = "cavalo"
        elif cls.opcao == 6 and len(cls.t.torre) > 0:
            tipo = "torre"
        else:
            print(f"\n\nNão há peça desejada no tabuleiro\n")
            return
        
        print("Informe as coordenadas da peça que você deseja movimentar: ")
        atual_x = int(input("Posição X: ")) - 1
        atual_y = int(input("Posição Y: ")) - 1

        peca = cls.recuperar_peca(atual_x, atual_y, tipo)

        print("Mover a peça para: ")
        destino_x = int(input("Destino X: ")) - 1
        destino_y = int(input("Destino Y: ")) - 1

        if isinstance(peca, Bispo):
            cls.t.movimentar_bispo(destino_x, destino_y, peca.id)
        elif isinstance(peca, Cavalo):
            cls.t.movimentar_cavalo(destino_x, destino_y, peca.id)
        else:
            cls.t.movimentar_torre(destino_x, destino_y, peca.id)

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

    if 1 <= Menu.opcao <= 3:
        Menu.adicionar_peca()
        Menu.exibir_tabuleiro()
    elif 4 <= Menu.opcao <= 6:
        Menu.realizar_movimento()
        Menu.exibir_tabuleiro()
    elif Menu.opcao == 7:
        Menu.exibir_tabuleiro()
    else:
        print("Obrigada por jogar!")
        break

    input("Aperte qualquer tecla para continuar...")
    print()
