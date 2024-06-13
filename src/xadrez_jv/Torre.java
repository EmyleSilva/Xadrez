package xadrez_jv;

public class Torre extends Peca{
	
	Torre(int posicaoX, int posicaoY, int cor)
	{
		super(posicaoX, posicaoY, cor);
	}
	
	@Override 
	public boolean validar(int posicaoX, int posicaoY)
	{
		if (super.validar(posicaoX, posicaoY))
		{
			if (posicaoX != this.posicaoAtualX && posicaoY != this.posicaoAtualY)
				return false;
			if ((posicaoX == this.posicaoAtualX || posicaoY == this.posicaoAtualY)
				&& posicaoX != this.posicaoAtualX || posicaoY != this.posicaoAtualY)
				return true;
		}
		return true;
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
