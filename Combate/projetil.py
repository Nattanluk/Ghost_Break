#projetil.py
import pygame

class Projetil:

    def __init__(self, x, y, direcao):

        self.x = x
        self.y = y
        # Tamanho do ataque
        self.largura = 45
        self.altura = 25
        self.velocidade = 5.5
        self.direcao = direcao     
        # ANIMAÇÃO
        self.frames = []

        nomes_imagens = [
            "imagens/projetil_1.png",
            "imagens/projetil_3.png",
            "imagens/projetil_2.png"
        ]

        for nome in nomes_imagens:

            imagem = pygame.image.load(nome).convert_alpha()
            imagem = pygame.transform.scale(imagem,(self.largura, self.altura))
            self.frames.append(imagem)

        self.frame_atual = 0
        self.tempo_animacao = 0
        self.velocidade_animacao = 5

    def mover(self):

        self.x += self.velocidade * self.direcao

        self.tempo_animacao += 1

        if self.tempo_animacao >= self.velocidade_animacao:

            self.tempo_animacao = 0
            self.frame_atual += 1

            if self.frame_atual >= len(self.frames):
                self.frame_atual = 0

    def desenhar(self, tela, camera_x):

        imagem = self.frames[self.frame_atual]

        # As imagens originais devem apontar para a DIREITA.
        # Se o ataque estiver indo para a esquerda,
        # espelha a imagem.
        if self.direcao > 0:

            imagem = pygame.transform.flip(imagem,True,False)

        # Posição na tela
        pos_x = int(self.x - camera_x)
        pos_y = int(self.y - (self.altura - 8) / 2)

        tela.blit(imagem,(pos_x, pos_y))

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            self.largura,
            self.altura
        )
        
        
class BarraPlasma:

    def __init__(self):

        tamanho_barra = (120, 70)

        self.barra_0 = pygame.image.load(
            "imagens/nenhum_plasma.png"
        ).convert_alpha()

        self.barra_1 = pygame.image.load(
            "imagens/plasma_pouco.png"
        ).convert_alpha()

        self.barra_2 = pygame.image.load(
            "imagens/plasma_metade.png"
        ).convert_alpha()

        self.barra_3 = pygame.image.load(
            "imagens/plasma_cheio.png"
        ).convert_alpha()

        # Redimensiona as imagens
        self.barra_0 = pygame.transform.scale(
            self.barra_0,
            tamanho_barra
        )

        self.barra_1 = pygame.transform.scale(
            self.barra_1,
            tamanho_barra
        )

        self.barra_2 = pygame.transform.scale(
            self.barra_2,
            tamanho_barra
        )

        self.barra_3 = pygame.transform.scale(
            self.barra_3,
            tamanho_barra
        )

    def desenhar(self, tela, player):

        plasmas = player.plasmas

        if plasmas == 0:

            imagem = self.barra_0

        elif plasmas == 1:

            imagem = self.barra_1

        elif plasmas == 2:

            imagem = self.barra_2

        else:

            imagem = self.barra_3

        tela.blit(
            imagem,
            (19, 5)
        )
        
class GerenciadorProjeteis:

    def __init__(self):
        self.projeteis = []

    def adicionar(self, projetil):

        if projetil is not None:
            self.projeteis.append(projetil)

    def atualizar(self):

        for projetil in self.projeteis:
            projetil.mover()

    def desenhar(self, tela, camera_x):

        for projetil in self.projeteis:

            projetil.desenhar(
                tela,
                camera_x
            )