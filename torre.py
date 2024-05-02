import peca

class Torre(peca.Peca):
   def __init__(self, posicao_origem_x, posicao_origem_y, cor):
       super().__init__(posicao_origem_x, posicao_origem_y, cor)



   def validar(self, posicao_x, posicao_y):
       if super().validar(posicao_x, posicao_y):
           if (posicao_x != self.posicao_atual_x ) and (posicao_y != self.posicao_atual_y):
             return False

           if((posicao_x== self.posicao_atual_x or posicao_y== self.posicao_atual_y) and
             (posicao_x!= self.posicao_atual_x or posicao_y!= self.posicao_atual_y)):

            return True


   def movimentar(self, destino_x, destino_y):

           if self.validar(destino_x, destino_y):
               self._posicao_atual_x= destino_x
               self._posicao_atual_y= destino_y
               return True
           return False

