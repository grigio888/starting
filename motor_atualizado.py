# Importando Modulos:
import pygame
from complementos.exibir_imagem_estatica import *
from complementos.entidades import *

# Iniciando pygame:
pygame.init()

# Carregando Modulos:
# -> Variaveis globais:
game_over = False
setor = 'inicio'
fundo = ExibirImagemEstatica('imagens/background.png', 0, 0, 500, 500)
botao_start = ExibirImagemEstatica('imagens/janelas/botao_start.png', 205, 287, 100, 23)
botao_repetir = ExibirImagemEstatica('imagens/janelas/botao_repetir.png', 205, 287, 100, 23)
botao_sair = ExibirImagemEstatica('imagens/janelas/botao_sair.png', 205, 333, 100, 23)
# -> Variaveis setor == 'inicio':
dialogo_sup = ExibirImagemEstatica('imagens/janelas/dialogo_comeco.png', 100, 105, 300, 150)
# -> Variaveis setor == 'comeco':
personagem = Personagem(224, 430, 63, 63, 4)
inimigo = Inimigo(233, 255, 63, 63, 4)
bau = Bau(233, 50, 32, 32, 0)
# -> Variaveis setor == 'game over':
img_game_over = ExibirImagemEstatica('imagens/janelas/game_over.png', 105, 155, 300, 85)
# -> Variaveis setor == 'game win':
img_game_win = ExibirImagemEstatica('imagens/janelas/game_win.png', 105, 155, 300, 85)

# Configurando a tela:
tela_largura_altura = (500, 500)
tela = pygame.display.set_mode(tela_largura_altura)
pygame.display.set_caption('Testando')

# Configurando a atualização:
relogio_de_atualizacao = pygame.time.Clock()
ponteiro = 30

# Definindo Inicializadores
def para_background():
    fundo.desenho(tela)

def para_dialogo(qual):
    if qual == 'inicio':
        dialogo_sup.desenho(tela)
        botao_start.desenho(tela)
        botao_sair.desenho(tela)
    if qual == 'game over':
        img_game_over.desenho(tela)
        botao_repetir.desenho(tela)
        botao_sair.desenho(tela)
    if qual == 'game win':
        img_game_win.desenho(tela)
        botao_repetir.desenho(tela)
        botao_sair.desenho(tela)

def para_personagem():
    chave = pygame.key.get_pressed()
    personagem.movimentacao(chave)
    personagem.contador_frames += 1
    personagem.animacao()
    personagem.desenho(tela)

def para_inimigo():
    inimigo.movimentacao(tela_largura_altura)
    inimigo.contador_frames += 1
    inimigo.animacao()
    inimigo.desenho(tela)

def para_bau():
    bau.contador_frames += 1
    bau.animacao()
    bau.desenho(tela)

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
        
        para_background()
        para_bau()
        para_personagem()
        para_inimigo()

        colisao_inimigo = personagem.detectar_colisao(inimigo)
        colisao_bau = personagem.detectar_colisao(bau)
        if colisao_inimigo == True:
            setor = 'game over'
        if colisao_bau == True:
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