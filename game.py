#game.py
import pygame
from Saulo_prota import Saulo
from menu import Menu
from mapa import Mapa
from inimigo import Inimigo
from gameover import GameOver
from fase_concluida import FaseConcluida


LARGURA = 800
ALTURA = 450


class Jogo:

    def __init__(self):

        pygame.init()

        self.tela = pygame.display.set_mode(
            (LARGURA, ALTURA)
        )

        pygame.display.set_caption("Ghost_Break")

        self.clock = pygame.time.Clock()
        self.player = Saulo(
            100,
            350,
            "imagens/Saulinho.png"
        )

        self.camera_x = 0
        self.chao_y = 410
        self.mapa = Mapa()
        self.projeteis = []
        self.inimigos = [
            Inimigo(600, 350),
            Inimigo(1200, 350)
        ]

    def reiniciar_jogo(self):

        # Cria um novo jogador
        # Isso faz a vida voltar ao valor inicial
        self.player = Saulo(
            100,
            350,
            "imagens/Saulinho.png"
        )

        # Remove os projéteis antigos
        self.projeteis = []

        # Cria os inimigos novamente
        self.inimigos = [
            Inimigo(600, 350),
            Inimigo(1200, 350)
        ]

        # Cria o mapa novamente
        # A chave também volta para o lugar
        self.mapa = Mapa()

        self.camera_x = 0

    def loop_jogo(self):

        rodando = True

        while rodando:

            self.clock.tick(60)

            # EVENTOS
            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:
                    return "sair"

                if evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_UP:
                        self.player.pular()

                    if evento.key == pygame.K_s:

                        projetil = self.player.atirar()

                        if projetil is not None:
                            self.projeteis.append(projetil)

            # GAME OVER
            if self.player.vida <= 0:

                print("ENTROU NO GAME OVER")
                gameover = GameOver(self)
                resultado = gameover.executar()

                # ENTER
                if resultado == "jogar":
                    self.reiniciar_jogo()
                    continue

                # ESC
                if resultado == "menu":

                    return "menu"

                # Fechar jogo
                if resultado == "sair":

                    return "sair"

            # ATUALIZAÇÃO DO JOGADOR

            teclas = pygame.key.get_pressed()

            self.player.update(
                teclas,
                self.mapa.plataformas
            )
            
            # ATUALIZAÇÃO DOS INIMIGOS

            for inimigo in self.inimigos:
                inimigo.atualizar()

 
            # PROJÉTEIS
            for projetil in self.projeteis:
                projetil.mover()


            # COLISÃO DOS PROJÉTEIS
            # COM OS INIMIGOS
  
            for projetil in self.projeteis[:]:
                for inimigo in self.inimigos:

                    if (
                        inimigo.vivo
                        and projetil.get_rect().colliderect(
                            inimigo.get_rect()
                        )
                    ):

                        inimigo.tomar_dano()

                        if projetil in self.projeteis:

                            self.projeteis.remove(
                                projetil
                            )

                        break

  
            # COLISÃO DO JOGADOR
            # COM OS INIMIGOS

            for inimigo in self.inimigos:

                if (
                    inimigo.vivo
                    and not self.player.invulneravel
                    and self.player.get_rect().colliderect(
                        inimigo.get_rect()
                    )
                ):

                    self.player.vida -= 1
                    self.player.invulneravel = True
                    self.player.tempo_invulnerabilidade = 60


                # PORTA

            if (
                    self.player.tem_chave
                    and self.player.get_rect().colliderect(
                        self.mapa.porta.rect
                    )
                ):

                    tela_fase = FaseConcluida(
                        self.tela,
                        self.clock
                    )

                    resultado = tela_fase.executar()

                    if resultado == "sair":
                        return "sair"

                    if resultado == "menu":
                        return "menu"

                    if resultado == "proxima":
                        self.reiniciar_jogo()
                        return "menu"

        
                    # CHAVE

            if (
                    not self.mapa.chave.coletada
                    and self.player.get_rect().colliderect(
                        self.mapa.chave.rect
                    )
                ):

                    self.mapa.chave.coletada = True
                    self.player.tem_chave = True
                    print("Chave coletada!")


            # PLASMAS

            for plasma in self.mapa.plasmas:

                if (
                    not plasma.coletado
                    and self.player.get_rect().colliderect(
                        plasma.get_rect()
                    )
                ):

                    plasma.coletado = True
                    self.player.plasmas += 1

                    print(
                        "Plasma coletado!",
                        self.player.plasmas
                    )
  
            # CÂMERA

            self.camera_x = max(
                0,
                self.player.pos_x - 200
            )

 
            # DESENHO

            self.tela.fill(
                (30, 30, 30)
            )

            # Plataformas
            for plataforma in self.mapa.plataformas:

                plataforma.desenhar(
                    self.tela,
                    self.camera_x
                )

            # Inimigos
            for inimigo in self.inimigos:

                inimigo.desenhar(
                    self.tela,
                    self.camera_x
                )

            # Porta
            self.mapa.porta.desenhar(
                self.tela,
                self.camera_x
            )

            # Chave
            self.mapa.chave.desenhar(
                self.tela,
                self.camera_x
            )
            
            # Plasmas

            for plasma in self.mapa.plasmas:

                plasma.desenhar(
                    self.tela,
                    self.camera_x
                )

            # Jogador
            self.player.desenhar(
                self.tela,
                self.camera_x
            )

            fonte = pygame.font.SysFont(
                "Arial",
                24,
                bold=True
            )

            texto_plasma = fonte.render(
                f"Plasma: {self.player.plasmas}",
                True,
                (0, 255, 255)
            )

            self.tela.blit(
                texto_plasma,
                (20, 20)
            )

            # Projéteis
            for projetil in self.projeteis:

                projetil.desenhar(
                    self.tela,
                    self.camera_x
                )

            pygame.display.flip()

        return "menu"

    def iniciar(self):
        menu = Menu(self)
        menu.executar()