import pygame

class Personagem():

	def __init__(self, pos_x, pos_y, largura, altura, velocidade):
		# variáveis de caracteristicas
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.largura = largura
		self.altura = altura
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
			self.pos_y -= self.velocidade
			self.parado = False
			self.andando = True
			self.cima = True
			self.direita = False
			self.baixo = False
			self.esquerda = False
		if chave[pygame.K_d] or chave[pygame.K_RIGHT]: # and self.pos_x + self.largura < tela_l_a[1] - self.velocidade:
			self.pos_x += self.velocidade
			self.parado = False
			self.andando = True
			self.cima = False
			self.direita = True
			self.baixo = False
			self.esquerda = False
		if chave[pygame.K_s] or chave[pygame.K_DOWN]:
			self.pos_y += self.velocidade
			self.parado = False
			self.andando = True
			self.cima = False
			self.direita = False
			self.baixo = True
			self.esquerda = False
		if chave[pygame.K_a] or chave[pygame.K_LEFT]: #and self.pos_x > self.velocidade:
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
		a_cima = [pygame.image.load('imagens/personagem/andando_cima_00.png'), pygame.image.load('imagens/personagem/andando_cima_01.png'), pygame.image.load('imagens/personagem/andando_cima_02.png'), pygame.image.load('imagens/personagem/andando_cima_03.png'), pygame.image.load('imagens/personagem/andando_cima_04.png'), pygame.image.load('imagens/personagem/andando_cima_05.png'), pygame.image.load('imagens/personagem/andando_cima_06.png'), pygame.image.load('imagens/personagem/andando_cima_07.png')]
		a_esquerda = [pygame.image.load('imagens/personagem/andando_esquerda_00.png'), pygame.image.load('imagens/personagem/andando_esquerda_01.png'), pygame.image.load('imagens/personagem/andando_esquerda_02.png'), pygame.image.load('imagens/personagem/andando_esquerda_03.png'), pygame.image.load('imagens/personagem/andando_esquerda_04.png'), pygame.image.load('imagens/personagem/andando_esquerda_05.png'), pygame.image.load('imagens/personagem/andando_esquerda_06.png'), pygame.image.load('imagens/personagem/andando_esquerda_07.png')]
		a_baixo = [pygame.image.load('imagens/personagem/andando_baixo_00.png'), pygame.image.load('imagens/personagem/andando_baixo_01.png'), pygame.image.load('imagens/personagem/andando_baixo_02.png'), pygame.image.load('imagens/personagem/andando_baixo_03.png'), pygame.image.load('imagens/personagem/andando_baixo_04.png'), pygame.image.load('imagens/personagem/andando_baixo_05.png'), pygame.image.load('imagens/personagem/andando_baixo_06.png'), pygame.image.load('imagens/personagem/andando_baixo_07.png')]

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

	def detectar_colisao(self, outro_corpo):
		if self.pos_x > outro_corpo.pos_x + outro_corpo.largura / 4:
			return False
		if self.pos_x + self.largura / 4 < outro_corpo.pos_x:
			return False
		if self.pos_y > outro_corpo.pos_y + outro_corpo.altura / 4:
			return False
		if self.pos_y + self.altura / 4 < outro_corpo.pos_y:
			return False
		return True

	def desenho(self, lugar):
		transformado = pygame.transform.scale(self.imagem, (self.largura, self.altura))
		lugar.blit(transformado, (self.pos_x, self.pos_y))

class Inimigo(Personagem):

	def __init__(self, pos_x, pos_y, largura, altura, velocidade):
		super().__init__(pos_x, pos_y, largura, altura, velocidade)
		# definindo estados
		self.parado = False
		self.andando = True
		self.direita = True
		self.esquerda = False
		# carregando imagens
		self.imagem = pygame.image.load('imagens/inimigo/caveira/andando_esquerda_00.png')
		self.a_esquerda = [pygame.image.load('imagens/inimigo/caveira/andando_esquerda_00.png'), pygame.image.load('imagens/inimigo/caveira/andando_esquerda_01.png'), pygame.image.load('imagens/inimigo/caveira/andando_esquerda_02.png'), pygame.image.load('imagens/inimigo/caveira/andando_esquerda_03.png'), pygame.image.load('imagens/inimigo/caveira/andando_esquerda_04.png'), pygame.image.load('imagens/inimigo/caveira/andando_esquerda_05.png'), pygame.image.load('imagens/inimigo/caveira/andando_esquerda_06.png'), pygame.image.load('imagens/inimigo/caveira/andando_esquerda_07.png')]

	def movimentacao(self, tela): 
		if self.pos_x <= 0:
			self.velocidade = abs(self.velocidade)
			self.andando = True
			self.direita = True
			self.esquerda = False
		elif self.pos_x >= tela[0] - self.largura:
			self.velocidade = abs(self.velocidade) * -1
			self.andando = True
			self.direita = False
			self.esquerda = True
		self.pos_x += self.velocidade
		
	def animacao(self):
		frame_a_esquerda = 0
		
		frame_skip = 4
		
		if self.esquerda or self.direita:
			if frame_a_esquerda < len(self.a_esquerda):
				frame_a_esquerda += self.contador_frames // frame_skip
			if frame_a_esquerda + 1 >= len(self.a_esquerda):
				frame_a_esquerda = 0
				self.contador_frames = 0

		if self.esquerda: #andando pra esquerda
			self.imagem = self.a_esquerda[frame_a_esquerda]
		if self.direita: #andando pra direita
			transforma = self.a_esquerda[frame_a_esquerda]
			self.imagem = pygame.transform.flip(transforma, True, False)

class Bau(Personagem):

	def __init__(self, pos_x, pos_y, largura, altura, velocidade):
		super().__init__(pos_x, pos_y, largura, altura, velocidade)
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
			self.imagem = self.abrindo #[frame_abrindo]
		# Aberto
		if self.a_aberto:
			self.imagem = self.aberto

	def desenho(self, lugar):
		transformado = pygame.transform.scale(self.imagem, (self.largura, self.altura))
		lugar.blit(transformado, (self.pos_x, self.pos_y))