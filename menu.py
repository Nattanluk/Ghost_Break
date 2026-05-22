#menu.py
import pygame
import sys


class Menu:
    def __init__(self, jogo):
        self.jogo = jogo
        self.tela = jogo.tela
        self.fonte = pygame.font.SysFont("Arial", 50)
        self.botao_play = pygame.Rect(300, 180, 200, 80)
        self.botao_sair = pygame.Rect(300, 290, 200, 80)

    def desenhar_botao(self, rect, texto, cor, cor_hover):
        mouse = pygame.mouse.get_pos()
        if rect.collidepoint(mouse):
            cor_atual = cor_hover
        else:
            cor_atual = cor

        pygame.draw.rect(
            self.tela,
            cor_atual,
            rect,
            border_radius=15
        )

        texto_render = self.fonte.render(
            texto,
            True,
            (255, 255, 255)
        )

        texto_rect = texto_render.get_rect(
            center=rect.center
        )

        self.tela.blit(texto_render, texto_rect)

    def executar(self):

        while True:

            self.tela.fill((15, 15, 15))

            titulo = self.fonte.render(
                "GHOST BREAK",
                True,
                (255, 255, 255)
            )

            self.tela.blit(titulo, (240, 80))

            # botão play
            self.desenhar_botao(
                self.botao_play,
                "PLAY",
                (0, 120, 255),
                (0, 180, 255)
            )

            # botão sair
            self.desenhar_botao(
                self.botao_sair,
                "SAIR",
                (200, 50, 50),
                (255, 80, 80)
            )

            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.MOUSEBUTTONDOWN:

                    # PLAY
                    if self.botao_play.collidepoint(evento.pos):
                        self.jogo.loop_jogo()

                    # SAIR
                    if self.botao_sair.collidepoint(evento.pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
            self.jogo.clock.tick(60)