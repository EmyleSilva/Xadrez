class Peca:
    def __init__(self, posicao_origem_x, posicao_origem_y):
        self.posicao_origem_x = posicao_origem_x
        self.posicao_origem_y = posicao_origem_y
        self.posicao_atual_x = posicao_origem_x
        self.posicao_atual_y = posicao_origem_y

    def validar(self, posicao_x, posicao_y):
        if (posicao_x > 7 or posicao_x < 0) or (posicao_y > 7 or posicao_y < 0):
            return False
        return True

    def movimentar(self, destino_x, destino_y):
        if self.validar(destino_x, destino_y):
            self.posicao_atual_x = destino_x
            self.posicao_atual_y = destino_y
