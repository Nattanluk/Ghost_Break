import math

import pygame

from Combate.projetil import ProjetilInimigo
from Sistemas.recursos import carregar_por_altura


class Inimigo:

    ALTURA_SPRITE = 76
    SEQUENCIA_ANIMACAO = (0, 1, 2, 1)
    DURACAO_MORTE = 18

    def __init__(self, x, y, fase=1):

        self.x = x
        self.y = y
        self.x_inicial = x
        self.largura = 46
        self.altura = 64
        self.vida = 1
        self.vivo = True
        self.tempo_morte = 0

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

        # Plataforma onde o inimigo patrulha (os limites da patrulha
        # respeitam as bordas dela: o inimigo não cai mais no vazio)
        self.plataforma = None

        # ANIMAÇÃO
        self.carregar_sprites()

        self.frame = 0

        self.tempo_animacao = 0
        self.velocidade_animacao = 9

        self.tempo_visual = (x * 0.05) % math.tau

        # ATAQUE
        self.atirador = None


    # CONFIGURAÇÃO DE MOVIMENTO
    def configurar_movimento(self):

        if self.fase == 1:

            # Movimento normal
            self.velocidade = 1.6
            self.distancia_patrulha = 190

        elif self.fase == 2:

            # Mais rápido
            self.velocidade = 2.2
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

        # As sprites só existem para as fases 1 e 2.
        # Fases sem arte própria reutilizam a da fase 2.
        tema = self.fase if self.fase in (1, 2) else 2

        self.imagens = []

        for numero in range(1, 4):

            caminho = f"imagens/inimigo_{tema}_{numero}.png"

            # Proporção preservada (antes todas eram esticadas
            # para 50x70, deformando os frames).
            self.imagens.append(
                carregar_por_altura(caminho, self.ALTURA_SPRITE)
            )

    # LIMITES DA PATRULHA
    def limites_patrulha(self):

        esquerda = self.x_inicial - self.distancia_patrulha
        direita = self.x_inicial + self.distancia_patrulha

        if self.plataforma is not None:

            esquerda = max(esquerda, self.plataforma.rect.left)

            direita = min(
                direita,
                self.plataforma.rect.right - self.largura
            )

        return esquerda, direita

    # ATUALIZAÇÃO
    def atualizar(self, plataformas):

        if not self.vivo:

            if self.tempo_morte > 0:
                self.tempo_morte -= 1

            return

        self.tempo_visual += 0.12

        if self.atirador is not None:

            self.atirador.atualizar()

        # Faz uma pausa enquanto carrega o tiro (aviso para o jogador)
        parado = (
            self.atirador is not None
            and self.atirador.carregando
        )

        # MOVIMENTO HORIZONTAL
        if not parado:

            self.x += (
                self.velocidade
                * self.direcao
            )

        esquerda, direita = self.limites_patrulha()

        # Limite direito da patrulha
        if self.x >= direita:

            self.x = direita
            self.direcao = -1

        # Limite esquerdo da patrulha
        if self.x <= esquerda:

            self.x = esquerda
            self.direcao = 1

        # GRAVIDADE
        y_anterior = self.y

        self.vel_y = min(self.vel_y + self.gravidade, 14)

        self.y += self.vel_y

        self.no_chao = False

        # COLISÃO COM PLATAFORMAS (apenas pelo topo)
        for plataforma in plataformas:

            esquerda_inimigo = self.x + 6
            direita_inimigo = self.x + self.largura - 6

            fundo_anterior = y_anterior + self.altura
            fundo_atual = self.y + self.altura

            if (
                direita_inimigo > plataforma.rect.left
                and esquerda_inimigo < plataforma.rect.right
                and fundo_anterior <= plataforma.rect.top + 1
                and fundo_atual >= plataforma.rect.top
                and self.vel_y >= 0
            ):

                self.y = plataforma.rect.top - self.altura
                self.vel_y = 0
                self.no_chao = True

                if self.plataforma is not plataforma:
                    self.plataforma = plataforma

                break

        # Caiu para fora do mundo: remove silenciosamente
        if self.y > 900:
            self.vivo = False
            self.tempo_morte = 0

        # ANIMAÇÃO
        if not parado:

            self.tempo_animacao += 1

            if self.tempo_animacao >= self.velocidade_animacao:

                self.tempo_animacao = 0
                self.frame = (
                    (self.frame + 1) % len(self.SEQUENCIA_ANIMACAO)
                )

    # DESENHAR
    def desenhar(self, tela, camera_x):

        if not self.vivo and self.tempo_morte <= 0:
            return

        tela_x = self.x - camera_x

        if not (-120 < tela_x < tela.get_width() + 120):
            return

        centro_x = tela_x + self.largura / 2
        base_y = self.y + self.altura

        # Sombra no chão
        if self.vivo and self.no_chao:

            sombra = pygame.Surface((54, 14), pygame.SRCALPHA)
            pygame.draw.ellipse(sombra, (0, 0, 0, 90), (0, 0, 54, 14))
            tela.blit(sombra, (centro_x - 27, base_y - 8))

        imagem = self.imagens[
            self.SEQUENCIA_ANIMACAO[self.frame]
        ]

        # Vira a imagem dependendo da direção
        if self.direcao == -1:

            imagem = pygame.transform.flip(
                imagem,
                True,
                False
            )

        # Respiração / passo: estica e comprime levemente
        passo = math.sin(self.tempo_visual)
        escala_x = 1 - 0.035 * passo
        escala_y = 1 + 0.045 * passo

        largura = imagem.get_width()
        altura = imagem.get_height()

        # Efeito de morte: encolhe e some
        alfa = 255

        if not self.vivo:

            fracao = self.tempo_morte / self.DURACAO_MORTE

            escala_x *= 0.6 + 0.6 * (1 - fracao)
            escala_y *= fracao
            alfa = int(255 * fracao)

        largura = max(1, int(largura * escala_x))
        altura = max(1, int(altura * escala_y))

        if (largura, altura) != imagem.get_size():
            imagem = pygame.transform.scale(imagem, (largura, altura))

        if alfa < 255:
            imagem = imagem.copy()
            imagem.set_alpha(alfa)

        # Alerta de tiro: brilho rosado
        if self.vivo and self.atirador is not None and self.atirador.carregando:

            pulso = 40 + int(
                50 * abs(math.sin(self.atirador.carga * 0.5))
            )

            aviso = pygame.Surface((70, 70), pygame.SRCALPHA)
            pygame.draw.circle(aviso, (255, 80, 170, pulso), (35, 35), 32)

            tela.blit(
                aviso,
                (
                    centro_x - 35 + self.direcao * 8,
                    base_y - self.altura * 0.55 - 35
                )
            )

        # Pés alinhados com a base da hitbox
        tela.blit(
            imagem,
            (
                centro_x - largura / 2,
                base_y - altura + 4
            )
        )


    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            self.largura,
            self.altura
        )

    @property
    def centro_x(self):

        return self.x + self.largura / 2


    def tomar_dano(self):

        self.vida -= 1

        if self.vida <= 0 and self.vivo:

            self.vivo = False
            self.tempo_morte = self.DURACAO_MORTE

    def atirar(self, jogador=None):

        if self.atirador is None or not self.vivo:
            return None

        return self.atirador.executar(
            self,
            jogador
        )


class Atirar:

    def __init__(self, intervalo=120, alcance=430, preparo=22):

        self.tempo = 0
        self.intervalo = intervalo
        self.alcance = alcance
        self.preparo = preparo
        self.carga = 0


    @property
    def carregando(self):

        return self.carga > 0


    def atualizar(self):

        self.tempo += 1


    def _alvo_a_vista(self, inimigo, jogador):

        if jogador is None:
            return True

        alvo = jogador.get_rect()

        dx = alvo.centerx - inimigo.centro_x
        dy = alvo.centery - (inimigo.y + inimigo.altura / 2)

        # Só atira para a frente, dentro do alcance e mais ou
        # menos na mesma altura (ou seja, nunca atira "no nada")
        return (
            dx * inimigo.direcao > 0
            and abs(dx) <= self.alcance
            and abs(dy) <= 120
        )


    def executar(self, inimigo, jogador=None):

        # Fase de preparo: o inimigo para e brilha antes de atirar
        if self.carga > 0:

            self.carga -= 1

            if self.carga > 0:
                return None

            self.tempo = 0

            return ProjetilInimigo(
                inimigo.centro_x + inimigo.direcao * (inimigo.largura / 2 + 8),
                inimigo.y + inimigo.altura * 0.45,
                inimigo.direcao
            )

        if self.tempo >= self.intervalo and self._alvo_a_vista(
            inimigo, jogador
        ):

            self.carga = self.preparo

        return None
