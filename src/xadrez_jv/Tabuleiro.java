package xadrez_jv;

import java.util.ArrayList;

public class Tabuleiro {
	private Peca[][] matrizPosicao; 
	private ArrayList<Peca> pecas;
	private ArrayList<Peca> capturadasBrancas;
	private ArrayList<Peca> capturadasPretas;
	
	Tabuleiro()
	{
		this.matrizPosicao = new Peca[8][8];
		this.pecas = new ArrayList<>();
		this.capturadasBrancas = new ArrayList<>();
		this.capturadasPretas = new ArrayList<>();
	}
	
	public Peca getMatrizPosicao(int posicaoX, int posicaoY) {
		return matrizPosicao[posicaoX][posicaoY];
	}
	
	public ArrayList<Peca> getPecas() {
		return pecas;
	}
	
	public void setPecas(ArrayList<Peca> pecas) {
		this.pecas = pecas;
	}
	
	public void setPeca(Peca peca)
	{
		int indice = this.pecas.size();
		peca.id = indice;
		this.pecas.add(peca);
		this.matrizPosicao[peca.posicaoAtualX][peca.posicaoAtualY] = peca;
	}
	
	public boolean validarMovimentacao(int destinoX, int destinoY, Peca peca)
	{
		if (this.matrizPosicao[destinoX][destinoY] == null)
			return true;
		
		Peca pecaDestino = this.matrizPosicao[destinoX][destinoY];
		if (pecaDestino.cor == peca.cor)
			return false;
		
		pecaDestino.mudarEstado();
		if (pecaDestino.cor == "Branco") this.capturadasBrancas.add(pecaDestino);
		else this.capturadasPretas.add(pecaDestino);
		return true;
	}
	
	public boolean movimentarPeca(int destinoX, int destinoY, int indice)
	{
		Peca peca = this.pecas.get(indice);
		if (peca.movimentar(destinoX, destinoY))
		{
			if (validarMovimentacao(destinoX, destinoY, peca))
			{
				this.matrizPosicao[destinoX][destinoY] = peca;
				this.matrizPosicao[peca.posicaoOrigemX][peca.posicaoOrigemY] = null;
			}
			return true;
		}
		//Caso o movimento seja válido, mas o tabuleiro na posição de destino não é livre
		this.pecas.get(indice).desfazer_movimento();
		return false;
	}
	
	public boolean isEmpty(int x, int y)
	{
		return (this.matrizPosicao[x][y] == null) ? true : false;
	}
	
	public void limparTabuleiro()
	{
		for (int i = 0; i < 8; i++)
		{
			for (int j = 0; j < 8; j++)
			{
				if (!isEmpty(i, j)) 
					this.matrizPosicao[i][j] = null;
			}
		}
	}
	
	public String verificaTipo(Peca peca)
	{
		if (peca == null)
			return "  ";
		if (peca instanceof Bispo)
		{
			if (peca.cor == "Branco")
				return "BB";
			return "BP";
		}
		if (peca instanceof Cavalo)
		{
			if (peca.cor == "Branco")
				return "CB";
			return "CP";
		}
		if (peca instanceof Torre)
		{
			if (peca.cor == "Branco")
				return "TB";
			return "TP";
		}
		
		return "  ";
	}
	
	public void capturados(String cor)
	{
		Peca peca;
		for (int i = 0; i < this.pecas.size(); i++)
		{
			peca = this.pecas.get(i);
			if (!(peca.estado) && peca.cor == cor)
				System.out.print(verificaTipo(peca));
		}
		System.out.println();
	}
	
	public void imprimirTabuleiro()
	{
		System.out.println("  |  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |");
		capturados("Preto");
		for (int i = 0; i < 8; i++)
		{
			System.out.printf("%d | ", i+1);
			for (int j = 0; j < 8; j++)
			{
				System.out.print(verificaTipo(this.matrizPosicao[i][j]) + " |");
			}
			System.out.println();			
		}
		capturados("Branco");
		System.out.println();
	}		
	
	/*public static void main(String args[])
	{
		Tabuleiro t = new Tabuleiro();
		Peca b = new Bispo(0,0,0);
		Peca c = new Cavalo(0, 7, 1);
		Peca to = new Torre(4, 7, 1);
		
		t.setPeca(b); t.setPeca(c); t.setPeca(to);
		t.imprimirTabuleiro();
		
		t.movimentarPeca(7, 7, b.id);
		t.imprimirTabuleiro();
		
		t.movimentarPeca(5, 5, b.id);
		t.imprimirTabuleiro();
		
		t.movimentarPeca(7, 3, b.id);
		t.imprimirTabuleiro();
	}*/
}
