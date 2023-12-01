import pygame

from Imagem import Imagem


pygame.init()

# configuração de tela
largura_tela, altura_tela = 500, 500 # dimensões padrão
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('mover imagem')

# configurar imagem

obj_img = pygame.image.load('imagem_traços.png').convert_alpha()#novo
imagem = Imagem(obj_img)
imagem.largura, imagem.altura = imagem.obj.get_width(), imagem.obj.get_height()
imagem.pos_x = largura_tela/2 - imagem.largura/2 # coordenada x da imagem no centro
imagem.pos_y = altura_tela/2 - imagem.altura/2 # coordenada y da imagem no centro


cor_fundo = (50, 50, 50) # cor de fundo
tela.fill(cor_fundo) # pôr cor de fundo na tela
tela.blit(imagem.obj, (imagem.pos_x, imagem.pos_y)) # pôr imagem na tela


# precisa encontrar uma forma de rotacionar no eixo
#  X precisa encontrar uma forma de mover preservando a rotação/angulo - FEITO



while True:
    for evento in pygame.event.get(): # lista de eventos

        # eventos de teclado
        if evento.type == pygame.KEYDOWN:

            # eventos de translação

            if evento.key == pygame.K_UP: # mover para cima
                imagem.pos_y -= 10
                tela.fill(cor_fundo)
                nova_imagem = pygame.transform.rotate(imagem.obj, imagem.angulo) # manter rotação
                tela.blit(nova_imagem, (imagem.pos_x, imagem.pos_y))
            
            if evento.key == pygame.K_DOWN: # mover para baixo
                imagem.pos_y += 10
                tela.fill(cor_fundo)
                nova_imagem = pygame.transform.rotate(imagem.obj, imagem.angulo) # manter rotação
                tela.blit(nova_imagem, (imagem.pos_x, imagem.pos_y))

            if evento.key == pygame.K_LEFT: # mover para a esquerda
                imagem.pos_x -= 10
                tela.fill(cor_fundo)
                nova_imagem = pygame.transform.rotate(imagem.obj, imagem.angulo) # manter rotação
                tela.blit(nova_imagem, (imagem.pos_x, imagem.pos_y))

            if evento.key == pygame.K_RIGHT: # mover para a direita
                imagem.pos_x += 10
                tela.fill(cor_fundo)
                nova_imagem = pygame.transform.rotate(imagem.obj, imagem.angulo) # manter rotação
                tela.blit(nova_imagem, (imagem.pos_x, imagem.pos_y))


            # eventos de rotação

            if evento.key == pygame.K_a: # rotacionar sentido horário
                imagem.angulo -= 10
                tela.fill(cor_fundo)
                nova_imagem = pygame.transform.rotate(imagem.obj, imagem.angulo)
                tela.blit(nova_imagem, (imagem.pos_x, imagem.pos_y))
            
            if evento.key == pygame.K_d: # rotacionar sentido anti-horário
                imagem.angulo += 10
                tela.fill(cor_fundo)
                nova_imagem = pygame.transform.rotate(imagem.obj, imagem.angulo)
                tela.blit(nova_imagem, (imagem.pos_x, imagem.pos_y))



    pygame.display.flip() # renderizar

pygame.quit()