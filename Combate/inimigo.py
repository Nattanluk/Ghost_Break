# inimigo.py
import pygame

class Inimigo:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.x_inicial = x
        self.largura = 50
        self.altura = 70
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

 
        # ANIMAÇÃO
        self.imagens = [
            pygame.image.load("imagens/1000326750.png").convert_alpha(),
            pygame.image.load("imagens/1000326751.png").convert_alpha(),
            pygame.image.load("imagens/1000326749.png").convert_alpha()
        ]

        # Ajusta o tamanho das imagens
        for i in range(len(self.imagens)):
            self.imagens[i] = pygame.transform.scale(
                self.imagens[i],
                (self.largura, self.altura)
            )

        self.frame = 0

        # Quanto maior, mais devagar a animação
        self.tempo_animacao = 0
        self.velocidade_animacao = 15

    def atualizar(self, plataformas):

        if not self.vivo:
            return

        # MOVIMENTO HORIZONTAL
        self.x += self.velocidade * self.direcao

        # Limite direito da patrulha
        if self.x >= self.x_inicial + self.distancia_patrulha:

            self.x = self.x_inicial + self.distancia_patrulha
            self.direcao = -1

        # Limite esquerdo da patrulha
        if self.x <= self.x_inicial - self.distancia_patrulha:

            self.x = self.x_inicial - self.distancia_patrulha
            self.direcao = 1

        # GRAVIDADE
        self.vel_y += self.gravidade
        self.y += self.vel_y
        self.no_chao = False

        # COLISÃO COM PLATAFORMAS
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

        # ANIMAÇÃO
        self.tempo_animacao += 1

        if self.tempo_animacao >= self.velocidade_animacao:
            self.tempo_animacao = 0
            self.frame += 1

            if self.frame >= len(self.imagens):
                self.frame = 0

    def desenhar(self, tela, camera_x):

        if self.vivo:

            imagem = self.imagens[self.frame]

            # Vira a imagem dependendo da direção
            if self.direcao == -1:
                imagem = pygame.transform.flip(
                    imagem,
                    True,
                    False
                )

            tela.blit(
                imagem,
                (
                    self.x - camera_x,
                    self.y
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


class Criar_Inimigos:

    def criar(self):

        inimigos = [
            Inimigo(400, 350),
            Inimigo(1200, 350),
            Inimigo(2200, 140)]

        return inimigos

