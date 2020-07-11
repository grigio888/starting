import pygame

from complementos.motor import tela_largura_altura

class Inimigo():

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

	def movimento(self, tela): 
		if self.posicao_x <= (self.largura):
			self.velocidade = abs(self.velocidade)
		elif self.posicao_x >= (tela_largura_altura[0] - (self.largura * 2)):
			self.velocidade = (abs(self.velocidade)) * -1
		self.posicao_x += self.velocidade