import player, cactus, chao, pygame, random

# Loop principal
def main():
    try:
        dino1 = player.Dino()
        cacto1 = cactus.Cacto()
        chao1 = chao.Chao()

        while True:
            
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            dino1.movimentacao()
            cacto1.movimentacao(dino1)
            chao1.movimentacao()

            dino1.desenhar(screen)
            cacto1.desenhar(screen)
            chao1.desenhar(screen)

            cacto1.colisao(dino1)

            pygame.display.flip()
            screen.fill((0, 0, 0))
    except:
         pass

pygame.init()

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
pygame.display.set_caption("Dino")

main()

pygame.quit()
