package xadrez_jv;

import java.awt.*;
import javax.swing.*;

import xadrez_jv.Menu;

public class Menu extends JFrame{
	public static int opcao = 1;
	public static Tabuleiro tabuleiro = new Tabuleiro();
	//public static Scanner s = new Scanner(System.in);
	
	//Atributos da interface gráfica
	private ImageIcon icon;
	private JLabel lblimagem;
	private JButton btnexplicavel;
	private JButton btnsimulacao;
	private JPanel cLeftSide;
	private JPanel cRightSide;
	
	Menu()
	{
		icon = new ImageIcon(getClass().getResource("/imagens/chess.jpeg"));
		lblimagem = new JLabel(icon);
		btnexplicavel = new JButton("Modo Explicável");
		btnsimulacao = new JButton("Modo Simulação");
		
		/*btnexplicavel.setPreferredSize(new Dimension(100, 30));
		btnsimulacao.setPreferredSize(new Dimension(100, 30));
		btnexplicavel.setMargin(new Insets(5,5,5,5));
		btnsimulacao.setMargin(new Insets(5,5,5,5));*/
		
		cRightSide = new JPanel();
		cRightSide.setLayout(new GridLayout(1, 1));
		cRightSide.add(lblimagem);
		
		cLeftSide = new JPanel();
		cLeftSide.setLayout(new GridLayout(2, 1));
		cLeftSide.add(btnexplicavel);
		cLeftSide.add(btnsimulacao);
		
		setLayout(new GridLayout(1, 2));
		add(cLeftSide);
		add(cRightSide);
	}
	
	/*public static void lerOpcao(int quantidadeOpcoes)
	{
		System.out.print("Opção: ");
		Menu.opcao = s.nextInt();
		System.out.println();
		
		while (Menu.opcao < 1 || Menu.opcao > quantidadeOpcoes)
		{
			System.out.println("Opção Inválida! Selecione uma opção entre 0 e " + quantidadeOpcoes);
			Menu.opcao = s.nextInt();
			System.out.println();
		}
	}
	
	public static void exibirMenu()
	{
		System.out.println("1 - Adicionar Bispo");
		System.out.println("2 - Adicionar Cavalo");
		System.out.println("3 - Adicionar Torre");
		System.out.println("4 - Movimentar Peça");
		System.out.println("5 - Exibir Tabuleiro");
		System.out.println("6 - Sair");
	}
	
	public static void adicionarPeca()
	{
		System.out.print("Informe a posição X: ");
		int posicaoX = s.nextInt() - 1;
		System.out.println("X: " + posicaoX);
		System.out.println("Informe a posição Y: ");
		int posicaoY = s.nextInt() - 1;
		System.out.println("Y: " + posicaoY);
		System.out.println("Informe a cor (1 para 'Branco' e 2 para 'Preto'): ");
		int cor = s.nextInt() - 1;
		System.out.println();
		
		Peca peca;
		
		if (Menu.opcao == 1) {
			peca = new Bispo(posicaoX, posicaoY, cor);
			System.out.println("BISPO X: " + peca.posicaoAtualX + " BISPO Y: " + peca.posicaoAtualY);
		}else if(Menu.opcao == 2) 
			peca = new Cavalo(posicaoX, posicaoY, cor);
		else
			peca = new Torre(posicaoX, posicaoY, cor);
		
		Menu.tabuleiro.setPeca(peca);
	}
	
	public static Peca recuperarPeca(int posicaoAtualX, int posicaoAtualY)
	{
		Peca peca = Menu.tabuleiro.getMatrizPosicao(posicaoAtualX, posicaoAtualY);
		
		while (peca == null)
		{
			System.out.println("Posição Inválida! Não existe peça na posição indicada. Informe uma posição válida!");
			System.out.println("Posição X: ");
			posicaoAtualX = s.nextInt() - 1;
			System.out.println("Posição Y: ");
			posicaoAtualY = s.nextInt() - 1;
			peca = Menu.tabuleiro.getMatrizPosicao(posicaoAtualX, posicaoAtualY);
		}
		
		return peca;
	}
	
	public static void realizarMovimento()
	{
		System.out.println("Informe as coordenadas da peça que você deseja movimentar: ");
		System.out.print("Posição X: ");
		int atualX = s.nextInt() - 1;
		System.out.println();
		System.out.print("Posição Y: ");
		int atualY = s.nextInt() - 1;
		System.out.println();
		
		Peca peca = recuperarPeca(atualX, atualY);
		
		System.out.println("Mover a peça para: ");
		System.out.print("Destino X: ");
		int destinoX = s.nextInt() - 1;
		System.out.println();
		System.out.print("Destino Y: ");
		int destinoY = s.nextInt() - 1;
		System.out.println();
		
		Menu.tabuleiro.movimentarPeca(destinoX, destinoY, peca.id);
	}
	
	public static void exibirTabuleiro()
	{
		System.out.println();
		Menu.tabuleiro.imprimirTabuleiro();
		System.out.println();
	}*/
}
