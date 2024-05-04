import bispo

class Tabuleiro:
    def __init__(self):
        # Inicializa a matriz de posição com None (ou qualquer valor inicial desejado)
        self._matrizPosicao = [[0 for _ in range(8)] for _ in range(8)]
        self._cavalo = []
        self._bispo = []
        self._torre = []

    @property
    def cavalo(self):
        return self._cavalo

    @cavalo.setter
    def cavalo(self, cavalo):
        if len(self._cavalo) > 3:
            print("Quantidade máxima de cavalos no tabuleiro já foi atingida!")
        else:
            indice = len(self._cavalo)
            self._cavalo.append(cavalo)
            self._cavalo[-1].indice = indice

    @property
    def torre(self):
        return self._torre

    @torre.setter
    def torre(self, torre):
        if len(self._torre) > 3:
            print("Quantidade máxima de torres no tabuleiro já foi atingida!")
        else:
            indice = len(self._torre)
            self._torre.append(torre)
            self._torre[-1].indice = indice

    @property
    def bispo(self):
        return self._bispo

    @bispo.setter
    def bispo(self, bispo):
        if len(self._bispo) > 3:
            print("Quantidade máxima de bispos no tabuleiro já foi atingida!")
        else:
            indice = len(self._bispo)
            self._bispo.append(bispo)
            self._bispo[-1].indice = indice

    def validar_movimentacao(self, destino_x, destino_y, peca):
        if self._matrizPosicao[destino_x][destino_y] == 0:
            print("aqui1")
            return True
        else:
            peca_destino = self._matrizPosicao[destino_x][destino_y]
            if peca_destino.cor == peca.cor:
                print("DESGRAÇAAAAAAAAAAAAAAAAAAA")
                return False
            else:
                print("aqui2")
                peca_destino.estado = False
                return True

    def movimentar_bispo(self, destino_x, destino_y, indice):
        if self._bispo[indice].movimentar(destino_x, destino_y):
            print("Posicao atual bispo 1: ", self._bispo[indice].posicao_atual_x, self._bispo[indice].posicao_atual_y)
            if self.validar_movimentacao(destino_x, destino_y, self._bispo[indice]):
                print("Entra aqui?")
                self._matrizPosicao[destino_x][destino_y] = self._bispo[indice]
        else:
            # Caso o movimento de cavalo seja valido mas o tabuleiro não é livre
            self.bispo[indice].desfazer_movimento()

    def imprimir_tabuleiro(self):
        i = 1
        for linha in self._matrizPosicao:
            i += 1
            print(f"{i}", end=" | ")
            for elemento in linha:
                print(f"{elemento} | ", end=" ")
            print()


b = bispo.Bispo(0, 0, "Branco")
b2 = bispo.Bispo(1, 2, "Preto")
b3 = bispo.Bispo(0, 3, "Branco")
b4 = bispo.Bispo(2, 4, "Preto")
t = Tabuleiro()

t.bispo = b
t.bispo = b2
t.bispo = b3
t.bispo = b4

print(b.indice)
print(b2.indice)
print(b3.indice)
print(b4.indice)

print("Posicao atual bispo 1: ", b.posicao_atual_x, b.posicao_atual_y)
t.movimentar_bispo(1, 2, b.indice)
print("Posicao atual bispo 1: ", b.posicao_atual_x, b.posicao_atual_y)
