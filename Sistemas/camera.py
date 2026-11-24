#camera.py
import random


class Camera:

    def __init__(self, largura_mapa):
        self.x = 0
        self.largura_mapa = largura_mapa
        self.tremor = 0
        self.intensidade_tremor = 0
        self.deslocamento_tremor = 0
        self._olhar_a_frente = 0

    def tremer(self, frames=10, intensidade=5):

        self.tremor = frames
        self.intensidade_tremor = intensidade

    @property
    def x_desenho(self):
        """Posição usada para desenhar (inclui o tremor)."""
        return self.x + self.deslocamento_tremor

    def atualizar(self, jogador, largura_tela):

        # Olha um pouco para o lado em que o jogador anda
        alvo_olhar = jogador.direcao * 40
        self._olhar_a_frente += (alvo_olhar - self._olhar_a_frente) * 0.05

        posicao_desejada = jogador.pos_x - 250 + self._olhar_a_frente

        limite_direito = self.largura_mapa - largura_tela

        posicao_desejada = max(0, min(posicao_desejada, limite_direito))

        # Segue o jogador suavemente (em vez de "grudar" nele)
        self.x += (posicao_desejada - self.x) * 0.14

        if abs(posicao_desejada - self.x) < 0.5:
            self.x = posicao_desejada

        self.x = max(0, min(self.x, limite_direito))

        # Tremor de tela
        if self.tremor > 0:

            self.tremor -= 1

            self.deslocamento_tremor = random.uniform(
                -self.intensidade_tremor,
                self.intensidade_tremor
            ) * (self.tremor / max(1, self.tremor + 4))

        else:

            self.deslocamento_tremor = 0
