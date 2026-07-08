import pygame
from personagem import Personagem
from projetil import Projetil

LARGURA_TELA = 800
LARGURA_MAPA = 5000
CHAO_Y = 350


class Saulo(Personagem):

    def __init__(self, x, y):
        super().__init__(x, y)

        # Movimento
        self.velocidade = 5

        # Física
        self.vel_y = 0
        self.gravidade = 0.5
        self.forca_pulo = -10

        # Estado
        self.no_chao = True

        self.tem_chave = False

        self.direção = 1 

    def mover_horizontal(self, teclas):

        if teclas[pygame.K_LEFT]:
            self.pos_x -= self.velocidade
            self.direcao = -1

        if teclas[pygame.K_RIGHT]:
            self.pos_x += self.velocidade
            self.direcao = 1

        # Limites do mapa
        if self.pos_x < 0:
            self.pos_x = 0

        if self.pos_x + self.largura > LARGURA_MAPA:
            self.pos_x = LARGURA_MAPA - self.largura

    def pular(self):

        if self.no_chao:
            self.vel_y = self.forca_pulo
            self.no_chao = False

    def aplicar_gravidade(self, plataformas):

        self.vel_y += self.gravidade
        self.pos_y += self.vel_y

        # Assume que está no ar
        self.no_chao = False

        # Colisão com as plataformas
        for plataforma in plataformas:

            if (
                self.pos_x + self.largura > plataforma.rect.left
                and self.pos_x < plataforma.rect.right
                and self.pos_y + self.altura >= plataforma.rect.top
                and self.pos_y + self.altura <= plataforma.rect.top + 15
                and self.vel_y >= 0
            ):
                self.pos_y = plataforma.rect.top - self.altura
                self.vel_y = 0
                self.no_chao = True


    def update(self, teclas, plataformas):

        self.mover_horizontal(teclas)
        self.aplicar_gravidade(plataformas)

    def desenhar(self, tela, camera_x):

        pygame.draw.rect(
            tela,
            (255, 255, 0),
            (
                int(self.pos_x - camera_x),
                int(self.pos_y),
                self.largura,
                self.altura
            )
        )

    def get_rect(self):
        return pygame.Rect(
            self.pos_x,
            self.pos_y,
            self.largura,
            self.altura
        )

    def atirar(self):
        return Projetil(
            self.pos_x + self.largura // 2,
            self.pos_y + self.altura // 2,
            self.direcao
        )