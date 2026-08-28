
#menu.py
import pygame
import sys

from Telas.fase_concluida import FaseConcluida #tirar


class Menu:

    def __init__(self, jogo):

        self.jogo = jogo
        self.tela = jogo.tela
        self.fonte_1 = pygame.font.SysFont("Arial", 40, bold= True)
        self.fonte_2 = pygame.font.SysFont("Arial", 24)
        self.fonte_titulo_creditos = pygame.font.SysFont(
            "Arial",
            42,
            bold=True
        )

        self.fonte_creditos = pygame.font.SysFont(
            "Arial",
            24
        )

        self.fonte_destaque = pygame.font.SysFont(
            "Arial",
            28,
            bold=True
        )

        self.menu = FaseConcluida

        largura, altura = self.tela.get_size()

        # Imagem de fundo
        self.fundo = pygame.image.load("imagens/img_capa.png").convert()

        self.fundo = pygame.transform.scale(self.fundo,(largura, altura))

        # Tamanho dos botões
        largura_botao = 200
        altura_botao = 60

        # Botão JOGAR
        self.botao_play = pygame.Rect(300, 340, largura_botao, altura_botao)
        # Botão CRÉDITOS
        self.botao_creditos = pygame.Rect(80, 340, largura_botao, altura_botao)
        # Botão SAIR
        self.botao_sair = pygame.Rect(520, 340, largura_botao, altura_botao)

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

            # Fundo
            self.tela.blit(
                self.fundo,
                (0, 0)
            )

            # Fundo escuro transparente
            sombra = pygame.Surface(
                self.tela.get_size(),
                pygame.SRCALPHA
            )

            sombra.fill(
                (0, 0, 0, 170)
            )

            self.tela.blit(
                sombra,
                (0, 0)
            )

            # =========================
            # TÍTULO
            # =========================

            titulo = self.fonte_titulo_creditos.render(
                "CRÉDITOS",
                True,
                (255, 255, 255)
            )

            self.tela.blit(
                titulo,
                titulo.get_rect(
                    center=(400, 70)
                )
            )

            # =========================
            # INFORMAÇÕES
            # =========================

            textos = [

                ("GHOST BREAK", "titulo", 145),

                ("Desenvolvimento", "destaque", 210),

                ("Sofia Sabina Azevedo Nobrega", "normal", 250),

                ("Nataniel M. Lucena dos Santos", "normal", 285),

                ("Professor: Max Miller", "normal", 355),

                ("IFRN • Informática • 2º Ano 2M", "normal", 400),

            ]

            for texto, tipo, y in textos:

                if tipo == "titulo":

                    fonte = self.fonte_destaque

                elif tipo == "destaque":

                    fonte = self.fonte_destaque

                else:

                    fonte = self.fonte_creditos

                render = fonte.render(
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

            # =========================
            # VOLTAR
            # =========================

            voltar = self.fonte_creditos.render(
                "Pressione qualquer tecla para voltar",
                True,
                (200, 200, 200)
            )

            self.tela.blit(
                voltar,
                voltar.get_rect(
                    center=(400, 530)
                )
            )

            # =========================
            # EVENTOS
            # =========================

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

                        self.jogo.reiniciar_jogo()
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
