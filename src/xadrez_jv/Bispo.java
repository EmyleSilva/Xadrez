package xadrez_jv;

public class Bispo extends Peca{
	
	Bispo(int posicaoOrigemX, int posicaoOrigemY, int cor)
	{
		super(posicaoOrigemX, posicaoOrigemY, cor);
	}
	
	@Override
	public boolean validar(int posicaoX, int posicaoY)
	{
		if (posicaoX == this.posicaoAtualX || posicaoY == this.posicaoAtualY)
			return false;
		if (Math.abs(posicaoY - this.posicaoAtualY) != Math.abs(posicaoX - this.posicaoAtualX))
			return false;
		return true;
	}
	
	@Override 
	public boolean movimentar(int destinoX, int destinoY)
	{
		if (super.validar(destinoX, destinoY))
		{
			if (validar(destinoX, destinoY))
			{
				this.posicaoOrigemX = this.posicaoAtualX;
				this.posicaoOrigemY = this.posicaoAtualY;
				this.posicaoAtualX = destinoX;
				this.posicaoAtualY = destinoY;
				return true;
			}
		}
		return false;
	}
}
