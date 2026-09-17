import pygame
import sys


class SelecaoNiveis:

    def __init__(self, jogo):
        self.jogo = jogo
        self.tela = jogo.tela

        self.fonte = pygame.font.SysFont(
            "Arial",
            28,
            bold=True
        )

        self.botao_nivel_1 = pygame.Rect(
            300,
            200,
            200,
            60
        )

        self.fundo = pygame.image.load(
            "imagens/fases.jpg"
        ).convert()

        self.fundo = pygame.transform.scale(
            self.fundo,
            (700, 500)
        )

    def executar(self):

        while True:

            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.MOUSEBUTTONDOWN:

                    if self.botao_nivel_1.collidepoint(
                        evento.pos
                    ):
                        self.jogo.reiniciar_jogo()
                        return self.jogo.loop_jogo()

            self.tela.blit(
                self.fundo,
                (50, 50)
            )

            pygame.draw.rect(
                self.tela,
                (0, 0, 0),
                self.botao_nivel_1,
                border_radius=15
            )

            pygame.draw.rect(
                self.tela,
                (255, 255, 255),
                self.botao_nivel_1,
                2,
                border_radius=15
            )

            texto = self.fonte.render(
                "NÍVEL 1",
                True,
                (255, 255, 255)
            )

            texto_rect = texto.get_rect(
                center=self.botao_nivel_1.center
            )

            self.tela.blit(
                texto,
                texto_rect
            )

            pygame.display.flip()

            self.jogo.clock.tick(60)