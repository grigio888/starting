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
# |-> Entidades:
personagem = Personagem(224, 430, 63, 63, 4)
inimigo = Inimigo(233, 255, 63, 63, 4)
inimigo2 = Inimigo(100, 150, 63, 63, 10) 
bau = Bau(230, 50, 40, 40, 0)
# |-> Obstaculos:
pos_arv_x = [-60, -5, -55, 0, 370, 430, 385, 450]
arv_esq_1 = ArvoreGrandeA(pos_arv_x[3], -70)
arv_esq_2 = ArvoreGrandeB(pos_arv_x[0], -20)
arv_esq_3 = ArvoreGrandeA(pos_arv_x[2], 30)
arv_esq_4 = ArvoreGrandeB(pos_arv_x[0], 80)
arv_esq_5 = ArvoreGrandeA(pos_arv_x[1], 80)
arv_esq_6 = ArvoreGrandeB(pos_arv_x[2], 130)
arv_esq_7 = ArvoreGrandeA(pos_arv_x[0], 180)
arv_esq_8 = ArvoreGrandeB(pos_arv_x[2], 230)
arv_esq_9 = ArvoreGrandeA(pos_arv_x[3], 230)
arv_esq_10 = ArvoreGrandeB(pos_arv_x[0], 280)
arv_esq_11 = ArvoreGrandeA(pos_arv_x[2], 330)

arv_dir_1 = ArvoreGrandeA(pos_arv_x[6], -70)
arv_dir_2 = ArvoreGrandeB(pos_arv_x[4], -20)
arv_dir_3 = ArvoreGrandeA(pos_arv_x[5], 30)
arv_dir_4 = ArvoreGrandeB(pos_arv_x[7], 80)
arv_dir_5 = ArvoreGrandeA(pos_arv_x[4], 80)
arv_dir_6 = ArvoreGrandeB(pos_arv_x[7], 130)
arv_dir_7 = ArvoreGrandeA(pos_arv_x[5], 180)
arv_dir_8 = ArvoreGrandeB(pos_arv_x[7], 230)
arv_dir_9 = ArvoreGrandeA(pos_arv_x[6], 230)
arv_dir_10 = ArvoreGrandeB(pos_arv_x[5], 280)
arv_dir_11 = ArvoreGrandeA(pos_arv_x[7], 330)

caixa_esq_1 = CaixaInteira(85, 75)
caixa_esq_2 = CaixaInteira(155, 75)
caixa_esq_3 = CaixaQuebrada(115, 65)
caixa_dir_1 = CaixaInteira(285, 75)
caixa_dir_2 = CaixaInteira(355, 75)
caixa_dir_3 = CaixaQuebrada(315, 65)


lista_de_colisoes = [arv_esq_1.hitbox(),
                    arv_esq_2.hitbox(),
                    arv_esq_3.hitbox(),
                    arv_esq_4.hitbox(),
                    arv_esq_5.hitbox(),
                    arv_esq_6.hitbox(),
                    arv_esq_7.hitbox(),
                    arv_esq_8.hitbox(),
                    arv_esq_9.hitbox(),
                    arv_esq_10.hitbox(),
                    arv_esq_11.hitbox(),
                    arv_dir_1.hitbox(),
                    arv_dir_2.hitbox(),
                    arv_dir_3.hitbox(),
                    arv_dir_4.hitbox(),
                    arv_dir_5.hitbox(),
                    arv_dir_6.hitbox(),
                    arv_dir_7.hitbox(),
                    arv_dir_8.hitbox(),
                    arv_dir_9.hitbox(),
                    arv_dir_10.hitbox(),
                    arv_dir_11.hitbox(),
                    caixa_esq_1.hitbox(),
                    caixa_esq_2.hitbox(),
                    caixa_esq_3.hitbox(),
                    caixa_dir_1.hitbox(),
                    caixa_dir_2.hitbox(),
                    caixa_dir_3.hitbox()]



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

    inimigo2.movimentacao(tela_largura_altura)
    inimigo2.contador_frames += 1
    inimigo2.animacao()
    inimigo2.desenho(tela)

def para_bau():
    bau.contador_frames += 1
    bau.animacao()
    bau.desenho(tela)

def para_arvores():
    arv_esq_1.desenho(tela)
    arv_esq_2.desenho(tela)
    arv_esq_3.desenho(tela)

    arv_esq_4.desenho(tela)
    arv_esq_5.desenho(tela)
    arv_esq_6.desenho(tela)
    arv_esq_7.desenho(tela)
    arv_esq_8.desenho(tela)
    arv_esq_9.desenho(tela)
    arv_esq_10.desenho(tela)
    arv_esq_11.desenho(tela)
    arv_dir_1.desenho(tela)
    arv_dir_2.desenho(tela)
    arv_dir_3.desenho(tela)
    arv_dir_4.desenho(tela)
    arv_dir_5.desenho(tela)
    arv_dir_6.desenho(tela)
    arv_dir_7.desenho(tela)
    arv_dir_8.desenho(tela)
    arv_dir_9.desenho(tela)
    arv_dir_10.desenho(tela)
    arv_dir_11.desenho(tela)
    
def para_caixas():
    caixa_esq_1.desenho(tela)
    caixa_esq_2.desenho(tela)
    caixa_esq_3.desenho(tela)
    caixa_dir_1.desenho(tela)
    caixa_dir_2.desenho(tela)
    caixa_dir_3.desenho(tela)
