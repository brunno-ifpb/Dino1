import pygame

class Chao:
    def __init__(self):
        self.x = 0
        self.y = 300
        self.velocidade = 10

    def movimentacao(self):
        self.x -= self.velocidade
        if self.x < -600:
            self.x = 0

    def desenhar(self, screen):
        pygame.draw.line(screen, (255, 255, 0), (self.x, self.y), (self.x + 1500, self.y), 10)