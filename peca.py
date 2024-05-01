class Peca:
    def __init__(self, posicao_origem_x, posicao_origem_y, cor):
        self._posicao_origem_x = posicao_origem_x
        self._posicao_origem_y = posicao_origem_y
        self._posicao_atual_x = posicao_origem_x
        self._posicao_atual_y = posicao_origem_y
        self._cor = cor
        # O estado indica se a peça ainda está no tabuleiro (True) ou se foi capturada (False)
        self._estado = True

    @property
    def posicao_origem_x(self):
        return self._posicao_origem_x

    @property
    def posicao_origem_y(self):
        return self._posicao_origem_y

    @property
    def posicao_atual_x(self):
        return self._posicao_atual_x
    
    @property
    def posicao_atual_y(self):
        return self._posicao_atual_y

    @property
    def cor(self):
        return self._cor

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        if estado is True or estado is False:
            self._estado = estado
        else:
            raise ValueError(" O estado da peça deve ser 'True' ou 'False' ")

    def validar(self, posicao_x, posicao_y):
        if (posicao_x > 7 or posicao_x < 0) or (posicao_y > 7 or posicao_y < 0):
            return False
        return True

    def movimentar(self, destino_x, destino_y):
        if self.validar(destino_x, destino_y):
            self._posicao_atual_x = destino_x
            self._posicao_atual_y = destino_y
            return True
        return False
