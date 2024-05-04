import peca


class Cavalo(peca.Peca):
    def __init__(self, posicao_origem_x, posicao_origem_y, cor):
        super().__init__(posicao_origem_x,posicao_origem_y, cor)
        

    def validar(self, posicao_x, posicao_y):
        if super().validar(posicao_x, posicao_y):
            if (posicao_x == self._posicao_atual_x+2) or (posicao_x == self._posicao_atual_x-2):
                if (posicao_y == self._posicao_atual_y+1) or (posicao_y == self._posicao_atual_y-1):
                    return True
            elif (posicao_y == self._posicao_atual_y+2) or (posicao_y == self._posicao_atual_y-2):
                if (posicao_x == self._posicao_atual_x+1) or (posicao_x == self._posicao_atual_x-1):
                    return True
            return False
                
    def movimentar(self, destino_x, destino_y):
        if self.validar(destino_x, destino_y):
            self._posicao_origem_x = self._posicao_atual_x
            self._posicao_origem_y = self._posicao_atual_y
            self._posicao_atual_x = destino_x
            self._posicao_atual_y = destino_y
            return True
        return False