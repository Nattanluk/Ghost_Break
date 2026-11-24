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
        self.atualizar_mapa()
        self.jogo.projeteis.atualizar(
            self.jogo.efeitos,
            self.jogo.mapa.largura
        )
        self.verificar_colisoes()
        self.jogo.efeitos.atualizar()

        # Coleta antes de checar a porta (assim, pegar a chave e
        # alcançar a porta no mesmo instante funciona)
        self.coletar_itens()

        resultado = self.jogo.verificar_porta()

        if resultado is not None:
            return resultado

        self.atualizar_camera()

        return None


    def atualizar_jogador(self):

        teclas = pygame.key.get_pressed()

        self.jogo.player.update(
            teclas,
            self.jogo.mapa.plataformas,
            self.jogo.mapa.largura,
            self.jogo.efeitos
        )


    def verificar_queda(self):

        if self.jogo.player.pos_y > ALTURA + 50:

            self.jogo.player.vida = 0


    def atualizar_inimigos(self):

        for inimigo in self.jogo.mapa.inimigos:

            inimigo.atualizar(
                self.jogo.mapa.plataformas
            )

            projetil = inimigo.atirar(self.jogo.player)

            if projetil is not None:
                self.jogo.projeteis.adicionar(projetil)


    def atualizar_mapa(self):

        # Animação dos plasmas, chave e porta
        self.jogo.mapa.atualizar(
            self.jogo.player,
            self.jogo.efeitos
        )


    def verificar_colisoes(self):

        self.jogo.colisao.projetil_inimigo(
            self.jogo.projeteis,
            self.jogo.mapa.inimigos
        )

        self.jogo.colisao.projetil_jogador(
            self.jogo.projeteis,
            self.jogo.player
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
