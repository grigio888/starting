import pygame

tela_largura_altura = (500, 500)
cor_branca = (255, 255, 255)
cor_preta = (0, 0, 0)
relogio_de_atualizacao = pygame.time.Clock()

from complementos.fundo import *
from complementos.personagem import *
from complementos.inimigo import *
from complementos.bau import *
from complementos.gameover import *

class Jogo:

	tick_rate = 60

	def __init__(self, titulo, tamanho_tela):
		self.titulo = titulo
		self.tamanho_tela = tamanho_tela

		self.tela = pygame.display.set_mode(tamanho_tela)
		self.tela.fill(cor_branca)
		pygame.display.set_caption(titulo)

	def loop_do_jogo(self):

		fundo = Fundo('imagens/background.png', 0, 0, 500, 500)
		personagem = Personagem('imagens/player.png', 233, 450, 36, 40)
		inimigo = Inimigo('imagens/enemy.png', 233, 255, 40, 36)
		bau = Bau('imagens/bau.png', 235, 50, 30, 28)
		img_game_over = GameOver('imagens/game_over.png', 55, 155, 400, 200)
		direcao_y = 0
		direcao_x = 0
		colisao = False
		game_over = False
		setor = 'comeco'
		while not game_over:
			#onde tudo começa
			while setor == 'comeco':
				for event in pygame.event.get():
					# habilitando o jogo para fechar
					if event.type == pygame.QUIT:
						game_over = True
					# movimentação do personagem
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_UP:
							direcao_y = 1
						if event.key == pygame.K_DOWN:
							direcao_y = -1
						if event.key == pygame.K_RIGHT:
							direcao_x = 1
						if event.key == pygame.K_LEFT:
							direcao_x = -1
					if event.type == pygame.KEYUP:
						if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
							direcao_y = 0
							direcao_x = 0
					print(event)
		
				fundo.desenho(self.tela)
				bau.desenho(self.tela)
				personagem.movimento(direcao_y, direcao_x)
				personagem.desenho(self.tela)
				inimigo.movimento(self.tela)
				inimigo.desenho(self.tela)

				colisao = personagem.detectar_colisao(inimigo)
				if colisao == True:
					setor = 'game over'
			
				#até aqui
				pygame.display.update()
				relogio_de_atualizacao.tick(self.tick_rate)
				#pra sempre atualizar a tela

			while setor == 'game over':
				fundo.desenho(self.tela)

				img_game_over.desenho(self.tela)

				pygame.display.update()
				relogio_de_atualizacao.tick(self.tick_rate)