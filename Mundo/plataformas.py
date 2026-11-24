# plataformas.py
import pygame

from Sistemas.recursos import carregar_imagem
from configuracoes import CHAO_Y, ALTURA

ESPESSURA_CHAO = 60


def _montar_faixa(imagem, largura, altura):
    """Monta uma faixa de 'largura' x 'altura' repetindo a imagem
    original sem esticá-la de forma exagerada."""

    proporcao = imagem.get_width() / imagem.get_height()
    largura_ideal = altura * proporcao

    quantidade = max(1, round(largura / largura_ideal))
    largura_peca = largura / quantidade

    faixa = pygame.Surface((largura, altura), pygame.SRCALPHA)

    for i in range(quantidade):

        x0 = round(i * largura_peca)
        x1 = round((i + 1) * largura_peca)

        peca = pygame.transform.smoothscale(
            imagem,
            (max(1, x1 - x0), altura)
        )

        faixa.blit(peca, (x0, 0))

    return faixa


class Plataforma:

    def __init__(self, x, y, largura, altura, imagem):

        # Área visual e de colisão são a MESMA (antes a colisão ficava
        # deslocada 15px para a esquerda do desenho).
        self.rect = pygame.Rect(x, y, largura, altura)
        self.rect_colisao = self.rect

        self.imagem = imagem

    def desenhar(self, tela, camera_x):

        x = self.rect.x - camera_x

        # Não desenha o que está fora da tela
        if x > tela.get_width() or x + self.rect.width < 0:
            return

        tela.blit(self.imagem, (x, self.rect.y))


class Criar_Plataforma:

    def __init__(self, fase=1):

        # Seleciona as sprites de acordo com a fase
        if fase == 1:

            self.caminho_plataforma = "imagens/plataforma.png"
            self.caminho_chao = "imagens/chao.png"
            self.espessura_plataforma = 42

        elif fase == 2:

            self.caminho_plataforma = "imagens/plataforma2.png"
            self.caminho_chao = "imagens/chao2.png"
            self.espessura_plataforma = 52

        else:

            raise ValueError(
                f"Fase inexistente: {fase}"
            )

        self.sprite_plataforma = carregar_imagem(
            self.caminho_plataforma
        )

        self.sprite_chao = carregar_imagem(
            self.caminho_chao
        )

    def criar(self, dados_plataformas, dados_chao):
        """
        dados_plataformas: lista de (x, y, largura) em pixels
                           (a espessura é calculada automaticamente).
        dados_chao:        lista de (x_inicio, x_fim) em pixels.
        """

        plataformas = []

        # Trechos de chão: UMA plataforma por trecho
        for inicio, fim in dados_chao:

            largura = fim - inicio

            imagem = _montar_faixa(
                self.sprite_chao,
                largura,
                ESPESSURA_CHAO
            )

            plataformas.append(
                Plataforma(
                    inicio,
                    CHAO_Y,
                    largura,
                    ESPESSURA_CHAO,
                    imagem
                )
            )

        # Plataformas suspensas
        for x, y, largura in dados_plataformas:

            imagem = _montar_faixa(
                self.sprite_plataforma,
                largura,
                self.espessura_plataforma
            )

            plataformas.append(
                Plataforma(
                    x,
                    y,
                    largura,
                    self.espessura_plataforma,
                    imagem
                )
            )

        return plataformas
