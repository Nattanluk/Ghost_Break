# efeitos.py
"""Partículas e efeitos visuais leves (poeira, faíscas, brilho)."""
import math
import random

import pygame


class Particula:

    __slots__ = (
        "x", "y", "vx", "vy", "vida", "vida_max",
        "raio", "cor", "gravidade", "encolher"
    )

    def __init__(
        self, x, y, vx, vy, vida, raio, cor,
        gravidade=0.0, encolher=True
    ):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.vida = vida
        self.vida_max = vida
        self.raio = raio
        self.cor = cor
        self.gravidade = gravidade
        self.encolher = encolher


class Efeitos:

    LIMITE = 260

    def __init__(self, largura_tela, altura_tela):

        self.particulas = []
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.camada = None

    # CRIAÇÃO
    def _adicionar(self, particula):

        if len(self.particulas) < self.LIMITE:
            self.particulas.append(particula)

    def poeira(self, x, y, quantidade=6):

        for _ in range(quantidade):

            self._adicionar(Particula(
                x + random.uniform(-10, 10),
                y,
                random.uniform(-1.4, 1.4),
                random.uniform(-1.2, -0.2),
                random.randint(14, 24),
                random.uniform(2, 4),
                (190, 200, 225),
                gravidade=0.02
            ))

    def faiscas(self, x, y, quantidade=10, cor=(120, 200, 255)):

        for _ in range(quantidade):

            angulo = random.uniform(0, math.tau)
            velocidade = random.uniform(1.0, 3.6)

            self._adicionar(Particula(
                x, y,
                math.cos(angulo) * velocidade,
                math.sin(angulo) * velocidade,
                random.randint(16, 30),
                random.uniform(2, 4),
                cor,
                gravidade=0.05
            ))

    def explosao(self, x, y, cor=(190, 110, 255)):

        self.faiscas(x, y, 18, cor)
        self.faiscas(x, y, 8, (255, 255, 255))

    def rastro(self, x, y, cor=(120, 150, 255)):

        self._adicionar(Particula(
            x + random.uniform(-6, 6),
            y + random.uniform(-6, 6),
            random.uniform(-0.2, 0.2),
            random.uniform(-0.5, -0.1),
            random.randint(14, 22),
            random.uniform(2, 4),
            cor
        ))

    def brilho_suave(self, x, y, cor=(140, 210, 255)):

        self._adicionar(Particula(
            x + random.uniform(-12, 12),
            y + random.uniform(-4, 8),
            random.uniform(-0.15, 0.15),
            random.uniform(-0.7, -0.25),
            random.randint(26, 40),
            random.uniform(1.5, 2.6),
            cor
        ))

    # ATUALIZAÇÃO / DESENHO
    def atualizar(self):

        for p in self.particulas:

            p.x += p.vx
            p.y += p.vy
            p.vy += p.gravidade
            p.vx *= 0.97
            p.vida -= 1

        self.particulas = [p for p in self.particulas if p.vida > 0]

    def desenhar(self, tela, camera_x):

        if not self.particulas:
            return

        if self.camada is None:
            self.camada = pygame.Surface(
                (self.largura_tela, self.altura_tela),
                pygame.SRCALPHA
            )

        self.camada.fill((0, 0, 0, 0))

        for p in self.particulas:

            fracao = p.vida / p.vida_max
            raio = p.raio * (fracao if p.encolher else 1)

            if raio < 0.8:
                continue

            tela_x = p.x - camera_x

            if not (-10 < tela_x < self.largura_tela + 10):
                continue

            alfa = int(255 * min(1.0, fracao * 1.4))

            pygame.draw.circle(
                self.camada,
                (p.cor[0], p.cor[1], p.cor[2], alfa),
                (int(tela_x), int(p.y)),
                max(1, int(raio))
            )

        tela.blit(self.camada, (0, 0))


def halo(raio, cor, intensidade=90):
    """Cria um brilho circular suave (para plasma, chave, portão)."""

    tamanho = raio * 2
    superficie = pygame.Surface((tamanho, tamanho), pygame.SRCALPHA)

    passos = 7

    for i in range(passos, 0, -1):

        fracao = i / passos
        alfa = int(intensidade * (1 - fracao) ** 1.3 / 2.2) + 4

        pygame.draw.circle(
            superficie,
            (cor[0], cor[1], cor[2], min(255, alfa)),
            (raio, raio),
            int(raio * fracao)
        )

    return superficie
