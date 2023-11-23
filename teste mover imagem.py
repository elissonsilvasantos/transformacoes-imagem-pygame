import pygame

pygame.init()

# configuração de tela
largura_tela, altura_tela = 500, 500 # dimensões padrão
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('mover imagem')

# configurar imagem
imagem = pygame.image.load('imagem_traços.png').convert_alpha()
larg_img, alt_img = imagem.get_width(), imagem.get_height()

pos_x = largura_tela/2 - larg_img/2
pos_y = altura_tela/2 - alt_img/2

cor_fundo = (50, 50, 50) # cor de fundo
tela.fill(cor_fundo) # pôr cor de fundo na tela
tela.blit(imagem, (pos_x, pos_y)) # pôr imagem na tela


func = True
while func:
    for evento in pygame.event.get(): # lista de eventos
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                pos_y -= 10
                tela.fill(cor_fundo)
                tela.blit(imagem, (pos_x, pos_y))
            
            if evento.key == pygame.K_DOWN:
                pos_y += 10
                tela.fill(cor_fundo)
                tela.blit(imagem, (pos_x, pos_y))

            if evento.key == pygame.K_LEFT:
                pos_x -= 10
                tela.fill(cor_fundo)
                tela.blit(imagem, (pos_x, pos_y))

            if evento.key == pygame.K_RIGHT:
                pos_x += 10
                tela.fill(cor_fundo)
                tela.blit(imagem, (pos_x, pos_y))

    pygame.display.flip() # renderizar



pygame.quit()