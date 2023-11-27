import dino, chao, pygame, cactus
def main(screen, clock, hitboxes):
        dino1 = dino.Dino()
        cacto1 = cactus.Cacto()
        chao1 = chao.Chao()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #funções principais
            dino1.movimentacao() 
            cacto1.movimentacao(dino1)
            chao1.movimentacao()

            dino1.desenhar(screen, hitboxes)
            cacto1.desenhar(screen)
            chao1.desenhar(screen)

            cacto1.colisao(dino1)

            pygame.display.flip()
            screen.fill((0, 0, 255))
