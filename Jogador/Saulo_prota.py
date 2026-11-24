# Saulo_prota.py

import pygame
import math

from Jogador.personagem import Personagem
from Combate.projetil import ProjetilSaulo
from Sistemas.recursos import carregar_por_altura, carregar_escalada
from configuracoes import LARGURA_MAPA, TECLA_ESQUERDA, TECLA_DIREITA


class Saulo(Personagem):

    ALTURA_SPRITE = 76

    def __init__(self, x, y, esquerda=False):

        super().__init__(x, y)

        # SPRITES (mesma altura nas duas versões, para não "pular"
        # de tamanho ao tomar dano)
        self.sprite_direita = carregar_por_altura(
            "imagens/Saulinho.png",
            self.ALTURA_SPRITE
        )

        self.sprite_esquerda = pygame.transform.flip(
            self.sprite_direita,
            True,
            False
        )

        # Saulo recebendo dano
        self.sprite_dano_direita = carregar_por_altura(
            "imagens/Saulinho_Dano.png",
            self.ALTURA_SPRITE
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
        self.tempo_dano = 0
        self.tempo_sem_controle = 0

        # MOVIMENTO
        self.velocidade = 5
        self.vel_x = 0
        self.aceleracao_chao = 1.0
        self.atrito_chao = 1.2
        self.aceleracao_ar = 0.7
        self.atrito_ar = 0.25
        self.direcao = -1 if esquerda else 1

        # FÍSICA
        self.vel_y = 0
        self.gravidade = 0.5
        self.forca_pulo = -10
        self.velocidade_queda_max = 13
        self.no_chao = True

        # "Coyote time": pequena tolerância para pular logo após sair da
        # borda; "buffer": o pulo apertado um pouco antes de pousar vale.
        self.tempo_coiote = 0
        self.buffer_pulo = 0
        self.COIOTE = 6
        self.BUFFER = 7

        # ESTADO
        self.tem_chave = False
        self.plasmas = 0
        self.recarga_tiro = 0

        # FLUTUAÇÃO
        self.tempo_flutuar = 0
        self.velocidade_flutuar = 0.05
        self.amplitude_flutuar = 3

        # ANIMAÇÃO
        self.escala_x = 1.0
        self.escala_y = 1.0
        self.sombra_y = None
        self.tempo_rastro = 0
        self.efeitos = None


    # MOVIMENTO HORIZONTAL (com aceleração: mais suave)
    def mover_horizontal(self, teclas, largura_mapa=LARGURA_MAPA):

        esquerda = teclas[TECLA_ESQUERDA[0]] or teclas[TECLA_ESQUERDA[1]]
        direita = teclas[TECLA_DIREITA[0]] or teclas[TECLA_DIREITA[1]]

        # Logo após levar dano o controle fica bloqueado por instantes
        # (o empurrão não é cancelado na hora)
        if self.tempo_sem_controle > 0:
            esquerda = direita = False

        # Teclas opostas juntas se anulam
        if esquerda and direita:
            esquerda = direita = False

        aceleracao = (
            self.aceleracao_chao if self.no_chao else self.aceleracao_ar
        )
        atrito = self.atrito_chao if self.no_chao else self.atrito_ar

        if esquerda:
            self.vel_x -= aceleracao
            self.direcao = -1
            self.esquerda = True

        elif direita:
            self.vel_x += aceleracao
            self.direcao = 1
            self.esquerda = False

        elif self.vel_x > 0:
            self.vel_x = max(0, self.vel_x - atrito)

        elif self.vel_x < 0:
            self.vel_x = min(0, self.vel_x + atrito)

        if self.tempo_sem_controle <= 0:
            self.vel_x = max(
                -self.velocidade,
                min(self.velocidade, self.vel_x)
            )

        self.pos_x += self.vel_x

        # Limites do mapa
        if self.pos_x < 0:
            self.pos_x = 0
            self.vel_x = 0

        if self.pos_x + self.largura > largura_mapa:
            self.pos_x = largura_mapa - self.largura
            self.vel_x = 0


    # PULO
    def pular(self):

        # Apenas registra o pedido; o pulo acontece no update()
        # (assim vale o "buffer" e o "coyote time")
        self.buffer_pulo = self.BUFFER

    def soltar_pulo(self):

        # Soltar a tecla no meio do pulo = pulo mais curto
        if self.vel_y < -3:
            self.vel_y *= 0.5

    def _executar_pulo(self):

        self.vel_y = self.forca_pulo
        self.no_chao = False
        self.tempo_coiote = 0
        self.buffer_pulo = 0

        # Estica ao decolar
        self.escala_x = 0.82
        self.escala_y = 1.2

        if self.efeitos is not None:
            self.efeitos.poeira(
                self.pos_x + self.largura / 2,
                self.pos_y + self.altura,
                5
            )


    def _hitbox_pes(self):

        # Margens laterais da colisão (simétricas)
        return self.pos_x + 6, self.pos_x + self.largura - 6


    def aplicar_gravidade(self, plataformas):

        # Guarda a posição antes da gravidade
        pos_y_anterior = self.pos_y
        vel_y_antes = self.vel_y
        estava_no_chao = self.no_chao

        # Aplica a gravidade
        self.vel_y = min(
            self.vel_y + self.gravidade,
            self.velocidade_queda_max
        )
        self.pos_y += self.vel_y

        # Assume que está no ar
        self.no_chao = False

        esquerda_saulo, direita_saulo = self._hitbox_pes()

        # Parte inferior do Saulo
        fundo_anterior = pos_y_anterior + self.altura
        fundo_atual = self.pos_y + self.altura

        # Colisão com as plataformas (pelo topo)
        for plataforma in plataformas:

            topo = plataforma.rect_colisao.top

            if (
                direita_saulo > plataforma.rect_colisao.left
                and esquerda_saulo < plataforma.rect_colisao.right
                and fundo_anterior <= topo
                and fundo_atual >= topo
                and self.vel_y >= 0
            ):
                self.pos_y = topo - self.altura

                # Pouso: comprime o corpo e levanta poeira
                if vel_y_antes > 3 and not estava_no_chao:

                    impacto = min(1.0, vel_y_antes / 11)
                    self.escala_x = 1 + 0.22 * impacto
                    self.escala_y = 1 - 0.2 * impacto

                    if self.efeitos is not None:
                        self.efeitos.poeira(
                            self.pos_x + self.largura / 2,
                            topo,
                            4 + int(4 * impacto)
                        )

                self.vel_y = 0
                self.no_chao = True
                break


    def _calcular_sombra(self, plataformas):

        # Topo da plataforma mais próxima ABAIXO dos pés
        esquerda_saulo, direita_saulo = self._hitbox_pes()
        pes = self.pos_y + self.altura

        melhor = None

        for plataforma in plataformas:

            topo = plataforma.rect_colisao.top

            if (
                topo >= pes - 2
                and direita_saulo > plataforma.rect_colisao.left
                and esquerda_saulo < plataforma.rect_colisao.right
                and (melhor is None or topo < melhor)
            ):
                melhor = topo

        self.sombra_y = melhor


    def update(
        self,
        teclas,
        plataformas,
        largura_mapa=LARGURA_MAPA,
        efeitos=None
    ):

        self.efeitos = efeitos

        self.mover_horizontal(teclas, largura_mapa)

        # Tolerâncias do pulo
        if self.no_chao:
            self.tempo_coiote = self.COIOTE
        elif self.tempo_coiote > 0:
            self.tempo_coiote -= 1

        if self.buffer_pulo > 0:

            if self.no_chao or self.tempo_coiote > 0:
                self._executar_pulo()

            else:
                self.buffer_pulo -= 1

        self.aplicar_gravidade(plataformas)
        self._calcular_sombra(plataformas)

        if self.recarga_tiro > 0:
            self.recarga_tiro -= 1

        # Flutuação
        self.tempo_flutuar += self.velocidade_flutuar

        # Invulnerabilidade
        if self.invulneravel:
            self.tempo_invulnerabilidade -= 1

        if self.tempo_invulnerabilidade <= 0:
            self.invulneravel = False

        if self.tempo_dano > 0:
            self.tempo_dano -= 1

        if self.tempo_sem_controle > 0:
            self.tempo_sem_controle -= 1

        self._atualizar_animacao()


    def _atualizar_animacao(self):

        # Forma-alvo do corpo conforme o movimento
        if not self.no_chao and self.vel_y < -1:
            alvo_x, alvo_y = 0.93, 1.1

        elif not self.no_chao and self.vel_y > 4:
            alvo_x, alvo_y = 0.95, 1.07

        else:
            alvo_x, alvo_y = 1.0, 1.0

        # Aproxima suavemente (suaviza o "squash and stretch")
        self.escala_x += (alvo_x - self.escala_x) * 0.22
        self.escala_y += (alvo_y - self.escala_y) * 0.22

        # Rastro fantasmagórico ao correr
        self.tempo_rastro += 1

        if (
            self.efeitos is not None
            and self.tempo_rastro % 3 == 0
            and (abs(self.vel_x) > 4 or (not self.no_chao and abs(self.vel_y) > 7))
        ):
            self.efeitos.rastro(
                self.pos_x + self.largura / 2 - self.vel_x * 3,
                self.pos_y + self.altura * 0.6
            )


    def receber_dano(self, origem_x=None):
        """Aplica 1 de dano. Retorna False se estava invulnerável."""

        if self.invulneravel:
            return False

        self.vida -= 1
        self.invulneravel = True
        self.tempo_invulnerabilidade = 90
        self.tempo_dano = 16

        # Empurrão para longe da origem do dano
        if origem_x is None:
            sentido = -self.direcao
        else:
            sentido = 1 if self.pos_x + self.largura / 2 >= origem_x else -1

        self.vel_x = 6 * sentido
        self.vel_y = -6
        self.no_chao = False
        self.tempo_coiote = 0
        self.tempo_sem_controle = 12

        return True


    def desenhar(self, tela, camera_x):

        tela_x = self.pos_x - camera_x

        # Flutuação: o fantasma paira um pouco acima do chão
        bob = math.sin(self.tempo_flutuar) * self.amplitude_flutuar

        # Escolhe o sprite
        if self.tempo_dano > 0:

            imagem = (
                self.sprite_dano_esquerda
                if self.esquerda
                else self.sprite_dano_direita
            )

        else:

            imagem = (
                self.sprite_esquerda
                if self.esquerda
                else self.sprite_direita
            )

        # Pisca enquanto está invulnerável
        piscando = (
            self.invulneravel
            and self.tempo_dano <= 0
            and (self.tempo_invulnerabilidade // 4) % 2 == 0
        )

        # SOMBRA no chão (some quando está alto no ar)
        if self.sombra_y is not None:

            distancia = self.sombra_y - (self.pos_y + self.altura)

            if 0 <= distancia < 220:

                forca = 1 - distancia / 220
                largura_sombra = int(46 * (0.55 + 0.45 * forca))

                sombra = pygame.Surface((54, 14), pygame.SRCALPHA)
                pygame.draw.ellipse(
                    sombra,
                    (0, 0, 0, int(110 * forca)),
                    (
                        (54 - largura_sombra) // 2, 2,
                        largura_sombra, 10
                    )
                )

                tela.blit(
                    sombra,
                    (
                        tela_x + self.largura / 2 - 27,
                        self.sombra_y - 8
                    )
                )

        # Deformação (squash/stretch) + inclinação ao se mover
        largura = max(1, int(imagem.get_width() * self.escala_x))
        altura = max(1, int(imagem.get_height() * self.escala_y))

        corpo = pygame.transform.smoothscale(imagem, (largura, altura))

        inclinacao = -self.vel_x * 1.5

        if abs(inclinacao) > 0.5:
            corpo = pygame.transform.rotozoom(corpo, inclinacao, 1.0)

        if piscando:
            corpo = corpo.copy()
            corpo.set_alpha(110)

        # Centralizado na hitbox; base do sprite pouco abaixo dos pés
        centro_x = tela_x + self.largura / 2
        base_y = self.pos_y + self.altura + 4 + bob

        retangulo = corpo.get_rect()
        retangulo.midbottom = (round(centro_x), round(base_y))

        tela.blit(corpo, retangulo)


    def get_rect(self):

        return pygame.Rect(
            self.pos_x,
            self.pos_y,
            self.largura,
            self.altura
        )


    def get_rect_dano(self):
        """Hitbox um pouco menor, usada para receber dano
        (evita dano 'injusto' encostando só de raspão)."""

        return self.get_rect().inflate(-10, -12)


    def atirar(self):

        if self.plasmas < 3 or self.recarga_tiro > 0:
            return None

        self.plasmas -= 3
        self.recarga_tiro = 12

        return ProjetilSaulo(
            self.pos_x + self.largura / 2 + self.direcao * (self.largura / 2 + 22),
            self.pos_y + self.altura * 0.45,
            self.direcao
        )


    def colidir(self, inimigorect):

        rect = self.get_rect_dano()

        return rect.colliderect(inimigorect)


class BarraVidas:

    def __init__(self):

        self.coracao_cheio = carregar_escalada(
            "imagens/corações_1.png", (104, 32)
        )

        self.coracao_meio = carregar_escalada(
            "imagens/corações_2.png", (104, 32)
        )

        self.coracao_vazio = carregar_escalada(
            "imagens/corações_3.png", (104, 32)
        )

        self.icone_chave = carregar_escalada(
            "imagens/chave.png", (45, 22)
        )


    def desenhar(self, tela, player):

        if player.vida >= 3:
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

        # Ícone da chave quando coletada
        if player.tem_chave:

            tela.blit(
                self.icone_chave,
                (
                    x + (imagem.get_width() - self.icone_chave.get_width()) // 2,
                    y + imagem.get_height() + 8
                )
            )
