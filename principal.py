import pygame

from complementos.motor import *

tela_titulo = 'Testando'
relogio_de_atualizacao = pygame.time.Clock()

pygame.init()

novo_jogo = Jogo(tela_titulo, tela_largura_altura)
novo_jogo.loop_do_jogo()

pygame.quit()