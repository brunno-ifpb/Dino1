import pygame, l_principal
hitboxes = True
pygame.init() 
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("jogo do GALO")
try:
    l_principal.main(screen, clock, hitboxes)
except:
    pass
pygame.quit()
 