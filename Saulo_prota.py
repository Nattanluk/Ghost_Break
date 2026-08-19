import pygame
import math
from personagem import Personagem
from projetil import Projetil

LARGURA_TELA = 800
LARGURA_MAPA = 3000
CHAO_Y = 350


class Saulo(Personagem):

    def __init__(self, x, y, spritecaminho, esquerda = False):
        super().__init__(x, y)
        self.spritecaminho = spritecaminho

        self.sprite = pygame.image.load(self.spritecaminho).convert_alpha()
        self.sprite_direita = pygame.transform.scale(self.sprite, (64, 77))
        self.sprite_esquerda = pygame.transform.flip(self.sprite_direita, True, False)
        self.esquerda = esquerda
        self.vida = 3
        self.invulneravel = False
        self.tempo_invulnerabilidade = 0
            
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

        self.tempo_flutuar = 0  
        self.velocidade_flutuar = 0.05  
        self.amplitude_flutuar = 8  
        
        self.plasmas = 0

    def mover_horizontal(self, teclas):

        if teclas[pygame.K_LEFT]:
            self.pos_x -= self.velocidade
            self.direcao = -1
            self.esquerda = True
            

        if teclas[pygame.K_RIGHT]:
            self.pos_x += self.velocidade
            self.direcao = 1
            self.esquerda = False

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

        self.tempo_flutuar += self.velocidade_flutuar
        if self.invulneravel:
            self.tempo_invulnerabilidade -= 1

        if self.tempo_invulnerabilidade <= 0:
            self.invulneravel = False

    def desenhar(self, tela, camera_x):
        deslocamento_y = math.sin(self.tempo_flutuar) * self.amplitude_flutuar
        pos_y_final = self.pos_y - 25 + deslocamento_y
        if self.esquerda:
            tela.blit(self.sprite_esquerda, (self.pos_x - camera_x, pos_y_final))
        else:
            tela.blit(self.sprite_direita, (self.pos_x - camera_x, pos_y_final))

    def get_rect(self):
        return pygame.Rect(
            self.pos_x,
            self.pos_y,
            self.largura,
            self.altura
        )

    def atirar(self):

        if self.plasmas < 3:
            return None

        self.plasmas -= 3

        return Projetil(
            self.pos_x + self.largura // 2,
            self.pos_y + self.altura // 2,
            self.direcao
        )

    def colidir(self, inimigorect):
        rect = self.get_rect()
        return rect.colliderect(inimigorect)