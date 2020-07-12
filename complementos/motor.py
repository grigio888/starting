import pygame

tela_largura_altura = (500, 500)
cor_branca = (255, 255, 255)
cor_preta = (0, 0, 0)
relogio_de_atualizacao = pygame.time.Clock()

from complementos.exibir_imagem_estatica import *
from complementos.entidades import *

class Jogo:

	tick_rate = 60

	def __init__(self, titulo, tamanho_tela):
		self.titulo = titulo
		self.tamanho_tela = tamanho_tela

		self.tela = pygame.display.set_mode(tamanho_tela)
		self.tela.fill(cor_branca)
		pygame.display.set_caption(titulo)

	def loop_do_jogo(self):

		#variaveis que vão ser utilizadas dentro do loop
		#variaveis globais
		fundo = ExibirImagemEstatica('imagens/background.png', 0, 0, 500, 500)
		botao_start = ExibirImagemEstatica('imagens/botao_start.png', 205, 287, 100, 23)
		botao_repetir = ExibirImagemEstatica('imagens/botao_repetir.png', 205, 287, 100, 23)
		botao_sair = ExibirImagemEstatica('imagens/botao_sair.png', 205, 333, 100, 23)

		#variaveis setor == 'inicio':
		dialogo_sup = ExibirImagemEstatica('imagens/dialogo_comeco.png', 100, 105, 300, 150)

		#variaveis setor == 'comeco':
		personagem = Personagem('imagens/player.png', 233, 450, 36, 40)
		inimigo = Inimigo('imagens/enemy.png', 233, 255, 40, 36)
		bau = Bau('imagens/bau.png', 235, 50, 30, 28)
		direcao_y = 0
		direcao_x = 0
		
		#variaveis setor == 'game over':
		img_game_over = ExibirImagemEstatica('imagens/game_over.png', 105, 155, 300, 85)

		#variaveis setor == 'game win':
		img_game_win = ExibirImagemEstatica('imagens/game_win.png', 105, 155, 300, 85)

		#variaveis referente ao loop
		game_over = False
		setor = 'inicio'

		while not game_over:

			#onde tudo começa
			while setor == 'inicio':

				for event in pygame.event.get():
					# habilitando o jogo para fechar
					if event.type == pygame.QUIT:
						game_over = True
						setor = 'saida'
				
				#funcao de clicar
				if pygame.mouse.get_pos()[0] >= botao_start.posicao_x and pygame.mouse.get_pos()[1] >= botao_start.posicao_y and pygame.mouse.get_pos()[0] <= botao_start.posicao_x + botao_start.largura and pygame.mouse.get_pos()[1] <= botao_start.posicao_y + botao_start.altura:
					if pygame.mouse.get_pressed()[0]:
						setor = 'comeco'
				if pygame.mouse.get_pos()[0] >= botao_sair.posicao_x and pygame.mouse.get_pos()[1] >= botao_sair.posicao_y and pygame.mouse.get_pos()[0] <= botao_sair.posicao_x + botao_sair.largura and pygame.mouse.get_pos()[1] <= botao_sair.posicao_y + botao_sair.altura:
					if pygame.mouse.get_pressed()[0]:
						game_over = True
						setor = 'saida'
				
				#definindo ordem dos fatos
				fundo.desenho(self.tela)
				personagem.desenho(self.tela)
				dialogo_sup.desenho(self.tela)
				botao_start.desenho(self.tela)
				botao_sair.desenho(self.tela)

				#atualizando a tela
				pygame.display.update()
				relogio_de_atualizacao.tick(self.tick_rate)
			
			while setor == 'comeco':

				for event in pygame.event.get():
					# habilitando o jogo para fechar
					if event.type == pygame.QUIT:
						game_over = True
						setor = 'saida'
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

				#definindo a ordem dos fatos
				fundo.desenho(self.tela)
				bau.desenho(self.tela)
				personagem.movimento(direcao_y, direcao_x)
				personagem.desenho(self.tela)
				inimigo.movimento(self.tela)
				inimigo.desenho(self.tela)

				#detector de colisao
				colisao_inimigo = personagem.detectar_colisao(inimigo)
				colisao_bau = personagem.detectar_colisao(bau)
				if colisao_inimigo == True:
					setor = 'game over'
				elif colisao_bau == True:
					setor = 'game win'
			
				#atualizando a tela
				pygame.display.update()
				relogio_de_atualizacao.tick(self.tick_rate)

			while setor == 'game over':

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						game_over = True
						setor = 'saida'

				#funcao de clicar
				if pygame.mouse.get_pos()[0] >= botao_repetir.posicao_x and pygame.mouse.get_pos()[1] >= botao_repetir.posicao_y and pygame.mouse.get_pos()[0] <= botao_repetir.posicao_x + botao_repetir.largura and pygame.mouse.get_pos()[1] <= botao_repetir.posicao_y + botao_repetir.altura:
					if pygame.mouse.get_pressed()[0]:
						personagem.posicao_x = 233
						personagem.posicao_y = 450
						self.direcao_x = 0
						self.direcao_y = 0
						setor = 'comeco'
				if pygame.mouse.get_pos()[0] >= botao_sair.posicao_x and pygame.mouse.get_pos()[1] >= botao_sair.posicao_y and pygame.mouse.get_pos()[0] <= botao_sair.posicao_x + botao_sair.largura and pygame.mouse.get_pos()[1] <= botao_sair.posicao_y + botao_sair.altura:
					if pygame.mouse.get_pressed()[0]:
						game_over = True
						setor = 'saida'

				fundo.desenho(self.tela)

				img_game_over.desenho(self.tela)
				botao_repetir.desenho(self.tela)
				botao_sair.desenho(self.tela)

				pygame.display.update()
				relogio_de_atualizacao.tick(self.tick_rate)

			while setor == 'game win':

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						game_over = True
						setor = 'saida'

				#funcao de clicar
				if pygame.mouse.get_pos()[0] >= botao_repetir.posicao_x and pygame.mouse.get_pos()[1] >= botao_repetir.posicao_y and pygame.mouse.get_pos()[0] <= botao_repetir.posicao_x + botao_repetir.largura and pygame.mouse.get_pos()[1] <= botao_repetir.posicao_y + botao_repetir.altura:
					if pygame.mouse.get_pressed()[0]:
						personagem.posicao_x = 233
						personagem.posicao_y = 450
						self.direcao_x = 0
						self.direcao_y = 0
						setor = 'comeco'
				if pygame.mouse.get_pos()[0] >= botao_sair.posicao_x and pygame.mouse.get_pos()[1] >= botao_sair.posicao_y and pygame.mouse.get_pos()[0] <= botao_sair.posicao_x + botao_sair.largura and pygame.mouse.get_pos()[1] <= botao_sair.posicao_y + botao_sair.altura:
					if pygame.mouse.get_pressed()[0]:
						game_over = True
						setor = 'saida'

				fundo.desenho(self.tela)

				img_game_win.desenho(self.tela)
				botao_repetir.desenho(self.tela)
				botao_sair.desenho(self.tela)

				pygame.display.update()
				relogio_de_atualizacao.tick(self.tick_rate)