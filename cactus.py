import pygame, random

class Cacto:
    def __init__(self):
        self.x = 600
        self.y = 256
        self.velocidade = 10
        self.rect = pygame.Rect(self.x, self.y, 10, 40)

    def movimentacao(self, dino):
        if dino.pixels_count // 10 > 10:
            self.x -= self.velocidade + random.randint(0, 8)
            if self.x < -15:
                self.x = random.randint(600, 750)
                if self.velocidade < 30:
                    self.velocidade += 0.1
        
        self.rect = pygame.Rect(self.x, self.y, 10, 40) 

    def desenhar(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 10, 40))

    def colisao(self, dino):
        if self.rect.colliderect(dino.rect):
            print(f"Você perdeu! Sua pontuação foi de: {dino.pixels_count//10} pontos")
            pygame.quit()

class Cacto_grande:
    def __init__(self):
        self.x = 600
        self.y = 236
        self.velocidade = 10
        self.rect = pygame.Rect(self.x, self.y, 10, 60)

    def movimentacao(self, dino):
        if dino.pixels_count // 10 > 10:
            self.x -= self.velocidade + random.randint(0, 8)
            if self.x < -15:
                self.x = random.randint(600, 750)
                if self.velocidade < 30:
                    self.velocidade += 0.1
        
        self.rect = pygame.Rect(self.x, self.y, 10, 80)  # Ajuste nas dimensões

    def desenhar(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 10, 60))

    def colisao(self, dino):
        if self.rect.colliderect(dino.rect):
            print(f"Você perdeu! Sua pontuação foi de: {dino.pixels_count//10} pontos")
            pygame.quit()

def random_def():
    if random.randint(0, 1) == 0:
        return Cacto()
    else:
        return Cacto_grande()
