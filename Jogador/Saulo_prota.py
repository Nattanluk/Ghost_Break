# Saulo_prota.py

import pygame
import math

from Jogador.personagem import Personagem
from Combate.projetil import Projetil
from configuracoes import LARGURA_MAPA, TECLA_ESQUERDA, TECLA_DIREITA


class Saulo(Personagem):

    def __init__(self, x, y, esquerda=False):

        super().__init__(x, y)

        # SPRITES
        self.sprite = pygame.image.load(
            "imagens/Saulinho.png"
        ).convert_alpha()

        self.sprite_dano = pygame.image.load(
            "imagens/Saulinho_Dano.png"
        ).convert_alpha()

        # Saulo normal
        self.sprite_direita = pygame.transform.scale(
            self.sprite,
            (69, 77)
        )

        self.sprite_esquerda = pygame.transform.flip(
            self.sprite_direita,
            True,
            False
        )

        # Saulo recebendo dano
        self.sprite_dano_direita = pygame.transform.scale(
            self.sprite_dano,
            (60, 68)
        )

        self.sprite_dano_esquerda = pygame.transform.flip(
            self.sprite_dano_direita,
            True,
            False
        )

        self.esquerda = esquerda

        # VIDA
        self.vida = 3
        self.invulneravel = False
        self.tempo_invulnerabilidade = 0

        # MOVIMENTO
        self.velocidade = 5
        self.direcao = 1

        # FÍSICA
        self.vel_y = 0
        self.gravidade = 0.5
        self.forca_pulo = -10
        self.no_chao = True

        # ESTADO
        self.tem_chave = False
        self.plasmas = 0

        # FLUTUAÇÃO
        self.tempo_flutuar = 0
        self.velocidade_flutuar = 0.05
        self.amplitude_flutuar = 3


    def mover_horizontal(self, teclas):

        # Esquerda: ← ou A
        if teclas[TECLA_ESQUERDA[0]] or teclas[TECLA_ESQUERDA[1]]:
            self.pos_x -= self.velocidade
            self.direcao = -1
            self.esquerda = True

        # Direita: → ou D
        if teclas[TECLA_DIREITA[0]] or teclas[TECLA_DIREITA[1]]:
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

        # Guarda a posição antes da gravidade
        pos_y_anterior = self.pos_y

        # Aplica a gravidade
        self.vel_y += self.gravidade
        self.pos_y += self.vel_y

        # Assume que está no ar
        self.no_chao = False

        # Colisão com as plataformas
        for plataforma in plataformas:

            # Margens laterais da colisão
            esquerda_saulo = self.pos_x + 5
            direita_saulo = self.pos_x + self.largura - 10

            # Parte inferior do Saulo
            fundo_anterior = pos_y_anterior + self.altura
            fundo_atual = self.pos_y + self.altura

            # Verifica se Saulo atravessou o topo
            # da plataforma
            if (
                direita_saulo > plataforma.rect_colisao.left
                and esquerda_saulo < plataforma.rect_colisao.right
                and fundo_anterior <= plataforma.rect_colisao.top
                and fundo_atual >= plataforma.rect_colisao.top
                and self.vel_y >= 0
            ):
                self.pos_y = (
                    plataforma.rect_colisao.top - self.altura
                )

                self.vel_y = 0
                self.no_chao = True
                break


    def update(self, teclas, plataformas):

        self.mover_horizontal(teclas)
        self.aplicar_gravidade(plataformas)

        # Flutuação
        self.tempo_flutuar += self.velocidade_flutuar

        # Invulnerabilidade
        if self.invulneravel:
            self.tempo_invulnerabilidade -= 1

        if self.tempo_invulnerabilidade <= 0:
            self.invulneravel = False


    def desenhar(self, tela, camera_x):

        deslocamento_y = math.sin(
            self.tempo_flutuar
        ) * self.amplitude_flutuar

        pos_y_final = (
            self.pos_y - 13 + deslocamento_y
        )

        # Escolhe o sprite
        if self.invulneravel:

            if self.esquerda:
                imagem = self.sprite_dano_esquerda
            else:
                imagem = self.sprite_dano_direita

        else:

            if self.esquerda:
                imagem = self.sprite_esquerda
            else:
                imagem = self.sprite_direita

        # Desenha Saulo
        tela.blit(
            imagem,
            (
                self.pos_x - camera_x,
                pos_y_final
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


class BarraVidas:

    def __init__(self):

        self.coracao_cheio = pygame.image.load(
            "imagens/corações_1.png"
        ).convert_alpha()

        self.coracao_meio = pygame.image.load(
            "imagens/corações_2.png"
        ).convert_alpha()

        self.coracao_vazio = pygame.image.load(
            "imagens/corações_3.png"
        ).convert_alpha()


    def desenhar(self, tela, player):

        if player.vida == 3:
            imagem = self.coracao_cheio

        elif player.vida == 2:
            imagem = self.coracao_meio

        else:
            imagem = self.coracao_vazio

        x = tela.get_width() - imagem.get_width() - 20
        y = 20

        tela.blit(
            imagem,
            (x, y)
        )