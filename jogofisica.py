import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
x_retangulo = largura // 2 - 30
y_retangulo = altura // 2 - 40

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo Lei de Newton')

carro_img = pygame.image.load('carro.png')
carro_img = pygame.transform.scale(carro_img, (80, 80))
carro_rect = carro_img.get_rect()

velocidade_tela = 5
tempo_inicial = 0
aceleracao = 0.0
massa = 1980
v_final = 0

tempotela = 0.0

fonte = pygame.font.Font(None, 36)

x_botao_esquerda = 20
y_botao = altura // 2 + 60  # Centralizando o botão verticalmente
largura_botao = 90
altura_botao = 40

x_botao_direita = 150
x_botao_stop = 280
y_botao_stop = altura // 2 + 60  # Centralizando o botão verticalmente
largura_botao_stop = 90
altura_botao_stop = 40

clock = pygame.time.Clock()

jogo_ativo = True

while jogo_ativo:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == MOUSEBUTTONDOWN:
            if x_botao_esquerda <= event.pos[0] <= x_botao_esquerda + largura_botao and \
                    y_botao <= event.pos[1] <= y_botao + altura_botao:
                velocidade_tela += 1
            elif x_botao_direita <= event.pos[0] <= x_botao_direita + largura_botao and \
                    y_botao <= event.pos[1] <= y_botao + altura_botao:
                velocidade_tela -= 1
            elif x_botao_stop <= event.pos[0] <= x_botao_stop + largura_botao_stop and \
                    y_botao_stop <= event.pos[1] <= y_botao_stop + altura_botao_stop:
                jogo_ativo = False

    x_retangulo += velocidade_tela  # Multiplica pela aceleração para o movimento contínuo

    tela.fill((200, 200, 200))

    #pygame.draw.rect(tela, (255, 255, 0), (x_retangulo, y_retangulo, 80, 80))
    #texto = fonte.render('Bloco', True, (0, 0, 0))
    tela.blit(carro_img, (x_retangulo + 6, y_retangulo + 20))

    pygame.draw.line(tela, (0, 0, 0), (0, y_retangulo + 80), (largura, y_retangulo + 80), 2)

    pygame.draw.rect(tela, (0, 255, 0), (x_botao_esquerda, y_botao, largura_botao, altura_botao))
    texto_botao_esquerda = fonte.render('+ V', True, (0, 0, 0))
    tela.blit(texto_botao_esquerda, (x_botao_esquerda + 5, y_botao + 5))

    pygame.draw.rect(tela, (255, 0, 0), (x_botao_direita, y_botao, largura_botao, altura_botao))
    texto_botao_direita = fonte.render('- V', True, (0, 0, 0))
    tela.blit(texto_botao_direita, (x_botao_direita + 5, y_botao + 5))

    pygame.draw.rect(tela, (0, 0, 170), (x_botao_stop, y_botao_stop, largura_botao_stop, altura_botao_stop))
    texto_botao_stop = fonte.render('Stop!', True, (0, 0, 0))
    tela.blit(texto_botao_stop, (x_botao_stop + 5, y_botao_stop + 5))

    if x_retangulo >= largura and velocidade_tela > 0:
        if tempo_inicial > 0:
            tempo_passado = pygame.time.get_ticks() - tempo_inicial
            tempo_passado = tempo_passado / 1000
            tempo_passado = round(tempo_passado, 2)
            aceleracao = (velocidade_tela - v_final)  / tempo_passado
            tempotela = tempo_passado
            v_final = velocidade_tela
        else:
            aceleracao = (velocidade_tela - v_final)  / (pygame.time.get_ticks() / 1000)
            tempotela = pygame.time.get_ticks() / 1000
            v_final = velocidade_tela
        tempo_inicial = pygame.time.get_ticks()
        x_retangulo = -20

    if x_retangulo <= -20 and velocidade_tela < 0:
        if tempo_inicial > 0:
            tempo_passado = pygame.time.get_ticks() - tempo_inicial
            tempo_passado = tempo_passado / 1000
            tempo_passado = round(tempo_passado, 2)
            aceleracao = (velocidade_tela - v_final) / tempo_passado
            tempotela = tempo_passado
            v_final = velocidade_tela
        else:
            aceleracao = (velocidade_tela - v_final)  / (pygame.time.get_ticks() / 1000)
            tempotela = pygame.time.get_ticks() / 1000
            v_final = velocidade_tela
        tempo_inicial = pygame.time.get_ticks()
        x_retangulo = largura

    # Calcula a força usando F = m * a
    forca = massa * aceleracao

    cinetica = (massa * (v_final**2)) / 2

    texto_aceleracao = fonte.render(f'Aceleração: {aceleracao:.2f} m/s²', True, (0, 0, 0))
    tela.blit(texto_aceleracao, (20, 20))  # Posicione a caixa de texto acima do bloco
    texto_aceleracao = fonte.render(f'Tempo: {tempotela:.2f} s', True, (0, 0, 0))
    tela.blit(texto_aceleracao, (350, 20))  # Posicione a caixa de texto acima do bloco

    texto_velocidade = fonte.render(f'Velocidade: {velocidade_tela} m/s', True, (0, 0, 0))
    tela.blit(texto_velocidade, (20, 60))  # Adiciona o texto de velocidade

    texto_forca = fonte.render(f'F = {massa} kg x {aceleracao:.2f} m/s² = {forca:.2f} N', True, (0, 0, 0))
    tela.blit(texto_forca, (20, 100))  # Ajuste a posição conforme necessário

    texto_kfinal = fonte.render(f'K = (m x v^2) / 2 = {cinetica} J, Vfinal = {v_final} m/s', True, (0, 0, 0))
    tela.blit(texto_kfinal, (20, 380))  # Ajuste a posição conforme necessário

    pygame.display.update()
    clock.tick(30)
