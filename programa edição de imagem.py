import pygame

from Imagem import Imagem


pygame.init()

# configuração de tela
largura_tela, altura_tela = 500, 500 # dimensões padrão
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Programa Edição de Imagem')

# configurar imagem

obj_img = pygame.image.load('imagem_traços.png').convert_alpha()#novo
imagem = Imagem(obj_img)
imagem.largura, imagem.altura = imagem.obj.get_width(), imagem.obj.get_height()
imagem.pos_x = largura_tela/2 - imagem.largura/2 # coordenada x da imagem no centro
imagem.pos_y = altura_tela/2 - imagem.altura/2 # coordenada y da imagem no centro


cor_fundo = (50, 50, 50) # cor de fundo
tela.fill(cor_fundo) # pôr cor de fundo na tela
tela.blit(imagem.obj, (imagem.pos_x, imagem.pos_y)) # pôr imagem na tela


# erro translação x rotação (menor): precisa encontrar uma forma de rotacionar no eixo

# erro rotação x escala (menor): movendo de forma incorreta quando troca entre as transformações

# [resolvido] erro rotação x escala (MAIOR): quando faz rotação e depois escala, a escala desconsidera o grau

# erro rotação x escala (MAIOR): quando faz rotação, escala e rotação denovo, rotação deixa tamanho errado

# erro rotação x escala (MAIOR): quando faz rotação 90 e depois escala, o altura é trocado por largura

print('COMANDOS')
print('mover imagem: [seta-esquerda, seta-direita, seta-cima, seta-baixo]')
print('rotacionar imagem: [a, d]')
print('aumentar/diminuir: [w, s]')

while True:
    for evento in pygame.event.get(): # lista de eventos

        # eventos de teclado
        if evento.type == pygame.KEYDOWN:

            # eventos de translação

            if evento.key == pygame.K_UP: # mover para cima
                imagem.pos_y -= 10
                tela.fill(cor_fundo)
                nova_imagem = pygame.transform.rotate(imagem.obj, imagem.angulo) # manter rotação
                # manter escala
                imagem.largura = nova_imagem.get_width()
                imagem.altura = nova_imagem.get_height()
                nova_imagem = pygame.transform.scale(nova_imagem, (imagem.largura, imagem.altura)) 
                tela.blit(nova_imagem, (imagem.pos_x, imagem.pos_y))
            
            if evento.key == pygame.K_DOWN: # mover para baixo
                imagem.pos_y += 10
                tela.fill(cor_fundo)
                nova_imagem = pygame.transform.rotate(imagem.obj, imagem.angulo) # manter rotação
                # manter escala
                imagem.largura = nova_imagem.get_width()
                imagem.altura = nova_imagem.get_height()
                nova_imagem = pygame.transform.scale(nova_imagem, (imagem.wlargura, imagem.altura)) 
                tela.blit(nova_imagem, (imagem.pos_x, imagem.pos_y))

            if evento.key == pygame.K_LEFT: # mover para a esquerda
                imagem.pos_x -= 10
                tela.fill(cor_fundo)
                nova_imagem = pygame.transform.rotate(imagem.obj, imagem.angulo) # manter rotação
                # manter escala
                imagem.largura = nova_imagem.get_width()
                imagem.altura = nova_imagem.get_height()
                nova_imagem = pygame.transform.scale(nova_imagem, (imagem.largura, imagem.altura)) 
                tela.blit(nova_imagem, (imagem.pos_x, imagem.pos_y))

            if evento.key == pygame.K_RIGHT: # mover para a direita
                imagem.pos_x += 10
                tela.fill(cor_fundo)
                nova_imagem = pygame.transform.rotate(imagem.obj, imagem.angulo) # manter rotação
                # manter escala
                imagem.largura = nova_imagem.get_width()
                imagem.altura = nova_imagem.get_height()
                nova_imagem = pygame.transform.scale(nova_imagem, (imagem.largura, imagem.altura)) 
                tela.blit(nova_imagem, (imagem.pos_x, imagem.pos_y))


            # eventos de rotação

            if evento.key == pygame.K_a: # rotacionar sentido horário
                imagem.angulo -= 10
                tela.fill(cor_fundo)
                nova_imagem = pygame.transform.rotate(imagem.obj, imagem.angulo)
                imagem.largura = nova_imagem.get_width()
                imagem.altura = nova_imagem.get_height()
                nova_imagem = pygame.transform.scale(nova_imagem, (imagem.largura, imagem.altura))
                tela.blit(nova_imagem, (imagem.pos_x, imagem.pos_y))
            
            if evento.key == pygame.K_d: # rotacionar sentido anti-horário
                imagem.angulo += 10
                tela.fill(cor_fundo)
                nova_imagem = pygame.transform.rotate(imagem.obj, imagem.angulo)
                imagem.largura = nova_imagem.get_width()
                imagem.altura = nova_imagem.get_height()
                nova_imagem = pygame.transform.scale(nova_imagem, (imagem.largura, imagem.altura))
                tela.blit(nova_imagem, (imagem.pos_x, imagem.pos_y))


            # eventos de escala

            if evento.key == pygame.K_w: # aumentar
                imagem.largura += 50
                imagem.altura += 50
                # para permanecer no centro
                imagem.pos_x -= 25
                imagem.pos_y -= 25
                tela.fill((50, 50, 50)) # apagar tudo

                

                # manter rotação
                nova_imagem = pygame.transform.scale(imagem.obj, (imagem.largura, imagem.altura))
                nova_imagem = pygame.transform.rotate(nova_imagem, imagem.angulo)
                tela.blit(nova_imagem, (imagem.pos_x, imagem.pos_y))

                '''
                print('-'*30)
                print('largura teorica: ', imagem.largura)
                print('largura real:', nova_imagem.get_width())
                print('altura teorica:', imagem.altura)
                print('altura real:', nova_imagem.get_height())
                '''
            
            if evento.key == pygame.K_s:
                imagem.largura -= 50
                imagem.altura -= 50
                # para permanecer no centro
                imagem.pos_x += 25
                imagem.pos_y += 25
                tela.fill((50, 50, 50)) # apagar tudo

                # manter rotação
                nova_imagem = pygame.transform.scale(imagem.obj, (imagem.largura, imagem.altura))
                nova_imagem = pygame.transform.rotate(nova_imagem, imagem.angulo)
                tela.blit(nova_imagem, (imagem.pos_x, imagem.pos_y))


    pygame.display.flip() # renderizar

pygame.quit()