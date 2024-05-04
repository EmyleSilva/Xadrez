import bispo
import cavalo
import torre
import emoji

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
            self._matrizPosicao[cavalo.posicao_atual_x][cavalo.posicao_atual_y] = cavalo

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
            self._matrizPosicao[torre.posicao_atual_x][torre.posicao_atual_y] = torre

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
            self._matrizPosicao[bispo.posicao_atual_x][bispo.posicao_atual_y] = bispo

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

    def movimentar_bispo(self, destino_x, destino_y, indice):
        if self._bispo[indice].movimentar(destino_x, destino_y):
            if self.validar_movimentacao(destino_x, destino_y, self._bispo[indice]):
                self._matrizPosicao[destino_x][destino_y] = self._bispo[indice]
                self._matrizPosicao[self._bispo[indice].posicao_origem_x][self._bispo[indice].posicao_origem_y] = 0
                return
        # Caso o movimento de cavalo seja valido mas o tabuleiro não é livre
        print("Movimento inválido!")
        self.bispo[indice].desfazer_movimento()

    def movimentar_cavalo(self, destino_x, destino_y, indice):
        if self._cavalo[indice].movimentar(destino_x, destino_y):
            if self.validar_movimentacao(destino_x, destino_y, self._cavalo[indice]):
                self._matrizPosicao[destino_x][destino_y] = self._cavalo[indice]
                self._matrizPosicao[self._cavalo[indice].posicao_origem_x][self._cavalo[indice].posicao_origem_y] = 0
                return
            
        # Caso o movimento de cavalo seja valido mas o tabuleiro não é livre
        print("Movimento inválido!")
        self.cavalo[indice].desfazer_movimento()

    def movimentar_torre(self, destino_x, destino_y, indice):
        if self._torre[indice].movimentar(destino_x, destino_y):
            if self.validar_movimentacao(destino_x, destino_y, self._torre[indice]):
                self._matrizPosicao[destino_x][destino_y] = self._torre[indice]
                self._matrizPosicao[self._torre[indice].posicao_origem_x][self._torre[indice].posicao_origem_y] = 0
                return
            # Caso o movimento de cavalo seja valido mas o tabuleiro não é livre
        print("Movimento inválido!")
        self.torre[indice].desfazer_movimento()

    def verificaTipo(self, elemento):
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
        for i in range(len(self._bispo)):
            if self._bispo[i].estado == False and self._bispo[i].cor == cor:
                print(f"{self.verificaTipo(self._bispo[i])}", end="")
        for i in range(len(self._torre)):
            if self._torre[i].estado == False and self._torre[i].cor == cor:
                print(f"{self.verificaTipo(self._torre[i])}", end="")
        for i in range(len(self._cavalo)):
            if self._cavalo[i].estado == False and self._cavalo[i].cor == cor:
                print(f"{self.verificaTipo(self._cavalo[i])}", end="")
        print()

    def imprimir_tabuleiro(self):
        i = 0
        self.capturados("Preto")
        for linha in self._matrizPosicao:
            i += 1
            print(f"{i}", end=" | ")
            for elemento in linha: 
                print(f"{self.verificaTipo(elemento)}", end=" |")
            print()
        
        self.capturados("Branco")
        print()


b = bispo.Bispo(0, 0, "Branco")
b2 = bispo.Bispo(2, 4, "Branco")
b3 = bispo.Bispo(0, 3, "Branco")
b4 = bispo.Bispo(5, 5, "Preto")
t = Tabuleiro()

t.bispo = b
t.bispo = b2
t.bispo = b3
t.bispo = b4

t1 = torre.Torre(1,2,"Branco")
t.torre = t1
t2 = torre.Torre(2,3,"Preto")
t.torre = t2

c = cavalo.Cavalo(3,2, "Preto")
t.cavalo = c

t.movimentar_torre(2, 6, t2.indice)
t.imprimir_tabuleiro()