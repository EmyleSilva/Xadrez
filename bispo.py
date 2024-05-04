import peca


class Bispo(peca.Peca):
    def __init__(self, posicao_origem_x, posicao_origem_y, cor):
        super().__init__(posicao_origem_x, posicao_origem_y, cor)

    def validar(self, posicao_x, posicao_y):
        if (posicao_x == self._posicao_atual_x) or (posicao_y == self._posicao_atual_y):
            return False
        if abs(posicao_y - self._posicao_atual_y) != abs(posicao_x - self._posicao_atual_x):
            return False
        return True

    def movimentar(self, destino_x, destino_y):
        if super().validar(destino_x, destino_y):
            if self.validar(destino_x, destino_y):
                print("Validar.... True")
                self._posicao_origem_x = self._posicao_atual_x
                self._posicao_origem_y = self._posicao_atual_y
                self._posicao_atual_x = destino_x
                self._posicao_atual_y = destino_y
                return True
            return False

    def desfazer_movimento(self):
        self._posicao_atual_x = self._posicao_origem_x
        self._posicao_atual_y = self._posicao_origem_y
