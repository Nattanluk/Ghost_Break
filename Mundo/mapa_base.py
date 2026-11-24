# mapa_base.py
"""Comportamento comum dos mapas (desenho, atualização, montagem)."""
import pygame

from Mundo.plataformas import Criar_Plataforma
from Mundo.porta import Criar_Porta
from Mundo.chave import Criar_Chave
from Combate.inimigo import Inimigo, Atirar
from Combate.plasma import Criar_Plasmas


class MapaBase:

    # Largura total do cenário em pixels (cada mapa define a sua)
    LARGURA = 3000

    # Tema visual das plataformas / sprites dos inimigos (1 ou 2)
    TEMA = 1

    def montar(
        self,
        dados_chao,
        dados_plataformas,
        inimigos,
        plasmas,
        chave,
        porta
    ):
        """
        dados_chao:        [(x_inicio, x_fim), ...]
        dados_plataformas: [(x, y_topo, largura), ...]
        inimigos:          [(x_centro, y_topo_da_plataforma, intervalo_tiro)]
                           (intervalo_tiro = None -> não atira)
        plasmas:           [(x_centro, y_base), ...]
        chave:             (x, y) do canto superior esquerdo
        porta:             (x_centro, y_base)
        """

        self.largura = self.LARGURA

        self.plataformas = Criar_Plataforma(self.TEMA).criar(
            dados_plataformas,
            dados_chao
        )

        self.chave = Criar_Chave().criar(*chave)

        porta_x, porta_base = porta
        self.porta = Criar_Porta().criar(porta_x - 28, porta_base - 90)

        self.inimigos = []

        for x_centro, y_topo, intervalo in inimigos:

            inimigo = Inimigo(
                x_centro - 23,
                y_topo - 64,
                self.TEMA
            )

            if intervalo is not None:
                inimigo.atirador = Atirar(intervalo)

            self.inimigos.append(inimigo)

        self.plasmas = Criar_Plasmas().criar(plasmas)

    def atualizar(self, player, efeitos):

        alcance = 650

        for plasma in self.plasmas:

            if plasma.coletado:
                continue

            perto = abs(plasma.rect.centerx - player.pos_x) < alcance

            plasma.atualizar(efeitos if perto else None)

        self.chave.atualizar(
            efeitos
            if abs(self.chave.rect.centerx - player.pos_x) < alcance
            else None
        )

        self.porta.atualizar(
            player.tem_chave,
            efeitos
            if abs(self.porta.rect.centerx - player.pos_x) < alcance
            else None
        )

    def desenhar(self, tela, camera_x):

        self.porta.desenhar(tela, camera_x)

        for plataforma in self.plataformas:
            plataforma.desenhar(tela, camera_x)

        self.chave.desenhar(tela, camera_x)

        for plasma in self.plasmas:
            plasma.desenhar(tela, camera_x)

        for inimigo in self.inimigos:
            inimigo.desenhar(tela, camera_x)
