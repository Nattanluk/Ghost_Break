# menu.py
import pygame
import sys


class Menu:
    def __init__(self, jogo):
        self.jogo = jogo
        self.tela = jogo.tela
        self.fonte_1 = pygame.font.SysFont("Arial", 40)
        self.fonte_2 = pygame.font.SysFont("Arial", 20)
        self.fonte_creditos = pygame.font.SysFont("Arial", 24)
        largura_botao = 180
        altura_botao = 80
        self.botao_play = pygame.Rect(
            110, 300,
            largura_botao, altura_botao
        )

        self.botao_creditos = pygame.Rect(
            310, 300,
            largura_botao, altura_botao
        )

        self.botao_sair = pygame.Rect(
            510, 300,
            largura_botao, altura_botao
        )

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

        texto_render = self.fonte_2.render(
            texto,
            True,
            (255, 255, 255)
        )

        texto_rect = texto_render.get_rect(
            center=rect.center
        )

        self.tela.blit(texto_render, texto_rect)

    def tela_creditos(self):

        while True:

            self.tela.fill((15, 15, 15))

            titulo = self.fonte_2.render(
                "CREDITOS",
                True,
                (255, 255, 255)
            )

            texto1 = self.fonte_creditos.render(
                "Jogo: Ghost Break",
                True,
                (255, 255, 255)
            )

            texto2 = self.fonte_creditos.render(
                "Professor: Max Miller",
                True,
                (255, 255, 255)
            )

            texto3 = self.fonte_creditos.render(
                "Desenvolvedores:",
                True,
                (255, 255, 255)
            )

            texto4 = self.fonte_creditos.render(
                "Sofia Sabina Azevedo Nobrega",
                True,
                (255, 255, 255)
            )

            texto5 = self.fonte_creditos.render(
                "Nataniel M. Lucena dos Santos",
                True,
                (255, 255, 255)
            )

            texto6 = self.fonte_creditos.render(
                "Pressione qualquer tecla para voltar",
                True,
                (180, 180, 180)
            )

            self.tela.blit(titulo, titulo.get_rect(center=(400, 40)))
            self.tela.blit(texto1, texto1.get_rect(center=(400, 100)))
            self.tela.blit(texto2, texto2.get_rect(center=(400, 130)))
            self.tela.blit(texto3, texto3.get_rect(center=(400, 190)))
            self.tela.blit(texto4, texto4.get_rect(center=(400, 220)))
            self.tela.blit(texto5, texto5.get_rect(center=(400, 250)))

            self.tela.blit(texto6, texto6.get_rect(center=(400, 340)))

            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    return

            pygame.display.update()
            self.jogo.clock.tick(60)

    def executar(self):

        while True:

            self.tela.fill((15, 15, 15))

            titulo = self.fonte_1.render(
                "GHOST BREAK",
                True,
                (255, 255, 255)
            )

            titulo_rect = titulo.get_rect(center=(400, 150))
            self.tela.blit(titulo, titulo_rect)

            self.desenhar_botao(
                self.botao_play,
                "PLAY",
                (0, 120, 255),
                (0, 180, 255)
            )

            self.desenhar_botao(
                self.botao_creditos,
                "CRÉDITOS",
                (120, 0, 255),
                (180, 0, 255)
            )

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

                    if self.botao_play.collidepoint(evento.pos):
                        self.jogo.loop_jogo()

                    if self.botao_creditos.collidepoint(evento.pos):
                        self.tela_creditos()

                    if self.botao_sair.collidepoint(evento.pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
            self.jogo.clock.tick(60)