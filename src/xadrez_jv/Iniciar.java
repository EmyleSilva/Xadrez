package xadrez_jv;

import java.util.Scanner;
import java.awt.*;
import javax.swing.*;

public class Iniciar{

	public static void main(String[] args) {
		
		JFrame menuInicial = new Menu();
		menuInicial.setTitle("Xadrez");
		menuInicial.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		menuInicial.setBounds(300, 300, 1440, 1024);
		menuInicial.setVisible(true);		
	}
}
