#desenho_jogo.py
import pygame

from configuracoes import *


class DesenhoJogo:

    def __init__(self, jogo):

        self.jogo = jogo
        self.tela = jogo.tela

        self.fonte_mensagem = pygame.font.SysFont(
            "Arial",
            24,
            bold=True
        )


    def desenhar(self):

        self.desenhar_fundo()

        self.desenhar_mapa()

        self.desenhar_player()

        self.desenhar_interface()

        self.desenhar_mensagem_porta()

        self.desenhar_projeteis()


    def desenhar_fundo(self):

        self.tela.blit(
            self.jogo.fundo,
            (0, 0)
        )


    def desenhar_mapa(self):

        self.jogo.mapa.desenhar(
            self.tela,
            self.jogo.camera.x
        )


    def desenhar_player(self):

        self.jogo.player.desenhar(
            self.tela,
            self.jogo.camera.x
        )


    def desenhar_interface(self):

        # Barra de plasma
        self.jogo.barra_plasma.desenhar(
            self.tela,
            self.jogo.player
        )

        # Barra de vidas
        self.jogo.barra_vidas.desenhar(
            self.tela,
            self.jogo.player
        )


    def desenhar_mensagem_porta(self):

        if not self.jogo.mensagem_porta:
            return

        mensagem = self.fonte_mensagem.render(
            "Você precisa da chave!",
            True,
            (255, 255, 255)
        )

        largura_caixa = mensagem.get_width() + 60
        altura_caixa = mensagem.get_height() + 40

        x = (LARGURA - largura_caixa) // 2
        y = (ALTURA - altura_caixa) // 2

        caixa = pygame.Rect(
            x,
            y,
            largura_caixa,
            altura_caixa
        )

        # Caixa
        pygame.draw.rect(
            self.tela,
            (20, 20, 20),
            caixa
        )

        # Borda
        pygame.draw.rect(
            self.tela,
            (255, 255, 255),
            caixa,
            2
        )

        # Texto
        texto_x = x + (largura_caixa - mensagem.get_width()) // 2
        texto_y = y + (altura_caixa - mensagem.get_height()) // 2

        self.tela.blit(
            mensagem,
            (texto_x, texto_y)
        )

    def desenhar_projeteis(self):

        self.jogo.projeteis.desenhar(
            self.tela,
            self.jogo.camera.x
        )