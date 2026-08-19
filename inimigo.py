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
        self.direcao = 1

        # Distância máxima que pode andar
        self.distancia_patrulha = 100

    def atualizar(self):

        if not self.vivo:
            return

        self.x += self.velocidade * self.direcao

        # Chegou no limite direito
        if self.x >= self.x_inicial + self.distancia_patrulha:

            self.x = self.x_inicial + self.distancia_patrulha
            self.direcao = -1

        # Chegou no limite esquerdo
        if self.x <= self.x_inicial - self.distancia_patrulha:

            self.x = self.x_inicial - self.distancia_patrulha
            self.direcao = 1

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