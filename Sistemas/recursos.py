# recursos.py
"""Carregamento de imagens com cache.

- Cada arquivo é lido do disco uma única vez (antes, as sprites eram
  recarregadas a cada tiro, a cada reinício de fase etc.).
- Tolera diferença de maiúsculas/minúsculas no nome do arquivo
  (ex.: "chao2.png" x "Chao2.png"), que quebra em Linux e macOS.
"""
import os
import re

import pygame

_cache_originais = {}
_cache_escalas = {}


def _normalizar(nome):
    # Decodifica sequências "#U00e7" (geradas ao compactar nomes com acento)
    nome = re.sub(
        r"#U([0-9a-fA-F]{4})",
        lambda m: chr(int(m.group(1), 16)),
        nome
    )
    return nome.lower()


def resolver_caminho(caminho):

    if os.path.isfile(caminho):
        return caminho

    pasta, nome = os.path.split(caminho)
    pasta = pasta or "."

    if os.path.isdir(pasta):

        alvo = _normalizar(nome)

        for arquivo in os.listdir(pasta):

            if _normalizar(arquivo) == alvo:
                return os.path.join(pasta, arquivo)

    return caminho


def carregar_imagem(caminho, alpha=True):
    """Devolve a imagem original (compartilhada: não modifique!)."""

    chave = (caminho, alpha)

    if chave not in _cache_originais:

        imagem = pygame.image.load(resolver_caminho(caminho))

        _cache_originais[chave] = (
            imagem.convert_alpha() if alpha else imagem.convert()
        )

    return _cache_originais[chave]


def carregar_escalada(caminho, tamanho, alpha=True, suave=True):
    """Imagem já redimensionada (também guardada em cache)."""

    tamanho = (int(tamanho[0]), int(tamanho[1]))
    chave = (caminho, tamanho, alpha, suave)

    if chave not in _cache_escalas:

        original = carregar_imagem(caminho, alpha)

        if suave:
            nova = pygame.transform.smoothscale(original, tamanho)
        else:
            nova = pygame.transform.scale(original, tamanho)

        _cache_escalas[chave] = nova

    return _cache_escalas[chave]


def carregar_por_altura(caminho, altura, alpha=True):
    """Redimensiona mantendo a proporção original."""

    original = carregar_imagem(caminho, alpha)

    largura = max(
        1,
        round(original.get_width() * altura / original.get_height())
    )

    return carregar_escalada(caminho, (largura, altura), alpha)
