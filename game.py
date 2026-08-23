#game.py
import pygame
from Saulo_prota import Saulo
from menu import Menu
from mapa import Mapa
from inimigo import Inimigo
from gameover import GameOver
from fase_concluida import FaseConcluida


LARGURA = 800
ALTURA = 450


class Jogo:

    def __init__(self):

        pygame.init()
        
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        
        self.fundo = pygame.image.load(
            "imagens/fundo_nivel1.png"
        ).convert()

        self.fundo = pygame.transform.scale(
            self.fundo,
            (LARGURA, ALTURA)
        )

        pygame.display.set_caption("Ghost_Break")

        self.clock = pygame.time.Clock()
        self.player = Saulo(100, 350,"imagens/Saulinho.png")
        self.camera_x = 0
        self.chao_y = 410
        self.mensagem_porta = False
        self.mapa = Mapa()
        self.projeteis = []
        self.inimigos = [Inimigo(400, 350),Inimigo(1200, 350), Inimigo(2200, 140)]

        self.coracao_cheio = pygame.image.load(
            "imagens/corações_1.png"
        ).convert_alpha()

        self.coracao_meio = pygame.image.load(
            "imagens/corações_2.png"
        ).convert_alpha()

        self.coracao_vazio = pygame.image.load(
            "imagens/corações_3.png"
        ).convert_alpha()
        
        
        
        self.barra_plasma_0 = pygame.image.load(
            "imagens/nenhum_plasma.png"
        ).convert_alpha()

        self.barra_plasma_1 = pygame.image.load(
            "imagens/plasma_pouco.png"
        ).convert_alpha()

        self.barra_plasma_2 = pygame.image.load(
            "imagens/plasma_metade.png"
        ).convert_alpha()

        self.barra_plasma_3 = pygame.image.load(
            "imagens/plasma_cheio.png"
        ).convert_alpha()


        # Tamanho da barra de plasma
        tamanho_barra = (120, 70)

        self.barra_plasma_0 = pygame.transform.scale(
            self.barra_plasma_0, tamanho_barra
        )

        self.barra_plasma_1 = pygame.transform.scale(
            self.barra_plasma_1, tamanho_barra
        )

        self.barra_plasma_2 = pygame.transform.scale(
            self.barra_plasma_2, tamanho_barra
        )

        self.barra_plasma_3 = pygame.transform.scale(
            self.barra_plasma_3, tamanho_barra
        )
        
        

    def reiniciar_jogo(self):

        # Cria um novo jogador
        # Isso faz a vida voltar ao valor inicial
        self.player = Saulo(100, 350,"imagens/Saulinho.png")

        # Remove os projéteis antigos
        self.projeteis = []

        # Cria os inimigos novamente
        self.inimigos = [
            Inimigo(400, 350), 
            Inimigo(1200, 350),
            Inimigo(2200,  140)
            ]

        # Cria o mapa novamente
        # A chave também volta para o lugar
        self.mapa = Mapa()

        self.camera_x = 0

    def loop_jogo(self):

        rodando = True

        while rodando:

            self.clock.tick(60)

            # EVENTOS
            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:
                    return "sair"

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        self.player.pular()

                    if evento.key == pygame.K_s:
                        projetil = self.player.atirar()

                        if projetil is not None:
                            self.projeteis.append(projetil)

            # GAME OVER
            if self.player.vida <= 0:

                print("ENTROU NO GAME OVER")
                gameover = GameOver(self)
                resultado = gameover.executar()

                # ENTER
                if resultado == "jogar":
                    self.reiniciar_jogo()
                    continue

                # ESC
                if resultado == "menu":
                    return "menu"

                # Fechar jogo
                if resultado == "sair":
                    return "sair"

            # ATUALIZAÇÃO DO JOGADOR
            teclas = pygame.key.get_pressed()

            self.player.update(
                teclas,
                self.mapa.plataformas
            )

            # VERIFICA SE O JOGADOR CAIU NO BURACO
            if self.player.pos_y > ALTURA + 50:
                self.player.vida = 0

            # ATUALIZAÇÃO DOS INIMIGOS
            for inimigo in self.inimigos:
                inimigo.atualizar(
                    self.mapa.plataformas
    )
 
            # PROJÉTEIS
            for projetil in self.projeteis:
                projetil.mover()


            # COLISÃO DOS PROJÉTEIS
            # COM OS INIMIGOS
            for projetil in self.projeteis[:]:
                for inimigo in self.inimigos:

                    if (
                        inimigo.vivo
                        and projetil.get_rect().colliderect(
                            inimigo.get_rect()
                        )
                    ):

                        inimigo.tomar_dano()

                        if projetil in self.projeteis:

                            self.projeteis.remove(
                                projetil
                            )

                        break

  
            # COLISÃO DO JOGADOR
            # COM OS INIMIGOS
            for inimigo in self.inimigos:

                if (
                    inimigo.vivo
                    and not self.player.invulneravel
                    and self.player.get_rect().colliderect(
                        inimigo.get_rect()
                    )
                ):

                    self.player.vida -= 1
                    self.player.invulneravel = True
                    self.player.tempo_invulnerabilidade = 60


            # PORTA
            if self.player.get_rect().colliderect(
                self.mapa.porta.rect
            ):

                # Se tiver a chave, conclui a fase
                if self.player.tem_chave:

                    tela_fase = FaseConcluida(
                        self.tela,
                        self.clock
                    )

                    resultado = tela_fase.executar()

                    if resultado == "sair":
                        return "sair"

                    if resultado == "menu":
                        return "menu"

                    if resultado == "proxima":
                        self.reiniciar_jogo()
                        return "menu"

                # Se não tiver a chave, mostra a mensagem
                else:
                    self.mensagem_porta = True

            else:

                # Saiu de perto da porta
                self.mensagem_porta = False

        
            # CHAVE
            if (
                    not self.mapa.chave.coletada
                    and self.player.get_rect().colliderect(
                        self.mapa.chave.rect
                    )
                ):

                    self.mapa.chave.coletada = True
                    self.player.tem_chave = True
                    print("Chave coletada!")


            # PLASMAS
            for plasma in self.mapa.plasmas:

                if (
                    not plasma.coletado
                    and self.player.get_rect().colliderect(
                        plasma.get_rect()
                    )
                ):

                    plasma.coletado = True
                    self.player.plasmas += 1

                    print(
                        "Plasma coletado!",
                        self.player.plasmas
                    )
  
            # CÂMERA

            # Mantém o Saulo mais para a esquerda da tela
            posicao_camera_desejada = self.player.pos_x - 250

            self.camera_x = max(
                0,
                min(posicao_camera_desejada, 3000 - LARGURA)
            )

            # Limites da câmera
            limite_esquerdo = 0
            limite_direito = 3000 - LARGURA

            # Impede a câmera de sair dos limites do mapa
            self.camera_x = max(
                limite_esquerdo,
                min(posicao_camera_desejada, limite_direito)
            )


            # DESENHO
            self.tela.blit(
                self.fundo,
                (0, 0)
            )

            # Plataformas
            for plataforma in self.mapa.plataformas:

                plataforma.desenhar(
                    self.tela,
                    self.camera_x
                )

            # Inimigos
            for inimigo in self.inimigos:

                inimigo.desenhar(
                    self.tela,
                    self.camera_x
                )

            # Porta
            self.mapa.porta.desenhar(
                self.tela,
                self.camera_x
            )

            # Chave
            self.mapa.chave.desenhar(
                self.tela,
                self.camera_x
            )
            
            # Plasmas

            for plasma in self.mapa.plasmas:
                plasma.desenhar(
                    self.tela,
                    self.camera_x
                )

            # Jogador
            self.player.desenhar(
                self.tela,
                self.camera_x
            )

            # Mensagem da porta
            self.desenhar_mensagem_porta()

            fonte = pygame.font.SysFont(
                "Arial",
                24,
                bold=True
            )
            
            # Barra de plasma
            self.desenhar_barra_plasma()
            
            #vidas
            self.desenhar_vidas()

            # Projéteis
            for projetil in self.projeteis:

                projetil.desenhar(
                    self.tela,
                    self.camera_x
                )

            pygame.display.flip()
        return "menu"
    
    def desenhar_mensagem_porta(self):

        if not self.mensagem_porta:
            return

        fonte = pygame.font.SysFont(
            "Arial",
            22,
            bold=True
        )

        texto = fonte.render(
            "Você precisa da chave!",
            True,
            (255, 255, 255)
        )

        # Tamanho da caixa
        largura_caixa = texto.get_width() + 40
        altura_caixa = texto.get_height() + 20

        # Centraliza a caixa na tela
        x = (LARGURA - largura_caixa) // 2
        y = ALTURA - altura_caixa - 20

        # Fundo da caixa
        pygame.draw.rect(
            self.tela,
            (15, 20, 30),
            (x, y, largura_caixa, altura_caixa),
            border_radius=8
        )

        # Borda
        pygame.draw.rect(
            self.tela,
            (80, 180, 255),
            (x, y, largura_caixa, altura_caixa),
            2,
            border_radius=8
        )

        # Texto
        texto_x = x + (largura_caixa - texto.get_width()) // 2
        texto_y = y + (altura_caixa - texto.get_height()) // 2

        self.tela.blit(
            texto,
            (texto_x, texto_y)
        )

    def iniciar(self):
        menu = Menu(self)
        menu.executar()

    def desenhar_vidas(self):

        if self.player.vida == 3:
            imagem = self.coracao_cheio

        elif self.player.vida == 2:
            imagem = self.coracao_meio

        else:
            imagem = self.coracao_vazio

        # Coloca a barra de vidas no canto superior direito
        x = LARGURA - imagem.get_width() - 20
        y = 20

        self.tela.blit(imagem, (x, y))
        
    def desenhar_barra_plasma(self):

        plasmas = self.player.plasmas

        if plasmas == 0:
            imagem = self.barra_plasma_0

        elif plasmas == 1:
            imagem = self.barra_plasma_1

        elif plasmas == 2:
            imagem = self.barra_plasma_2

        else:
            imagem = self.barra_plasma_3

        self.tela.blit(
            imagem,
            (15, 20)
        )