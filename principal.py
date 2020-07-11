import pygame

from complementos.motor import *

tela_titulo = 'Testando'
cor_branca = (255, 255, 255)
cor_preta = (0, 0, 0)
relogio_de_atualizacao = pygame.time.Clock()

pygame.init()

novo_jogo = Jogo(tela_titulo, tela_largura_altura)
novo_jogo.loop_do_jogo()

pygame.quit()