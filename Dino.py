import pygame
import os

class Dino:
    def __init__(self):
        self.pulo = False
        self.caindo = False
        self.gravidade = 8
        self.x = 100
        self.y = 276
        self.p = 0
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.altura_do_pulo = 0
        self.pixels_count = 0
        self.font = pygame.font.Font(None, 36)
        self.velocidade = 15
        self.sprite = pygame.image.load('sprites/t-rex-0.png')
        

    def pular(self):
        if not self.pulo and not self.caindo and self.y == 276:
            self.pulo = True
            self.altura_do_pulo = 14

    def gravidades(self):
        if self.pulo and self.altura_do_pulo > 0:
            self.y -= 10
            self.altura_do_pulo -= 1
        else:
            self.caindo = True
            if self.y < 276:
                self.y += self.gravidade
            else:
                self.y = 276
                self.pulo = False
                self.caindo = False
        self.rect.y = self.y

    def movimentacao(self ):
        keys = pygame.key.get_pressed()
        if self.pixels_count % 1000 == 0:
            self.p += 0.5
        self.pixels_count += 1 + self.p
        self.velocidade += 0.001
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            
            self.pular()
        self.gravidades()

    def desenhar(self, screen, hitboxes):
        # Desenha o quadrado
        if hitboxes == True:
            pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 20, 20))
        #desenha dino
        screen.blit(self.sprite, (self.x, self.y))
        #desenha o contador
        pixels_count_surface = self.font.render(str(int(self.pixels_count//10)), True, (0,0,0))

        screen.blit(pixels_count_surface, (550, 10))

    def pontuacao(self):
        with open("point.txt", "a") as f:
            f.write(f"{int(self.pixels_count//10)} \n" )
