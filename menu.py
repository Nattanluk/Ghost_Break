import pygame
import sys


class Menu:

    def __init__(self, jogo):

        self.jogo = jogo
        self.tela = jogo.tela
        self.fonte_1 = pygame.font.SysFont("Arial", 40, bold= True)
        self.fonte_2 = pygame.font.SysFont("Arial", 24)
        self.fonte_creditos = pygame.font.SysFont("Arial", 24)

        largura, altura = self.tela.get_size()

        # Imagem de fundo
        self.fundo = pygame.image.load(
            "imagens/img_capa.png"
        ).convert()

        self.fundo = pygame.transform.scale(
            self.fundo,
            (largura, altura)
        )

        # Tamanho dos botões
        largura_botao = 200
        altura_botao = 60

        # Botão JOGAR
        self.botao_play = pygame.Rect(
            300,
            340,
            largura_botao,
            altura_botao
        )

        # Botão CRÉDITOS
        self.botao_creditos = pygame.Rect(
            80,
            340,
            largura_botao,
            altura_botao
        )

        # Botão SAIR
        self.botao_sair = pygame.Rect(
            520,
            340,
            largura_botao,
            altura_botao
        )

    def desenhar_botao(self, rect, texto):

        mouse = pygame.mouse.get_pos()

        # Muda a cor quando o mouse passa por cima
        if rect.collidepoint(mouse):
            cor = (120, 70, 255, 220)

        else:
            cor = (0, 0, 0, 170)

        superficie = pygame.Surface(
            (rect.width, rect.height),
            pygame.SRCALPHA
        )

        pygame.draw.rect(
            superficie,
            cor,
            superficie.get_rect(),
            border_radius=15
        )

        pygame.draw.rect(
            superficie,
            (255, 255, 255),
            superficie.get_rect(),
            2,
            border_radius=15
        )

        self.tela.blit(
            superficie,
            rect.topleft
        )

        texto_render = self.fonte_2.render(
            texto,
            True,
            (255, 255, 255)
        )

        texto_rect = texto_render.get_rect(
            center=rect.center
        )

        self.tela.blit(
            texto_render,
            texto_rect
        )

    def tela_creditos(self):

        while True:

            self.tela.blit(
                self.fundo,
                (0, 0)
            )

            sombra = pygame.Surface(
                (800, 600),
                pygame.SRCALPHA
            )

            sombra.fill(
                (0, 0, 0, 10)
            )

            self.tela.blit(
                sombra,
                (0, 0)
            )

            textos = [
                ("CRÉDITOS", 40),
                ("Jogo: Ghost Break", 120),
                ("Professor: Max Miller", 160),
                ("Desenvolvedores:", 240),
                ("Sofia Sabina Azevedo Nobrega", 280),
                ("Nataniel M. Lucena dos Santos", 320),
                ("Pressione qualquer tecla para voltar", 520),
            ]

            for texto, y in textos:

                render = self.fonte_creditos.render(
                    texto,
                    True,
                    (255, 255, 255)
                )

                self.tela.blit(
                    render,
                    render.get_rect(
                        center=(400, y)
                    )
                )

            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:

                    return

            pygame.display.flip()

            self.jogo.clock.tick(60)

    def executar(self):

        while True:

            # Desenha o fundo
            self.tela.blit(
                self.fundo,
                (0, 0)
            )

            sombra = pygame.Surface(
                (800, 600),
                pygame.SRCALPHA
            )

            sombra.fill(
                (0, 0, 0, 0)
            )

            self.tela.blit(
                sombra,
                (0, 0)
            )

            # Desenha os botões
            self.desenhar_botao(
                self.botao_play,
                "JOGAR"
            )

            self.desenhar_botao(
                self.botao_creditos,
                "CRÉDITOS"
            )

            self.desenhar_botao(
                self.botao_sair,
                "SAIR"
            )

            # Verifica os eventos
            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.MOUSEBUTTONDOWN:

                    # JOGAR
                    if self.botao_play.collidepoint(
                        evento.pos
                    ):

                        resultado = self.jogo.loop_jogo()

                        # Se o jogo pediu para fechar
                        if resultado == "sair":

                            pygame.quit()
                            sys.exit()

                        # Se resultado for "menu",
                        # simplesmente continua o while
                        # e o menu aparece novamente.

                    # CRÉDITOS
                    elif self.botao_creditos.collidepoint(
                        evento.pos
                    ):

                        self.tela_creditos()

                    # SAIR
                    elif self.botao_sair.collidepoint(
                        evento.pos
                    ):

                        pygame.quit()
                        sys.exit()

            pygame.display.flip()

            self.jogo.clock.tick(60)