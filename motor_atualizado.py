# Importando Modulos:
import pygame
from complementos.inicializadores import *
from complementos.exibir_imagem_estatica import *
from complementos.entidades import *

# Iniciando pygame:
pygame.init()

# Loop interno do game:
while not game_over:

    #onde tudo começa
    while setor == 'inicio':

        for event in pygame.event.get():
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
        para_background()
        para_dialogo(setor)
        
        pygame.display.update()
        relogio_de_atualizacao.tick(60)
    
    while setor == 'comeco':

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                setor = 'saida'
            print(event)
        
        para_background()
        para_bau()
        para_personagem()
        para_inimigo()

        #if personagem.hitbox().collidelist(fundo.hitbox()):
            #personagem.velocidade = 0
        if personagem.hitbox().colliderect(inimigo.hitbox()):
            setor = 'game over'
        if personagem.hitbox().colliderect(bau.hitbox()):
            setor = 'game win'

        pygame.display.update()
        relogio_de_atualizacao.tick(ponteiro)

    while setor == 'game over':

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                setor = 'saida'

        #funcao de clicar
        if pygame.mouse.get_pos()[0] >= botao_repetir.posicao_x and pygame.mouse.get_pos()[1] >= botao_repetir.posicao_y and pygame.mouse.get_pos()[0] <= botao_repetir.posicao_x + botao_repetir.largura and pygame.mouse.get_pos()[1] <= botao_repetir.posicao_y + botao_repetir.altura:
            if pygame.mouse.get_pressed()[0]:
                personagem.pos_x = 224
                personagem.pos_y = 430
                setor = 'comeco'
        if pygame.mouse.get_pos()[0] >= botao_sair.posicao_x and pygame.mouse.get_pos()[1] >= botao_sair.posicao_y and pygame.mouse.get_pos()[0] <= botao_sair.posicao_x + botao_sair.largura and pygame.mouse.get_pos()[1] <= botao_sair.posicao_y + botao_sair.altura:
            if pygame.mouse.get_pressed()[0]:
                game_over = True
                setor = 'saida'

        para_background()
        para_dialogo(setor)

        pygame.display.update()
        relogio_de_atualizacao.tick(ponteiro)

    while setor == 'game win':

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                setor = 'saida'

        #funcao de clicar
        if pygame.mouse.get_pos()[0] >= botao_repetir.posicao_x and pygame.mouse.get_pos()[1] >= botao_repetir.posicao_y and pygame.mouse.get_pos()[0] <= botao_repetir.posicao_x + botao_repetir.largura and pygame.mouse.get_pos()[1] <= botao_repetir.posicao_y + botao_repetir.altura:
            if pygame.mouse.get_pressed()[0]:
                personagem.pos_x = 224
                personagem.pos_y = 430
                setor = 'comeco'
        if pygame.mouse.get_pos()[0] >= botao_sair.posicao_x and pygame.mouse.get_pos()[1] >= botao_sair.posicao_y and pygame.mouse.get_pos()[0] <= botao_sair.posicao_x + botao_sair.largura and pygame.mouse.get_pos()[1] <= botao_sair.posicao_y + botao_sair.altura:
            if pygame.mouse.get_pressed()[0]:
                game_over = True
                setor = 'saida'

        para_background()
        para_dialogo(setor)
        
        pygame.display.update()
        relogio_de_atualizacao.tick(ponteiro)