import pygame

pygame.init()

LARGURA_TELA, ALTURA_TELA = 500, 500
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('rotacionar imagem')

imagem = pygame.image.load('imagem_traços.png').convert_alpha()
cor_fundo = (50, 50, 50)
tela.fill(cor_fundo)

# centralizar imagem
larg_img, alt_img = imagem.get_width(), imagem.get_height()
pos_x = LARGURA_TELA/2 - larg_img/2
pos_y = ALTURA_TELA/2 - alt_img/2


angulo = 0
tela.blit(imagem, (pos_x, pos_y))

rodando = True
while rodando:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                angulo -= 10

                tela.fill(cor_fundo)
                nova_imagem = pygame.transform.rotate(imagem, angulo)

                # centralizar imagem
                larg_img, alt_img = nova_imagem.get_width(), nova_imagem.get_height()
                pos_x = LARGURA_TELA/2 - larg_img/2
                pos_y = ALTURA_TELA/2 - alt_img/2

                tela.blit(nova_imagem, (pos_x, pos_y))

            if e.key == pygame.K_LEFT:
                angulo += 10

                tela.fill(cor_fundo)
                nova_imagem = pygame.transform.rotate(imagem, angulo)

                # centralizar imagem
                larg_img, alt_img = nova_imagem.get_width(), nova_imagem.get_height()
                pos_x = LARGURA_TELA/2 - larg_img/2
                pos_y = ALTURA_TELA/2 - alt_img/2

                tela.blit(nova_imagem, (pos_x, pos_y))


    pygame.display.flip()
    

pygame.quit()