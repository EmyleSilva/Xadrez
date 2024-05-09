import bispo
import cavalo
import torre


class Tabuleiro:
    def __init__(self):
        # Inicializa a matriz de posição com None (ou qualquer valor inicial desejado)
        self._matrizPosicao = [[0 for _ in range(8)] for _ in range(8)]
        self._pecas = []

    @property
    def matriz_posicao(self):
        return self._matrizPosicao

    @property
    def pecas(self):
        return self._pecas

    @pecas.setter
    def pecas(self, peca):
        indice = len(self._pecas)
        self._pecas.append(peca)
        self._pecas[-1].id = indice
        self._matrizPosicao[peca.posicao_atual_x][peca.posicao_atual_y] = peca

    def validar_movimentacao(self, destino_x, destino_y, peca):
        if self._matrizPosicao[destino_x][destino_y] == 0:
            return True
        else:
            peca_destino = self._matrizPosicao[destino_x][destino_y]
            if peca_destino.cor == peca.cor:
                return False
            else:
                peca_destino.mudar_estado()
                return True

    def movimentar_peca(self, destino_x, destino_y, indice):
        if self._pecas[indice].movimentar(destino_x, destino_y):
            if self.validar_movimentacao(destino_x, destino_y, self._pecas[indice]):
                self._matrizPosicao[destino_x][destino_y] = self._pecas[indice]
                self._matrizPosicao[self._pecas[indice].posicao_origem_x][self._pecas[indice].posicao_origem_y] = 0 # TODO: Verificar porque não apaga a ocorrência no tabuleiro
            return
        # Caso o movimento da peça seja válido mas o tabuleiro na posição de destino não é livre
        print("Movimento Inválido!")
        self._pecas[indice].desfazer_movimento()

    @staticmethod
    def verifica_tipo(elemento):
        if elemento == 0:
            return " \U000025FD "
        else:
            if isinstance(elemento, cavalo.Cavalo):
                if elemento.cor == "Branco":
                    return " \U00002658  "
                else:
                    return " \U0000265E  "
            elif isinstance(elemento, bispo.Bispo):
                if elemento.cor == "Branco":
                    return " \U00002657  "
                else:
                    return " \U0000265D  "
            elif isinstance(elemento, torre.Torre):
                if elemento.cor == "Branco":
                    return " \U00002656  "
                else:
                    return " \U0000265C  "

    def capturados(self, cor):
        for i in range(len(self._pecas)):
            if self._pecas[i].estado is False and self._pecas[i].cor == cor:
                print(f"{self.verifica_tipo(self._pecas[i])}", end="")
        print()

    def imprimir_tabuleiro(self):
        i = 0
        print("  |  1   |  2  |  3  |  4  |  5  |  6  |  7   |  8   |")
        self.capturados("Preto")
        for linha in self._matrizPosicao:
            i += 1
            print(f"{i}", end=" | ")
            for elemento in linha:
                print(f"{self.verifica_tipo(elemento)}", end=" |")
            print()

        self.capturados("Branco")
        print()
