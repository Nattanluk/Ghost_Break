import pygame
from Saulo_prota import Saulo
from menu import Menu
from mapa import Mapa

LARGURA = 800
ALTURA = 450


class Jogo:

    def __init__(self):
        pygame.init()

        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Ghost_Break")
        self.clock = pygame.time.Clock()
        self.player = Saulo(100, 350)
        self.camera_x = 0
        self.chao_y = 410
        self.mapa = Mapa()
        self.projeteis = []

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

            teclas = pygame.key.get_pressed()

            self.player.update(teclas, self.mapa.plataformas)

            for projetil in self.projeteis:
                projetil.mover()

            for projetil in self.projeteis[:]:
                for inimigo in self.mapa.inimigos:

                    if inimigo.vivo and projetil.get_rect().colliderect(inimigo.get_rect()):

                        inimigo.tomar_dano()

                        # Remove o projétil
                        if projetil in self.projeteis:
                            self.projeteis.remove(projetil)

                        break

            if (
                self.player.tem_chave
                and self.player.get_rect().colliderect(self.mapa.porta.rect)
            ):
                print("Fase concluída!")
            if (
                not self.mapa.chave.coletada
                and self.player.get_rect().colliderect(self.mapa.chave.rect)
            ):
                self.mapa.chave.coletada = True
                self.player.tem_chave = True
                print("Chave coletada!")
            self.camera_x = max(0, self.player.pos_x - 200)

            self.tela.fill((30, 30, 30))
            
            # Plataformas
            for plataforma in self.mapa.plataformas:
                plataforma.desenhar(self.tela, self.camera_x)

            for inimigo in self.mapa.inimigos:
                inimigo.desenhar(self.tela, self.camera_x) 

            self.mapa.porta.desenhar(self.tela, self.camera_x)

            self.mapa.chave.desenhar(self.tela, self.camera_x)

            #jogador
            self.player.desenhar(self.tela, self.camera_x)

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