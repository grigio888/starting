import pygame

class GameOver():

	def __init__(self, lugar_da_imagem, posicao_x, posicao_y, largura, altura):
		self.carregando = pygame.image.load(lugar_da_imagem)
		self.imagem = pygame.transform.scale(self.carregando, (largura, altura))
		self.posicao_x = posicao_x
		self.posicao_y = posicao_y
		self.largura = largura
		self.altura = altura

	def desenho(self, lugar):
		lugar.blit(self.imagem, (self.posicao_x, self.posicao_y))



