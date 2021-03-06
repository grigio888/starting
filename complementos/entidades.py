import pygame
import random

class Personagem():

	def __init__(self, pos_x, pos_y, velocidade):
		# variáveis de caracteristicas
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.largura = 64
		self.altura = 64
		# variáveis referente aos movimentos
		self.velocidade = velocidade
		# variaveis referente às animações
		self.imagem = 'imagem'
		self.contador_frames = 0
		self.parado = True
		self.andando = False
		self.cima = True
		self.direita = False
		self.baixo = False
		self.esquerda = False
						
	def movimentacao(self, chave):
		if chave[pygame.K_w] or chave[pygame.K_UP]:
			if self.pos_y > -14:
				self.pos_y -= self.velocidade
				self.parado = False
				self.andando = True
				self.cima = True
				self.direita = False
				self.baixo = False
				self.esquerda = False
		if chave[pygame.K_d] or chave[pygame.K_RIGHT]: # and self.pos_x + self.largura < tela_l_a[1] - self.velocidade:
			if self.pos_x < 516:
				self.pos_x += self.velocidade
				self.parado = False
				self.andando = True
				self.cima = False
				self.direita = True
				self.baixo = False
				self.esquerda = False
		if chave[pygame.K_s] or chave[pygame.K_DOWN]:
			if self.pos_y < 437:
				self.pos_y += self.velocidade
				self.parado = False
				self.andando = True
				self.cima = False
				self.direita = False
				self.baixo = True
				self.esquerda = False
		if chave[pygame.K_a] or chave[pygame.K_LEFT]: #and self.pos_x > self.velocidade:
			if self.pos_x > -15:
				self.pos_x -= self.velocidade
				self.parado = False
				self.andando = True
				self.cima = False
				self.direita = False
				self.baixo = False
				self.esquerda = True
		if not chave[pygame.K_w] and not chave[pygame.K_UP]:
			if not chave[pygame.K_d] and not chave[pygame.K_RIGHT]:
				if not chave[pygame.K_s] and not chave[pygame.K_DOWN]:
					if not chave[pygame.K_a] and not chave[pygame.K_LEFT]:
									self.parado = True
									self.andando = False

	def animacao(self):
		parado_cima = pygame.image.load('imagens/personagem/parado_cima_00.png')
		parado_esquerda = pygame.image.load('imagens/personagem/parado_esquerda_00.png')
		parado_baixo = pygame.image.load('imagens/personagem/parado_baixo_00.png')
		a_cima = [pygame.image.load('imagens/personagem/andando_cima_00.png'),
				  pygame.image.load('imagens/personagem/andando_cima_01.png'),
				  pygame.image.load('imagens/personagem/andando_cima_02.png'),
				  pygame.image.load('imagens/personagem/andando_cima_03.png'),
				  pygame.image.load('imagens/personagem/andando_cima_04.png'),
				  pygame.image.load('imagens/personagem/andando_cima_05.png'),
				  pygame.image.load('imagens/personagem/andando_cima_06.png'),
				  pygame.image.load('imagens/personagem/andando_cima_07.png')]
		a_esquerda = [pygame.image.load('imagens/personagem/andando_esquerda_00.png'),
					  pygame.image.load('imagens/personagem/andando_esquerda_01.png'),
					  pygame.image.load('imagens/personagem/andando_esquerda_02.png'),
					  pygame.image.load('imagens/personagem/andando_esquerda_03.png'),
					  pygame.image.load('imagens/personagem/andando_esquerda_04.png'),
					  pygame.image.load('imagens/personagem/andando_esquerda_05.png'),
					  pygame.image.load('imagens/personagem/andando_esquerda_06.png'),
					  pygame.image.load('imagens/personagem/andando_esquerda_07.png')]
		a_baixo = [pygame.image.load('imagens/personagem/andando_baixo_00.png'),
				   pygame.image.load('imagens/personagem/andando_baixo_01.png'),
				   pygame.image.load('imagens/personagem/andando_baixo_02.png'),
				   pygame.image.load('imagens/personagem/andando_baixo_03.png'),
				   pygame.image.load('imagens/personagem/andando_baixo_04.png'),
				   pygame.image.load('imagens/personagem/andando_baixo_05.png'),
				   pygame.image.load('imagens/personagem/andando_baixo_06.png'),
				   pygame.image.load('imagens/personagem/andando_baixo_07.png')]

		frame_a_cima = 0
		frame_a_esquerda = 0
		frame_a_baixo = 0
			
		frame_skip = 4
		
		if self.andando:
			if self.cima:
				if frame_a_cima < len(a_cima):
					frame_a_cima += self.contador_frames // frame_skip
				if frame_a_cima + 1 >= len(a_cima):
					frame_a_cima = 0
					self.contador_frames = 0
			if self.esquerda or self.direita:
				if frame_a_esquerda < len(a_esquerda):
					frame_a_esquerda += self.contador_frames // frame_skip
				if frame_a_esquerda + 1 >= len(a_esquerda):
					frame_a_esquerda = 0
					self.contador_frames = 0
			if self.baixo:
				if frame_a_baixo < len(a_baixo):
					frame_a_baixo += self.contador_frames // frame_skip
				if frame_a_baixo + 1 >= len(a_baixo):
					frame_a_baixo = 0
					self.contador_frames = 0
					
		#parado e olhando pra cima
		if self.parado and self.cima:
			self.imagem = parado_cima
		#parado e olhando pra esquerda
		if self.parado and self.esquerda:
			self.imagem = parado_esquerda
		#parado e olhando pra baixo
		if self.parado and self.baixo:
			self.imagem = parado_baixo
		#parado e olhando pra direita
		if self.parado and self.direita:
			transforma = parado_esquerda
			self.imagem = pygame.transform.flip(transforma, True, False)

		#andando pra cima
		if self.andando and self.cima:
			self.imagem = a_cima[frame_a_cima]
		#andando pra esquerda
		if self.andando and self.esquerda:
			self.imagem = a_esquerda[frame_a_esquerda]
		#andando pra baixo
		if self.andando and self.baixo:
			self.imagem = a_baixo[frame_a_baixo]
		#andando pra direita
		if self.andando and self.direita:
			transforma = a_esquerda[frame_a_esquerda]
			self.imagem = pygame.transform.flip(transforma, True, False)

	def hitbox(self):
		return pygame.Rect(self.pos_x + self.altura / 4, self.pos_y + self.altura / 5, 33, 50)

	def desenho(self, lugar):
		transformado = pygame.transform.scale(self.imagem, (self.largura, self.altura))
		lugar.blit(transformado, (self.pos_x, self.pos_y))

class Inimigo(Personagem):

	def __init__(self, pos_x, pos_y, velocidade):
		super().__init__(pos_x, pos_y, velocidade)
		# definindo estados
		self.parado = True
		self.andando = False
		self.cima = False
		self.direita = False
		self.baixo = True
		self.esquerda = False
		# movimentacao
		self.cont_mov = 0
		self.aleatoriedade = 0
		self.rastro_x = 0
		self.rastro_y = 0
		# carregando imagens
		self.parado_cima = pygame.image.load('imagens/inimigo/caveira/parado_cima_00.png')
		self.parado_esquerda = pygame.image.load('imagens/inimigo/caveira/parado_esquerda_00.png')
		self.parado_baixo = pygame.image.load('imagens/inimigo/caveira/parado_baixo_00.png')
		self.a_cima = [pygame.image.load('imagens/inimigo/caveira/andando_cima_00.png'),
					   pygame.image.load('imagens/inimigo/caveira/andando_cima_01.png'),
					   pygame.image.load('imagens/inimigo/caveira/andando_cima_02.png'),
					   pygame.image.load('imagens/inimigo/caveira/andando_cima_03.png'),
					   pygame.image.load('imagens/inimigo/caveira/andando_cima_04.png'),
					   pygame.image.load('imagens/inimigo/caveira/andando_cima_05.png'),
					   pygame.image.load('imagens/inimigo/caveira/andando_cima_06.png'),
					   pygame.image.load('imagens/inimigo/caveira/andando_cima_07.png')]
		self.a_esquerda = [pygame.image.load('imagens/inimigo/caveira/andando_esquerda_00.png'),
						   pygame.image.load('imagens/inimigo/caveira/andando_esquerda_01.png'),
						   pygame.image.load('imagens/inimigo/caveira/andando_esquerda_02.png'),
						   pygame.image.load('imagens/inimigo/caveira/andando_esquerda_03.png'),
						   pygame.image.load('imagens/inimigo/caveira/andando_esquerda_04.png'),
						   pygame.image.load('imagens/inimigo/caveira/andando_esquerda_05.png'),
						   pygame.image.load('imagens/inimigo/caveira/andando_esquerda_06.png'),
						   pygame.image.load('imagens/inimigo/caveira/andando_esquerda_07.png')]
		self.a_baixo = [pygame.image.load('imagens/inimigo/caveira/andando_baixo_00.png'),
						pygame.image.load('imagens/inimigo/caveira/andando_baixo_01.png'),
						pygame.image.load('imagens/inimigo/caveira/andando_baixo_02.png'),
						pygame.image.load('imagens/inimigo/caveira/andando_baixo_03.png'),
						pygame.image.load('imagens/inimigo/caveira/andando_baixo_04.png'),
						pygame.image.load('imagens/inimigo/caveira/andando_baixo_05.png'),
						pygame.image.load('imagens/inimigo/caveira/andando_baixo_06.png'),
						pygame.image.load('imagens/inimigo/caveira/andando_baixo_07.png')]

	def movimentacao(self, lista_de_colisoes): 
		if self.aleatoriedade == 0: #parado baixo
			self.parado = True
			self.andando = False
			self.cima = False
			self.direita = False
			self.baixo = True
			self.esquerda = False
		if self.aleatoriedade == 3: #andando baixo
			if self.hitbox().collidelist(lista_de_colisoes) == -1:
				if self.pos_y < 500 - self.altura:
					self.parado = False
					self.andando = True
					self.cima = False
					self.direita = False
					self.baixo = True
					self.esquerda = False
					self.pos_y += self.velocidade
			if self.hitbox().collidelist(lista_de_colisoes) >= 0:
				if self.pos_y > 255:
					self.pos_y -= self.velocidade
		if self.aleatoriedade == 6: #parado esquerda
			self.parado = True
			self.andando = False
			self.cima = False
			self.direita = False
			self.baixo = False
			self.esquerda = True
		if self.aleatoriedade == 9: #andando esquerda
			if self.hitbox().collidelist(lista_de_colisoes) == -1:
				self.parado = False
				self.andando = True
				self.cima = False
				self.direita = False
				self.baixo = False
				self.esquerda = True
				self.pos_x -= self.velocidade
			if self.hitbox().collidelist(lista_de_colisoes) >= 0:
				if self.pos_x < 255:
					self.pos_x += self.velocidade
		if self.aleatoriedade == 12: #parado cima
			self.parado = True
			self.andando = False
			self.cima = True
			self.direita = False
			self.baixo = False
			self.esquerda = False
		if self.aleatoriedade == 15: #andando cima
			if self.hitbox().collidelist(lista_de_colisoes) == -1:
				if self.pos_y > 219:
					self.parado = False
					self.andando = True
					self.cima = True
					self.direita = False
					self.baixo = False
					self.esquerda = False
					self.pos_y -= self.velocidade
			if self.hitbox().collidelist(lista_de_colisoes) >= 0:
				if self.pos_y < 255:
					self.pos_y += self.velocidade
		if self.aleatoriedade == 18: #parado direita
			self.parado = True
			self.andando = False
			self.cima = False
			self.direita = True
			self.baixo = False
			self.esquerda = False
		if self.aleatoriedade == 21: #andando direita
			if self.hitbox().collidelist(lista_de_colisoes) == -1:
				self.parado = False
				self.andando = True
				self.cima = False
				self.direita = True
				self.baixo = True
				self.esquerda = False
				self.pos_x += self.velocidade
			if self.hitbox().collidelist(lista_de_colisoes) >= 0:
				if self.pos_x > 255:
					self.pos_x -= self.velocidade
		else:
			if self.rastro_x == self.pos_x and self.rastro_y == self.pos_y:
				self.parado = True
				self.andando = False
		
	def animacao(self):
		frame_a_cima = 0
		frame_a_esquerda = 0
		frame_a_baixo = 0
		
		frame_skip = 4

		if self.andando:
			if self.cima:
				if frame_a_cima < len(self.a_cima):
					frame_a_cima += self.contador_frames // frame_skip
				if frame_a_cima + 1 >= len(self.a_cima):
					frame_a_cima = 0
					self.contador_frames = 0
			if self.esquerda or self.direita:
				if frame_a_esquerda < len(self.a_esquerda):
					frame_a_esquerda += self.contador_frames // frame_skip
				if frame_a_esquerda + 1 >= len(self.a_esquerda):
					frame_a_esquerda = 0
					self.contador_frames = 0
			if self.baixo:
				if frame_a_baixo < len(self.a_baixo):
					frame_a_baixo += self.contador_frames // frame_skip
				if frame_a_baixo + 1 >= len(self.a_baixo):
					frame_a_baixo = 0
					self.contador_frames = 0
		if self.parado:
			if self.cima:
				self.imagem = self.parado_cima
			if self.esquerda:
				self.imagem = self.parado_esquerda
			if self.direita:
				transforma = self.parado_esquerda
				self.imagem = pygame.transform.flip(transforma, True, False)
			if self.baixo:
				self.imagem = self.parado_baixo

		if self.andando:
			if self.cima: #andando pra esquerda
				self.imagem = self.a_cima[frame_a_cima]
			if self.esquerda: #andando pra esquerda
				self.imagem = self.a_esquerda[frame_a_esquerda]
			if self.direita: #andando pra direita
				transforma = self.a_esquerda[frame_a_esquerda]
				self.imagem = pygame.transform.flip(transforma, True, False)
			if self.baixo: #andando pra esquerda
				self.imagem = self.a_baixo[frame_a_baixo]

class Bau(Personagem):

	def __init__(self, pos_x, pos_y, velocidade):
		super().__init__(pos_x, pos_y, velocidade)
		self.largura = 32
		self.altura = 32
		# definindo animacoes
		self.a_fechado = True
		self.a_abrindo = False
		self.a_aberto = False
		# carregando imagem
		self.fechado = pygame.image.load('imagens/objetos/bau_fechado.png')
		self.abrindo = pygame.image.load('imagens/objetos/bau_abrindo.png')
		self.aberto = pygame.image.load('imagens/objetos/bau_aberto.png')
		
	def animacao(self):
		frame_abrindo = 0
				
		frame_skip = 4
		
		# Fechado
		if self.a_fechado:
			self.imagem = self.fechado
		# Abrindo
		if self.a_abrindo:
			self.imagem = self.abrindo
		# Aberto
		if self.a_aberto:
			self.imagem = self.aberto

	def hitbox(self):
		return pygame.Rect(self.pos_x, self.pos_y, self.largura, 2)

	def desenho(self, lugar):
		transformado = pygame.transform.scale(self.imagem, (self.largura, self.altura))
		lugar.blit(transformado, (self.pos_x, self.pos_y))