#game.py
import pygame
from Saulo_prota import Saulo
from menu import Menu

LARGURA = 800
ALTURA = 400


class Jogo:

    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Ghost_Break")
        self.clock = pygame.time.Clock()
        self.player = Saulo(100, 300)

    def loop_jogo(self):

        rodando = True
        while rodando:

            self.clock.tick(60)
            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:
                    rodando = False

            teclas = pygame.key.get_pressed()
            self.player.update(teclas)
            self.tela.fill((30, 30, 30))

            pygame.draw.rect(
                self.tela,
                (100, 255, 100),
                (0, 360, 800, 40)
            )

            self.player.desenhar(self.tela)
            pygame.display.update()

        pygame.quit()

    def iniciar(self):

        menu = Menu(self)
        menu.executar()