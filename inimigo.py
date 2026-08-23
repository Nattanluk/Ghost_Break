#inimigo.py
import pygame


class Inimigo:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.x_inicial = x

        self.largura = 40
        self.altura = 60

        self.vida = 1
        self.vivo = True

        # Movimento
        self.velocidade = 2
        self.direcao = -1

        # Física
        self.vel_y = 0
        self.gravidade = 0.5
        self.no_chao = False

        # Distância máxima que pode andar
        self.distancia_patrulha = 190

    def atualizar(self, plataformas):

        if not self.vivo:
            return

        # -------------------------
        # MOVIMENTO HORIZONTAL
        # -------------------------

        self.x += self.velocidade * self.direcao

        # Limite direito da patrulha
        if self.x >= self.x_inicial + self.distancia_patrulha:

            self.x = self.x_inicial + self.distancia_patrulha
            self.direcao = -1

        # Limite esquerdo da patrulha
        if self.x <= self.x_inicial - self.distancia_patrulha:

            self.x = self.x_inicial - self.distancia_patrulha
            self.direcao = 1

        # -------------------------
        # GRAVIDADE
        # -------------------------

        self.vel_y += self.gravidade
        self.y += self.vel_y

        self.no_chao = False

        # -------------------------
        # COLISÃO COM PLATAFORMAS
        # -------------------------

        for plataforma in plataformas:

            esquerda_inimigo = self.x + 5
            direita_inimigo = self.x + self.largura - 5

            if (
                direita_inimigo > plataforma.rect.left
                and esquerda_inimigo < plataforma.rect.right
                and self.y + self.altura >= plataforma.rect.top
                and self.y + self.altura <= plataforma.rect.top + 15
                and self.vel_y >= 0
            ):

                self.y = plataforma.rect.top - self.altura
                self.vel_y = 0
                self.no_chao = True
                break

    def desenhar(self, tela, camera_x):

        if self.vivo:

            pygame.draw.rect(
                tela,
                (255, 0, 0),
                (
                    self.x - camera_x,
                    self.y,
                    self.largura,
                    self.altura
                )
            )

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            self.largura,
            self.altura
        )

    def tomar_dano(self):

        self.vida -= 1

        if self.vida <= 0:
            self.vivo = False