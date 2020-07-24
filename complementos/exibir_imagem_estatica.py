import pygame

class ExibirImagemEstatica():

	def __init__(self, lugar_da_imagem, posicao_x, posicao_y, largura, altura):
		self.carregando = pygame.image.load(lugar_da_imagem)
		self.imagem = pygame.transform.scale(self.carregando, (largura, altura))
		self.posicao_x = posicao_x
		self.posicao_y = posicao_y
		self.largura = largura
		self.altura = altura

	def desenho(self, lugar):
		lugar.blit(self.imagem, (self.posicao_x, self.posicao_y))

class Fundo(ExibirImagemEstatica):
	def __init__(self, lugar_da_imagem, posicao_x, posicao_y, largura, altura):
		super().__init__(lugar_da_imagem, posicao_x, posicao_y, largura, altura)

	def hitbox(self):
		return [pygame.Rect(0, 66, 69, 73), pygame.Rect(76, 64, 134, 32), pygame.Rect(109, 52, 67, 10), pygame.Rect(0, 282, 69, 73), pygame.Rect(0, 386, 60, 42), pygame.Rect(69, 429, 104, 35), pygame.Rect(182, 431, 22, 27), pygame.Rect(293, 64, 134, 32), pygame.Rect(325, 52, 67, 10), pygame.Rect(430, 140, 69, 73)]