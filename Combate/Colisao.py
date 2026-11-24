#Colisao.py
from Combate.projetil import ProjetilSaulo
from Combate.projetil import ProjetilInimigo


class Colisao:

    def __init__(self, jogo):

        self.jogo = jogo


    def projetil_inimigo(self, gerenciador, inimigos):

        for projetil in gerenciador.projeteis[:]:

            if not isinstance(projetil, ProjetilSaulo):
                continue

            for inimigo in inimigos:

                if (
                    inimigo.vivo
                    and projetil.get_rect().colliderect(inimigo.get_rect())
                ):

                    # Guarda se o inimigo estava vivo
                    estava_vivo = inimigo.vivo

                    # Inimigo recebe dano
                    inimigo.tomar_dano()

                    # Conta o inimigo somente quando ele morrer
                    if estava_vivo and not inimigo.vivo:
                        self.jogo.inimigos_derrotados += 1
                        self.jogo.score += 100

                        self.jogo.efeitos.explosao(
                            inimigo.centro_x,
                            inimigo.y + inimigo.altura / 2
                        )

                    else:
                        self.jogo.efeitos.faiscas(
                            projetil.x, projetil.y, 8
                        )

                    # Remove o projétil
                    if projetil in gerenciador.projeteis:
                        gerenciador.projeteis.remove(projetil)

                    break


    def _jogador_ferido(self, jogador, origem_x):

        if jogador.receber_dano(origem_x):

            self.jogo.camera.tremer(12, 6)

            self.jogo.efeitos.faiscas(
                jogador.pos_x + jogador.largura / 2,
                jogador.pos_y + jogador.altura / 2,
                12,
                (255, 120, 140)
            )


    def projetil_jogador(self, gerenciador, jogador):

        for projetil in gerenciador.projeteis[:]:

            if not isinstance(projetil, ProjetilInimigo):
                continue

            if (
                not jogador.invulneravel
                and projetil.get_rect().colliderect(jogador.get_rect_dano())
            ):

                self._jogador_ferido(jogador, projetil.x)

                if projetil in gerenciador.projeteis:
                    gerenciador.projeteis.remove(projetil)


    def jogador_inimigo(self, jogador, inimigos):

        for inimigo in inimigos:

            if (
                inimigo.vivo
                and not jogador.invulneravel
                and jogador.get_rect_dano().colliderect(inimigo.get_rect())
            ):

                self._jogador_ferido(jogador, inimigo.centro_x)


    def jogador_chave(self, jogador, chave):

        if (
            not chave.coletada
            and jogador.get_rect().colliderect(chave.rect)
        ):

            chave.coletada = True
            jogador.tem_chave = True

            self.jogo.efeitos.faiscas(
                chave.rect.centerx, chave.rect.centery,
                22, (255, 220, 110)
            )


    def jogador_plasma(self, jogador, plasmas):

        for plasma in plasmas:

            if (
                not plasma.coletado
                and jogador.get_rect().colliderect(plasma.get_rect())
            ):

                plasma.coletado = True
                jogador.plasmas += 1

                self.jogo.efeitos.faiscas(
                    plasma.rect.centerx, plasma.rect.centery,
                    10, (130, 210, 255)
                )
