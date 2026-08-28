#camera.py
class Camera:

    def __init__(self, largura_mapa):
        self.x = 0
        self.largura_mapa = largura_mapa

    def atualizar(self, jogador, largura_tela):

        posicao_desejada = jogador.pos_x - 250

        limite_direito = self.largura_mapa - largura_tela

        self.x = max(
            0,
            min(posicao_desejada, limite_direito)
        )