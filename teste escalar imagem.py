import pygame

pygame.init()

LARGURA_TELA, ALTURA_TELA = 500, 500
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('escalar imagem')

imagem = pygame.image.load('img-teste.png')
tela.fill((50, 50, 50))
pos_x = 200
pos_y = 200
tela.blit(imagem, (pos_x, pos_y))

larg_img, alt_img = imagem.get_width(), imagem.get_height()

LARG_MIN, ALT_MIN = 50, 50

while True:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP: # aumentar a imagem
                larg_img += 50
                alt_img += 50
                pos_x -= 25
                pos_y -= 25
                tela.fill((50, 50, 50)) # apagar tudo
                nova_imagem = pygame.transform.scale(imagem, (larg_img, alt_img))
                tela.blit(nova_imagem, (pos_x, pos_y))

            if e.key == pygame.K_DOWN:
                if (larg_img > LARG_MIN and alt_img > ALT_MIN):
                    larg_img -= 50
                    alt_img -= 50
                    pos_x += 25
                    pos_y += 25
                    tela.fill((50, 50, 50)) # apagar tudo
                    nova_imagem = pygame.transform.scale(imagem, (larg_img, alt_img))
                    tela.blit(nova_imagem, (pos_x, pos_y))
    
    pygame.display.flip()
    


pygame.quit()