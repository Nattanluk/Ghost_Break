#plasma.py
import math

import pygame

from Sistemas.recursos import carregar_por_altura
from Sistemas.efeitos import halo


class Plasma:

    ALTURA_SPRITE = 40
    # Vai e volta pelos frames (sem "pulo" do último para o primeiro)
    SEQUENCIA = (0, 1, 2, 3, 4, 3, 2, 1)

    def __init__(self, x, y):

        # (x, y) = canto superior esquerdo da área do plasma
        self.rect = pygame.Rect(x, y, 30, 40)
        self.coletado = False

        # ANIMAÇÃO (frames com proporção preservada)
        self.frames = [
            carregar_por_altura(
                f"imagens/plasma_frame_{numero}.png",
                self.ALTURA_SPRITE
            )
            for numero in range(1, 6)
        ]

        self.brilho = halo(30, (90, 170, 255), 120)

        self.indice = 0
        self.tempo_animacao = 0
        self.velocidade_animacao = 6

        # Cada plasma balança em uma fase diferente
        self.fase_flutuar = (x * 0.013) % math.tau
        self.tempo = 0.0

    @property
    def frame_atual(self):
        return self.SEQUENCIA[self.indice]

    def atualizar(self, efeitos=None):

        self.tempo += 0.07
        self.tempo_animacao += 1

        if self.tempo_animacao >= self.velocidade_animacao:

            self.tempo_animacao = 0
            self.indice = (self.indice + 1) % len(self.SEQUENCIA)

        if efeitos is not None and int(self.tempo * 100) % 11 == 0:

            efeitos.brilho_suave(
                self.rect.centerx,
                self.rect.centery - 6
            )

    def desenhar(self, tela, camera_x):

        if self.coletado:
            return

        x = self.rect.centerx - camera_x

        if not (-60 < x < tela.get_width() + 60):
            return

        deslocamento = math.sin(self.tempo + self.fase_flutuar) * 4

        centro_y = self.rect.centery + deslocamento

        brilho = self.brilho
        tela.blit(
            brilho,
            (
                x - brilho.get_width() // 2,
                centro_y - brilho.get_height() // 2
            )
        )

        imagem = self.frames[self.frame_atual]

        tela.blit(
            imagem,
            imagem.get_rect(center=(x, centro_y))
        )

    def get_rect(self):
        return self.rect


class Criar_Plasmas:

    def criar(self, posicoes=None):
        """posicoes: lista de (x_centro, y_base). O plasma é criado
        flutuando logo acima da base informada."""

        if posicoes is None:
            posicoes = [
                (415, 410), (815, 410), (1015, 235),
                (1215, 410), (1365, 410), (2215, 410)
            ]

        plasmas = []

        for x_centro, y_base in posicoes:

            plasmas.append(
                Plasma(x_centro - 15, y_base - 40 - 6)
            )

        return plasmas
