package xadrez_jv;

import java.util.Scanner;

public class Iniciar {

	public static void main(String[] args) {
		
		int quantidadeOpcoes = 6;
		Scanner s = new Scanner(System.in);
		
		while (Menu.opcao != 0)
		{
			Menu.exibirMenu();
			Menu.lerOpcao(quantidadeOpcoes);
			
			switch(Menu.opcao)
			{
				case 1:
				case 2:
				case 3:
					Menu.adicionarPeca();
					Menu.exibirTabuleiro();
					break;
				case 4:
					Menu.realizarMovimento();
					Menu.exibirTabuleiro();
					break;
				case 5:
					Menu.exibirTabuleiro();
					break;
				default:
					System.out.println("Obrigada por jogar!");
					break;
			}
		}			
	}
}
