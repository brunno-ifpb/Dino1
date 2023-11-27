import pygame, l_principal
hitboxes = False
pygame.init() 
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
pygame.display.set_caption("jogo da GALINHA")
try:
    l_principal.main(screen, clock, hitboxes)
except:
    pass
pygame.quit()
