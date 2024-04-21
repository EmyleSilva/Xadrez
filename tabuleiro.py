class Tabuleiro:
    def __init__(self, cavalo, bispo, torre):
        # Inicializa a matriz de posição com None (ou qualquer valor inicial desejado)
        self.matrizPosicao = [[0 for _ in range(8)] for _ in range(8)]
        self.cavalo = cavalo
        self.bispo = bispo
        self.torre = torre

    def atualizar_posicao(self):
        linha_atual = self.cavalo.posicao_linha
        coluna_atual = self.cavalo.posicao_coluna
        self.matrizPosicao[linha_atual][coluna_atual] = 'C'

    def imprimir_tabuleiro(self):
        i = 1
        for linha in self.matrizPosicao:
            i+=1
            print(f"{i}", end=" | ")
            for elemento in linha:
                print(f"{elemento} | ", end=" ")
            print()
