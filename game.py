import pygame
from Saulo_prota import Saulo
from menu import Menu

LARGURA = 800
ALTURA = 450

class Jogo:

    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Ghost_Break")
        self.clock = pygame.time.Clock()
        self.player = Saulo(100, 300)
        self.camera_x = 0
        self.chao_y = 410

    def loop_jogo(self):

        rodando = True
        while rodando:

            self.clock.tick(60)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

            teclas = pygame.key.get_pressed()
            self.player.update(teclas)
            self.camera_x = max(0, self.player.pos_x - 200)
            self.tela.fill((30, 30, 30))
            pygame.draw.rect(
                self.tela,
                (100, 255, 100),
                (-self.camera_x, self.chao_y, 5000, 40)
            )

            self.player.desenhar(self.tela, self.camera_x)

            pygame.display.update()

        pygame.quit()

    def iniciar(self):
        menu = Menu(self)
        menu.executar()