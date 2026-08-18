import pygame
from Saulo_prota import Saulo
from menu import Menu
from mapa import Mapa
from inimigo import Inimigo

LARGURA = 800
ALTURA = 450


class Jogo:

    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Ghost_Break")
        self.clock = pygame.time.Clock()
        self.player = Saulo(100, 350, "imagens/Saulinho.png")
        self.camera_x = 0
        self.chao_y = 410
        self.mapa = Mapa()
        self.projeteis = []

        self.inimigos = [
            Inimigo(600, 350),
            Inimigo(1200, 350)
        ]

    def loop_jogo(self):
        rodando = True

        while rodando:
            self.clock.tick(60)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

                if evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_UP:
                        self.player.pular()

                    if evento.key == pygame.K_s:
                        self.projeteis.append(
                            self.player.atirar()
                        )

            if self.player.vida <= 0:
                print("Game Over")
                rodando = False

            teclas = pygame.key.get_pressed()

            self.player.update(
                teclas,
                self.mapa.plataformas
            )

            for projetil in self.projeteis:
                projetil.mover()

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
                            self.projeteis.remove(projetil)

                        break

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

            if (
                self.player.tem_chave
                and self.player.get_rect().colliderect(
                    self.mapa.porta.rect
                )
            ):
                print("Fase concluída!")

            if (
                not self.mapa.chave.coletada
                and self.player.get_rect().colliderect(
                    self.mapa.chave.rect
                )
            ):
                self.mapa.chave.coletada = True
                self.player.tem_chave = True
                print("Chave coletada!")

            self.camera_x = max(
                0,
                self.player.pos_x - 200
            )

            self.tela.fill((30, 30, 30))

            for plataforma in self.mapa.plataformas:
                plataforma.desenhar(
                    self.tela,
                    self.camera_x
                )

            for inimigo in self.inimigos:
                inimigo.desenhar(
                    self.tela,
                    self.camera_x
                )

            self.mapa.porta.desenhar(
                self.tela,
                self.camera_x
            )

            self.mapa.chave.desenhar(
                self.tela,
                self.camera_x
            )

            self.player.desenhar(
                self.tela,
                self.camera_x
            )

            for projetil in self.projeteis:
                projetil.desenhar(
                    self.tela,
                    self.camera_x
                )

            pygame.display.update()

        pygame.quit()

    def iniciar(self):
        menu = Menu(self)
        menu.executar()