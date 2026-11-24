# projetil.py
import random

import pygame

from Sistemas.recursos import carregar_escalada
from Sistemas.efeitos import halo

_ALTURA_SPRITE = 22
_LARGURA_SPRITE = 66

_NOMES_FRAMES = [
    "imagens/projetil_1.png",
    "imagens/projetil_3.png",
    "imagens/projetil_2.png"
]

# Cache: os frames são preparados UMA vez (antes, cada tiro recarregava
# e redimensionava 3 imagens grandes do disco, causando travadas).
_cache_frames = {}
_cache_brilho = {}


def _frames(nome_cache, tintura=None):

    if nome_cache not in _cache_frames:

        lista = []

        for nome in _NOMES_FRAMES:

            imagem = carregar_escalada(
                nome,
                (_LARGURA_SPRITE, _ALTURA_SPRITE)
            ).copy()

            if tintura is not None:
                imagem.fill(
                    tintura,
                    special_flags=pygame.BLEND_RGBA_MULT
                )

            lista.append(imagem)

        _cache_frames[nome_cache] = lista

    return _cache_frames[nome_cache]


def _brilho(chave, cor):

    if chave not in _cache_brilho:
        _cache_brilho[chave] = halo(26, cor, 150)

    return _cache_brilho[chave]


class Projetil:

    ALCANCE = 650
    COR_BRILHO = (90, 170, 255)
    COR_RASTRO = (110, 190, 255)
    NOME_FRAMES = "saulo"
    TINTURA = None

    def __init__(self, x, y, direcao):

        # (x, y) = CENTRO do projétil
        self.x = x
        self.y = y

        # Tamanho do desenho
        self.largura = _LARGURA_SPRITE
        self.altura = _ALTURA_SPRITE

        # Parte "cabeça" do projétil, que causa o dano
        self.largura_hitbox = 34
        self.altura_hitbox = 14

        self.velocidade = 6.5
        self.direcao = 1 if direcao >= 0 else -1

        self.distancia_percorrida = 0
        self.ativo = True

        # Animação
        self.frames = _frames(self.NOME_FRAMES, self.TINTURA)
        self.frame_atual = 0
        self.tempo_animacao = 0
        self.velocidade_animacao = 5

        self.brilho = _brilho(self.NOME_FRAMES, self.COR_BRILHO)

    def mover(self):

        self.x += self.velocidade * self.direcao
        self.distancia_percorrida += self.velocidade

        if self.distancia_percorrida >= self.ALCANCE:
            self.ativo = False

        self.tempo_animacao += 1

        if self.tempo_animacao >= self.velocidade_animacao:

            self.tempo_animacao = 0
            self.frame_atual = (self.frame_atual + 1) % len(self.frames)

    def _x_cabeca(self):

        # As imagens originais apontam para a ESQUERDA.
        # Indo para a esquerda, a cabeça está na ponta esquerda.
        if self.direcao < 0:
            return self.x - self.largura / 2 + self.largura_hitbox / 2

        return self.x + self.largura / 2 - self.largura_hitbox / 2

    def get_rect(self):

        centro_x = self._x_cabeca()

        return pygame.Rect(
            centro_x - self.largura_hitbox / 2,
            self.y - self.altura_hitbox / 2,
            self.largura_hitbox,
            self.altura_hitbox
        )

    def desenhar(self, tela, camera_x):

        tela_x = self.x - camera_x

        if not (-120 < tela_x < tela.get_width() + 120):
            return

        imagem = self.frames[self.frame_atual]

        # As imagens originais apontam para a esquerda.
        if self.direcao > 0:
            imagem = pygame.transform.flip(imagem, True, False)

        cabeca_x = self._x_cabeca() - camera_x

        tela.blit(
            self.brilho,
            (
                cabeca_x - self.brilho.get_width() // 2,
                self.y - self.brilho.get_height() // 2
            )
        )

        tela.blit(
            imagem,
            (
                int(tela_x - self.largura / 2),
                int(self.y - self.altura / 2)
            )
        )


class ProjetilSaulo(Projetil):

    NOME_FRAMES = "saulo"
    ALCANCE = 720


class ProjetilInimigo(Projetil):

    # Projétil inimigo em tom rosado, para não ser confundido
    # com o plasma azul do Saulo.
    NOME_FRAMES = "inimigo"
    TINTURA = (255, 110, 200, 255)
    COR_BRILHO = (255, 90, 170)
    COR_RASTRO = (255, 120, 200)
    ALCANCE = 520

    def __init__(self, x, y, direcao):

        super().__init__(x, y, direcao)

        self.velocidade = 4.2


class BarraPlasma:

    def __init__(self):

        tamanho_barra = (120, 80)

        caminhos = [
            "imagens/nenhum_plasma.png",
            "imagens/plasma_pouco.png",
            "imagens/plasma_metade.png",
            "imagens/plasma_cheio.png"
        ]

        self.barras = [
            carregar_escalada(caminho, tamanho_barra)
            for caminho in caminhos
        ]

        self.fonte = pygame.font.SysFont("Arial", 18, bold=True)
        self._texto_cache = {}

    def _texto(self, quantidade):

        if quantidade not in self._texto_cache:
            self._texto_cache[quantidade] = self.fonte.render(
                f"x{quantidade}", True, (170, 220, 255)
            )

        return self._texto_cache[quantidade]

    def desenhar(self, tela, player):

        plasmas = player.plasmas

        imagem = self.barras[min(max(plasmas, 0), 3)]

        tela.blit(
            imagem,
            (19, 0)
        )

        # Mostra a quantidade total (a barra só vai até 3)
        if plasmas > 0:
            tela.blit(self._texto(plasmas), (146, 28))


class GerenciadorProjeteis:

    def __init__(self):

        self.projeteis = []

    def adicionar(self, projetil):

        if projetil is not None:

            self.projeteis.append(projetil)

    def atualizar(self, efeitos=None, largura_mapa=None):

        for projetil in self.projeteis:

            projetil.mover()

            if largura_mapa is not None and not (
                -100 < projetil.x < largura_mapa + 100
            ):
                projetil.ativo = False

            if efeitos is not None and random.random() < 0.6:

                traseira = (
                    projetil.x - projetil.direcao
                    * (projetil.largura / 2 - 8)
                )

                efeitos.rastro(
                    traseira,
                    projetil.y,
                    projetil.COR_RASTRO
                )

        # Remove projéteis que saíram do alcance / do mapa
        self.projeteis = [p for p in self.projeteis if p.ativo]

    def desenhar(self, tela, camera_x):

        for projetil in self.projeteis:

            projetil.desenhar(
                tela,
                camera_x
            )
