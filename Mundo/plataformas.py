import pygame


class Plataforma:

    def __init__(self, x, y, largura, altura, imagem):

        # Área visual
        self.rect = pygame.Rect(
            x, y, largura, altura
        )

        # Área de colisão
        self.rect_colisao = pygame.Rect(
            x - 15, y, largura + 5, altura
        )

        # Sprite da plataforma
        self.imagem = pygame.transform.scale(
            imagem,
            (largura, altura)
        )

    def desenhar(self, tela, camera_x):

        tela.blit(
            self.imagem,
            (self.rect.x - camera_x, self.rect.y)
        )


class Criar_Plataforma:

    def __init__(self, fase=1):

        # Seleciona as sprites de acordo com a fase
        if fase == 1:

            caminho_plataforma = "imagens/plataforma.png"
            caminho_chao = "imagens/chao.png"

        elif fase == 2:

            caminho_plataforma = "imagens/plataforma2.png"
            caminho_chao = "imagens/chao2.png"

        else:

            raise ValueError(
                f"Fase inexistente: {fase}"
            )

        # Carrega as imagens
        self.sprite_plataforma = pygame.image.load(
            caminho_plataforma
        ).convert_alpha()

        self.sprite_chao = pygame.image.load(
            caminho_chao
        ).convert_alpha()

    def criar(self, dados_plataformas, dados_chao):

        plataformas = []

        # Cria os trechos de chão
        for inicio, fim in dados_chao:

            for x in range(inicio, fim):

                plataformas.append(
                    Plataforma(
                        x * 20,
                        410,
                        50,
                        60,
                        self.sprite_chao
                    )
                )

        # Cria as plataformas suspensas
        for x, y, largura, altura in dados_plataformas:

            plataformas.append(
                Plataforma(
                    x,
                    y,
                    largura,
                    altura,
                    self.sprite_plataforma
                )
            )

        return plataformas
