import pygame

from complementos.motor import tela_largura_altura

class Personagem():

	velocidade = 5

	def __init__(self, lugar_da_imagem, posicao_x, posicao_y, largura, altura):
		self.carregando = pygame.image.load(lugar_da_imagem)
		self.imagem = pygame.transform.scale(self.carregando, (largura, altura))
		self.posicao_x = posicao_x
		self.posicao_y = posicao_y
		self.largura = largura
		self.altura = altura

	def desenho(self, lugar):
		lugar.blit(self.imagem, (self.posicao_x, self.posicao_y))

	def movimento(self, direcao_y, direcao_x):
		#subir e descer
		if direcao_y > 0:
			self.posicao_y -= self.velocidade
		if direcao_y < 0:
			self.posicao_y += self.velocidade
		#ir pra direita e esquerda
		if direcao_x > 0:
			self.posicao_x += self.velocidade
		if direcao_x < 0:
			self.posicao_x -= self.velocidade
		#travar na altura
		if self.posicao_y <= (self.altura / 6):
			self.posicao_y += self.velocidade
		if self.posicao_y >= (tela_largura_altura[1] - self.altura):
			self.posicao_y -= self.velocidade
		#travar na largura
		if self.posicao_x <= self.largura:
			self.posicao_x += abs(self.velocidade)
		if self.posicao_x >= (tela_largura_altura[0] - (self.largura * 2)):
			self.posicao_x -= abs(self.velocidade)

	def detectar_colisao(self, outro_corpo):
		if self.posicao_x > outro_corpo.posicao_x + outro_corpo.largura:
			return False
		if self.posicao_x + self.largura < outro_corpo.posicao_x:
			return False
		if self.posicao_y > outro_corpo.posicao_y + outro_corpo.altura:
			return False
		if self.posicao_y + self.altura < outro_corpo.posicao_y:
			return False
		return True

class Inimigo(Personagem):

	velocidade = 5

	def __init__(self, lugar_da_imagem, posicao_x, posicao_y, largura, altura):
		super().__init__(lugar_da_imagem, posicao_x, posicao_y, largura, altura)

	def movimento(self, tela): 
		if self.posicao_x <= (self.largura):
			self.velocidade = abs(self.velocidade)
		elif self.posicao_x >= (tela_largura_altura[0] - (self.largura * 2)):
			self.velocidade = (abs(self.velocidade)) * -1
		self.posicao_x += self.velocidade

class Bau(Personagem):

	def __init__(self, lugar_da_imagem, posicao_x, posicao_y, largura, altura):
		super().__init__(lugar_da_imagem, posicao_x, posicao_y, largura, altura)
		
	def desenho(self, lugar):
		lugar.blit(self.imagem, (self.posicao_x, self.posicao_y))