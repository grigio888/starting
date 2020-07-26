import pygame

class ExibirImagemEstatica():

	def __init__(self, lugar_da_imagem, pos_x, pos_y, largura, altura):
		self.carregando = pygame.image.load(lugar_da_imagem)
		self.imagem = pygame.transform.scale(self.carregando, (largura, altura))
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.largura = largura
		self.altura = altura

	def desenho(self, lugar):
		lugar.blit(self.imagem, (self.pos_x, self.pos_y))

class Fundo(ExibirImagemEstatica):
	def __init__(self, lugar_da_imagem, pos_x, pos_y, largura, altura):
		super().__init__(lugar_da_imagem, pos_x, pos_y, largura, altura)

class ArvoreGrandeA():
		
	def __init__(self, pos_x, pos_y):
		self.imagem = pygame.image.load('imagens/obstaculos/arvore_grande.png')
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.largura = 128
		self.altura = 160

	def hitbox(self):
		return pygame.Rect(self.pos_x + 37, self.pos_y + 109, 63, 45)

	def desenho(self, lugar):
		lugar.blit(self.imagem, (self.pos_x, self.pos_y))

class ArvoreGrandeB(ArvoreGrandeA):
	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('imagens/obstaculos/arvore_grande2.png')
		self.largura = 128
		self.altura = 176

	def hitbox(self):
		return pygame.Rect(self.pos_x + 34, self.pos_y + 125, 65, 45)

class TroncoCortado(ArvoreGrandeA):
	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('imagens/obstaculos/tronco_cortado.png')
		self.largura = 80
		self.altura = 64

	def hitbox(self):
		return pygame.Rect(self.pos_x + 16, self.pos_y + 3, 75, 47)

class CaixaInteira(ArvoreGrandeA):
	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('imagens/obstaculos/caixa_inteira.png')
		self.largura = 64
		self.altura = 32

	def hitbox(self):
		return pygame.Rect(self.pos_x, self.pos_y, self.largura, 2)

class CaixaQuebrada(ArvoreGrandeA):
	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('imagens/obstaculos/caixa_quebrada.png')
		self.largura = 64
		self.altura = 32

	def hitbox(self):
		return pygame.Rect(self.pos_x, self.pos_y, self.largura, 2)