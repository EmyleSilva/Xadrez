import peca

class Torre(peca.Peca):
   def __init__(self, posicao_origem_x, posicao_origem_y):
       #Fazer verificação da posicao_de_origem
       if(posicao_origem_x==0 and posicao_origem_y==7) or (posicao_origem_x==0 or posicao_origem_y == 0) :
         super().__init__(posicao_origem_x, posicao_origem_y)
       elif(posicao_origem_x==7 and posicao_origem_y==0) or (posicao_origem_x==7 and posicao_origem_y==7):
           super().__init__(posicao_origem_x, posicao_origem_y)
       else:
           super().__init__(0,0)


   def validar(self, posicao_x, posicao_y):
       if (posicao_x != self.posicao_atual_x ) and (posicao_y != self.posicao_atual_y):
           return False

       if((posicao_x== self.posicao_atual_x or posicao_y== self.posicao_atual_y) and
         (posicao_x!= self.posicao_atual_x or posicao_y!= self.posicao_atual_y)) :

        return True


   def movimentar(self, destino_x, destino_y):
       if super().validar(destino_x, destino_y):
           if self.validar(destino_x, destino_y):
               self.posicao_atual_x= destino_x
               self.posicao_atual_y= destino_y