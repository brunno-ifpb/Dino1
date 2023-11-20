import pygame
import random

# teste

class Dino:
    def __init__(self):
        self.pulo = False
        self.caindo = False
        self.gravidade = 4
        self.x = 100
        self.y = 276
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.altura_do_pulo = 0
        self.pixels_count = 0
        self.font = pygame.font.Font(None, 36)
        self.velocidade = 10

    def pular(self):
        if not self.pulo and not self.caindo and self.y == 276:
            self.pulo = True
            self.altura_do_pulo = 10

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


    def movimentacao(self):
        keys = pygame.key.get_pressed()
        self.pixels_count += 1
        self.velocidade += 0.001

        if keys[pygame.K_SPACE]:
            self.pular()

        self.gravidades()

    def desenhar(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 20, 20))
        pixels_count_surface = self.font.render(str(self.pixels_count//10), True, (255, 255, 255)) # contador
        screen.blit(pixels_count_surface, (550, 10))  # desenha o objeto de superfície na tela

        

class Cacto:
    def __init__(self):
        self.x = 600
        self.y = 256
        self.velocidade = 10
        self.rect = pygame.Rect(self.x, self.y, 20, 20)

    def movimentacao(self):
        self.x -= self.velocidade + random.randint(0, 5)
        if self.x < -10:
            self.x = random.randint(600, 750)
            if self.velocidade < 30:
                self.velocidade += 0.1

    def desenhar(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 20, 40))

    def colisao(self, dino):
        if self.rect.colliderect(dino.rect):
            pygame.quit()

class Chao:
    def __init__(self):
        self.x = 0
        self.y = 300
        self.velocidade = 10

    def movimentacao(self):
        self.x -= self.velocidade
        if self.x < -600:
            self.x = 0

    def desenhar(self):
        pygame.draw.line(screen, (0, 255, 0), (self.x, self.y), (self.x + 1500, self.y), 10)

# Loop principal
def main():
    dino1 = Dino()
    cacto1 = Cacto()
    chao1 = Chao()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        dino1.movimentacao()
        cacto1.movimentacao()
        chao1.movimentacao()

        dino1.desenhar()
        cacto1.desenhar()
        chao1.desenhar()

        cacto1.colisao(dino1)

        pygame.display.flip()
        screen.fill((0, 0, 0))

pygame.init()

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
pygame.display.set_caption("Dino")

main()

pygame.quit()
