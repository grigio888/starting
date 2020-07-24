import pygame

from complementos.entidades import *
from complementos.exibir_imagem_estatica import *


# Carregando Modulos:

# Configurando a tela:
tela_largura_altura = (500, 500)
tela = pygame.display.set_mode(tela_largura_altura)
pygame.display.set_caption("Road Cross")

# -> Variaveis globais:
game_over = False
setor = 'inicio'
fundo = Fundo('imagens/background.png', 0, 0, 500, 500)
botao_start = ExibirImagemEstatica('imagens/janelas/botao_start.png', 205, 287, 100, 23)
botao_repetir = ExibirImagemEstatica('imagens/janelas/botao_repetir.png', 205, 287, 100, 23)
botao_sair = ExibirImagemEstatica('imagens/janelas/botao_sair.png', 205, 333, 100, 23)

# -> Variaveis setor == 'inicio':
dialogo_sup = ExibirImagemEstatica('imagens/janelas/dialogo_comeco.png', 100, 105, 300, 150)

# -> Variaveis setor == 'comeco':
personagem = Personagem(224, 430, 63, 63, 4)
inimigo = Inimigo(233, 255, 63, 63, 4)
bau = Bau(230, 50, 40, 40, 0)

# -> Variaveis setor == 'game over':
img_game_over = ExibirImagemEstatica('imagens/janelas/game_over.png', 105, 155, 300, 85)

# -> Variaveis setor == 'game win':
img_game_win = ExibirImagemEstatica('imagens/janelas/game_win.png', 105, 155, 300, 85)


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