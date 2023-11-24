import pygame, l_principal
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
pygame.display.set_caption("Dino")
l_principal.main(screen, clock)
pygame.quit()
