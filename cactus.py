import pygame, random

class Cacto:
    def __init__(self):
        self.velocidade = 10
        self.tamanho_x = random.choice(tamanho)
        self.tamanho_y = random.choice(tamanho)
        self.tamanho_xa = int(self.tamanho_x[1])
        self.tamanho_ya = int(self.tamanho_y[0])
        self.y = self.tamanho_y[2]
        self.x = 600
        self.rect = pygame.Rect(self.x, self.y, self.tamanho_xa, self.tamanho_ya)

    def movimentacao(self, dino):
        if self.x <= -20:
            self.tamanho_x = random.choice(tamanho)
            self.tamanho_y = random.choice(tamanho)
            self.tamanho_xa = self.tamanho_x[1]
            self.tamanho_ya = self.tamanho_y[0]
            self.y = self.tamanho_y[2]

        if dino.pixels_count // 10 > 10:
            self.x -= self.velocidade + random.randint(0, 8)
            if self.x <= -30:
                self.x = random.randint(600, 800)
                if self.velocidade < 30:
                    self.velocidade += 0.1


        
        self.rect = pygame.Rect(self.x, self.y, self.tamanho_xa, self.tamanho_ya)
          # Ajuste nas dimensões

    def desenhar(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.tamanho_xa, self.tamanho_ya))

    def colisao(self, dino):
        if self.rect.colliderect(dino.rect):
            pygame.quit()
            print(dino.pixels_count // 10)

tamanho = ((40, 20, 256), (60, 40,236), (70,60,226))
# y, x, pos_y
