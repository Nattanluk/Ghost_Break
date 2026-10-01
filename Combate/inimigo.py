import pygame

from Combate.projetil import ProjetilInimigo


class Inimigo:

    def __init__(self, x, y, fase=1):

        self.x = x
        self.y = y
        self.x_inicial = x
        self.largura = 50
        self.altura = 70
        self.vida = 1
        self.vivo = True

        # FASE
        self.fase = fase

        # MOVIMENTO
        self.velocidade = 1
        self.direcao = -1

        self.distancia_patrulha = 190

        # Configuração do movimento da fase
        self.configurar_movimento()

        # FÍSICA
        self.vel_y = 0
        self.gravidade = 0.5
        self.no_chao = False

        # ANIMAÇÃO
        self.carregar_sprites()

        self.frame = 0

        self.tempo_animacao = 0
        self.velocidade_animacao = 15

        # ATAQUE
        self.atirador = None


    # CONFIGURAÇÃO DE MOVIMENTO
    def configurar_movimento(self):

        if self.fase == 1:

            # Movimento normal
            self.velocidade = 2
            self.distancia_patrulha = 190

        elif self.fase == 2:

            # Mais rápido
            self.velocidade = 3
            self.distancia_patrulha = 220

        elif self.fase == 3:

            # Patrulha maior
            self.velocidade = 3
            self.distancia_patrulha = 300

        elif self.fase == 4:

            # Muito rápido
            self.velocidade = 4
            self.distancia_patrulha = 250

        elif self.fase == 5:

            # Mais agressivo
            self.velocidade = 5
            self.distancia_patrulha = 350


    # CARREGAR SPRITEs
    def carregar_sprites(self):

        self.imagens = []

        for numero in range(1, 4):

            caminho = (
                f"imagens/inimigo_"
                f"{self.fase}_{numero}.png"
            )

            imagem = pygame.image.load(
                caminho
            ).convert_alpha()

            imagem = pygame.transform.scale(
                imagem,
                (
                    self.largura,
                    self.altura
                )
            )

            self.imagens.append(imagem)

    # ATUALIZAÇÃO
    def atualizar(self, plataformas):

        if not self.vivo:
            return

        if self.atirador is not None:

            self.atirador.atualizar()

        # MOVIMENTO HORIZONTAL
        self.x += (
            self.velocidade
            * self.direcao
        )

        # Limite direito da patrulha
        if self.x >= (
            self.x_inicial
            + self.distancia_patrulha
        ):

            self.x = (
                self.x_inicial
                + self.distancia_patrulha
            )

            self.direcao = -1

        # Limite esquerdo da patrulha
        if self.x <= (
            self.x_inicial
            - self.distancia_patrulha
        ):

            self.x = (
                self.x_inicial
                - self.distancia_patrulha
            )

            self.direcao = 1

        # GRAVIDADE
        self.vel_y += self.gravidade

        self.y += self.vel_y

        self.no_chao = False


        # COLISÃO COM PLATAFORMAS
        for plataforma in plataformas:

            esquerda_inimigo = (
                self.x + 5
            )

            direita_inimigo = (
                self.x
                + self.largura
                - 5
            )

            if (
                direita_inimigo
                > plataforma.rect.left

                and esquerda_inimigo
                < plataforma.rect.right

                and self.y + self.altura
                >= plataforma.rect.top

                and self.y + self.altura
                <= plataforma.rect.top + 15

                and self.vel_y >= 0
            ):

                self.y = (
                    plataforma.rect.top
                    - self.altura
                )

                self.vel_y = 0

                self.no_chao = True

                break

        # ANIMAÇÃO
        self.tempo_animacao += 1

        if (
            self.tempo_animacao
            >= self.velocidade_animacao
        ):

            self.tempo_animacao = 0
            self.frame += 1

            if self.frame >= len(
                self.imagens
            ):

                self.frame = 0

    # DESENHAR
    def desenhar(self, tela, camera_x):

        if not self.vivo:
            return

        imagem = self.imagens[
            self.frame
        ]

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

    def atirar(self):

        if self.atirador is None:
            return None

        return self.atirador.executar(
            self
        )


class Atirar:

    def __init__(self, intervalo=120):

        self.tempo = 0
        self.intervalo = intervalo


    def atualizar(self):

        self.tempo += 1


    def executar(self, inimigo):

        if self.tempo >= self.intervalo:

            self.tempo = 0

            return ProjetilInimigo(
                inimigo.x,
                inimigo.y
                + inimigo.altura // 2,
                inimigo.direcao
            )

        return None
