# Personagem.py

class Personagem:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.largura = 40
        self.altura = 60

#atividade --- 21/05
# Foi criada uma classe pai chamada personagem, que guarda algumas informações básicas dos personagens, como posição, largura e altura.
#A classe Saulo funciona como classe filha, herdando essas características da classe personagem usando o conceito de Herança de POO.