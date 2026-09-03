#Colisao.py
class Colisao:

    def __init__(self, jogo):

        self.jogo = jogo


    def projetil_inimigo(self, gerenciador, inimigos):

        for projetil in gerenciador.projeteis[:]:

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

                    # Remove o projétil
                    if projetil in gerenciador.projeteis:
                        gerenciador.projeteis.remove(projetil)

                    break


    def jogador_inimigo(self, jogador, inimigos):

        for inimigo in inimigos:

            if (
                inimigo.vivo
                and not jogador.invulneravel
                and jogador.get_rect().colliderect(inimigo.get_rect())
            ):

                jogador.vida -= 1
                jogador.invulneravel = True
                jogador.tempo_invulnerabilidade = 60


    def jogador_chave(self, jogador, chave):

        if (
            not chave.coletada
            and jogador.get_rect().colliderect(chave.rect)
        ):

            chave.coletada = True
            jogador.tem_chave = True

            print("Chave coletada!")


    def jogador_plasma(self, jogador, plasmas):

        for plasma in plasmas:

            if (
                not plasma.coletado
                and jogador.get_rect().colliderect(plasma.get_rect())
            ):

                plasma.coletado = True
                jogador.plasmas += 1

                print("Plasma coletado!", jogador.plasmas)