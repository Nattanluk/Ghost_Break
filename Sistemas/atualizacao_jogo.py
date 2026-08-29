#atualizacao_jogo.py
import pygame

from configuracoes import *


class AtualizacaoJogo:

    def __init__(self, jogo):

        self.jogo = jogo


    def atualizar(self):

        self.atualizar_jogador()

        self.verificar_queda()

        self.atualizar_inimigos()

        self.atualizar_plasmas()

        self.jogo.projeteis.atualizar()

        self.verificar_colisoes()

        resultado = self.jogo.verificar_porta()

        if resultado is not None:
            return resultado

        self.coletar_itens()

        self.atualizar_camera()

        return None


    def atualizar_jogador(self):

        teclas = pygame.key.get_pressed()

        self.jogo.player.update(
            teclas,
            self.jogo.mapa.plataformas
        )


    def verificar_queda(self):

        if self.jogo.player.pos_y > ALTURA + 50:

            self.jogo.player.vida = 0


    def atualizar_inimigos(self):

        for inimigo in self.jogo.mapa.inimigos:

            inimigo.atualizar(
                self.jogo.mapa.plataformas
            )


    def atualizar_plasmas(self):

        for plasma in self.jogo.mapa.plasmas:

            if not plasma.coletado:
                plasma.atualizar()


    def verificar_colisoes(self):

        self.jogo.colisao.projetil_inimigo(
            self.jogo.projeteis,
            self.jogo.mapa.inimigos
        )

        self.jogo.colisao.jogador_inimigo(
            self.jogo.player,
            self.jogo.mapa.inimigos
        )


    def coletar_itens(self):

        self.jogo.colisao.jogador_chave(
            self.jogo.player,
            self.jogo.mapa.chave
        )

        self.jogo.colisao.jogador_plasma(
            self.jogo.player,
            self.jogo.mapa.plasmas
        )


    def atualizar_camera(self):

        self.jogo.camera.atualizar(
            self.jogo.player,
            LARGURA
        )