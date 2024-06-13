package xadrez_jv;

public class Cavalo extends Peca{
	
	Cavalo(int posicaoOrigemX, int posicaoOrigemY, int cor)
	{
		super(posicaoOrigemX, posicaoOrigemY, cor);
	}
	
	@Override 
	public boolean validar(int posicaoX, int posicaoY)
	{
		if (super.validar(posicaoX, posicaoY)) {
			if (posicaoX == this.posicaoAtualX + 2 || posicaoX == this.posicaoAtualX - 2)
			{
				if (posicaoY == this.posicaoAtualY + 1 || posicaoY == posicaoAtualY - 1)
					return true;
			}else if(posicaoY == this.posicaoAtualY + 2 || posicaoY == posicaoAtualY - 2){
				if (posicaoX == this.posicaoAtualX + 1 || posicaoX == this.posicaoAtualX - 1)
					return true;
			}
		}
		return false;			
	}
	
	@Override 
	public boolean movimentar(int destinoX, int destinoY)
	{
		if (validar(destinoX, destinoY))
		{
			this.posicaoOrigemX = this.posicaoAtualX;
			this.posicaoOrigemY = this.posicaoAtualY;
			this.posicaoAtualX = destinoX;
			this.posicaoAtualY = destinoY;
			return true;
		}
		return false;
	}
}
