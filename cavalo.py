import peca

class Cavalo(peca.Peca):
    def __init__(self, posicao_origem_x, posicao_origem_y):
        if ((posicao_origem_x == 1 or posicao_origem_x == 6) and (posicao_origem_y == 0 or posicao_origem_y == 7)):
            super().__init__(posicao_origem_x,posicao_origem_y)
        else:
            super().__init__(1,0)
        

    def validar(self, posicao_x, posicao_y):
        if super().validar(posicao_x, posicao_y):
            if (posicao_x == self.posicao_atual_x+2) or (posicao_x == self.posicao_atual_x-2):
                if (posicao_y == self.posicao_atual_y+1) or (posicao_y == self.posicao_atual_y-1):
                    return True
            elif (posicao_y == self.posicao_atual_y+2) or (posicao_y == self.posicao_atual_y-2):
                if (posicao_x == self.posicao_atual_x+1) or (posicao_x == self.posicao_atual_x-1):
                    return True
            return False
                
    def movimentar(self, destino_x, destino_y):
        if self.validar(destino_x, destino_y):
            self.posicao_atual_x = destino_x
            self.posicao_atual_y = destino_y