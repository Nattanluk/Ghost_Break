# desenho_jogo.py

import os

import pygame

from configuracoes import *
from Sistemas.recursos import carregar_imagem, resolver_caminho


class DesenhoJogo:

    # O fundo se move mais devagar que o cenário (efeito de profundidade)
    FATOR_PARALLAX = 0.25

    def __init__(self, jogo):

        self.jogo = jogo
        self.tela = jogo.tela

        # Fonte da mensagem da porta
        self.fonte_mensagem = pygame.font.SysFont(
            "Arial",
            24,
            bold=True
        )

        # Fundos das fases
        self.fundos = {}

        self.vinheta = self._criar_vinheta()


    def _criar_vinheta(self):

        # Escurece levemente as bordas da tela
        vinheta = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)

        passos = 26

        for i in range(passos):

            alfa = int(95 * (1 - i / passos) ** 2)

            pygame.draw.rect(
                vinheta,
                (0, 0, 10, alfa),
                (i * 3, i * 3, LARGURA - i * 6, ALTURA - i * 6),
                3
            )

        return vinheta


    def desenhar(self):

        camera = self.jogo.camera.x_desenho

        self.desenhar_fundo()

        self.desenhar_mapa()

        self.desenhar_player()

        self.desenhar_projeteis()

        self.jogo.efeitos.desenhar(self.tela, camera)

        self.tela.blit(self.vinheta, (0, 0))

        self.desenhar_interface()

        self.desenhar_mensagem_porta()


    def _carregar_fundo(self, numero_fase):

        caminho = f"imagens/fundo_nivel{numero_fase}.png"

        # Fases 3, 4 e 5 ainda não têm cenário próprio:
        # reutilizam o fundo da fase 1 (antes o jogo travava aqui).
        if not os.path.isfile(resolver_caminho(caminho)):
            caminho = "imagens/fundo_nivel1.png"

        original = carregar_imagem(caminho, alpha=False)

        proporcao = original.get_width() / original.get_height()

        largura = max(LARGURA, int(ALTURA * proporcao))

        normal = pygame.transform.smoothscale(
            original,
            (largura, ALTURA)
        ).convert()

        espelhado = pygame.transform.flip(normal, True, False)

        return normal, espelhado


    def desenhar_fundo(self):

        numero_fase = self.jogo.fase_atual

        if numero_fase not in self.fundos:
            self.fundos[numero_fase] = self._carregar_fundo(numero_fase)

        normal, espelhado = self.fundos[numero_fase]

        largura = normal.get_width()

        deslocamento = int(
            self.jogo.camera.x_desenho * self.FATOR_PARALLAX
        )

        indice = deslocamento // largura
        resto = deslocamento % largura

        x = -resto

        # Telhas alternadas (normal/espelhada) para não aparecer emenda
        while x < LARGURA:

            imagem = normal if indice % 2 == 0 else espelhado

            self.tela.blit(imagem, (x, 0))

            x += largura
            indice += 1


    def desenhar_mapa(self):

        self.jogo.mapa.desenhar(
            self.tela,
            self.jogo.camera.x_desenho
        )


    def desenhar_player(self):

        self.jogo.player.desenhar(
            self.tela,
            self.jogo.camera.x_desenho
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
        texto_x = x + (
            largura_caixa - mensagem.get_width()
        ) // 2

        texto_y = y + (
            altura_caixa - mensagem.get_height()
        ) // 2

        self.tela.blit(
            mensagem,
            (texto_x, texto_y)
        )


    def desenhar_projeteis(self):

        self.jogo.projeteis.desenhar(
            self.tela,
            self.jogo.camera.x_desenho
        )
