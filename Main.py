# JOGO DA VELHA #

# IMPORTAÇÕES

from PyQt6 import uic, QtWidgets, QtGui
from PyQt6.QtCore import Qt
from random import choice
from time import sleep

# VARIÁVEIS E LISTAS

contador = 0
jogadas = 0
placarX = 0
placarO = 0
dadosX = []
dadosO = []
restantes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bot = False
estado = ''

ltop = [1, 2, 3]
lcenter = [4, 5, 6]
ldwon = [7, 8, 9]
cleft = [1, 4, 7]
ccenter = [2, 5, 8]
cright = [3, 6, 9]
d1 = [1, 5, 9]
d2 = [3, 5, 7]

# FUNÇÕES DE OPERAÇÃO


class Area():  # classe de criação das areas que compõe o jogo da velha
    def __init__(self, numero, marcado='', condicao=True):
        self.numero = numero
        self.marcado = marcado
        self.condicao = condicao

    def marcar(self):
        global contador, jogadas, restantes
        self.marcado = 'O' if contador % 2 == 0 else 'X'

        if self.condicao == False:
            game.informacao.setText('Casa já selecionada. Por favor escolha outra!')
        else:
            exec(f"game.area{self.numero}.setPixmap(QtGui.QPixmap('{self.marcado}.png'))")
            contador += 1
            jogadas += 1
            self.condicao = False
            
            if self.marcado == 'X':
                dadosX.append(self.numero)
                dadosX.sort()
            elif self.marcado == 'O':
                dadosO.append(self.numero)
                dadosO.sort()

            restantes.remove(self.numero)
            verificador()
        QtWidgets.QApplication.processEvents()


def verificador():  # função que verifica a posição das areas marcadas  
    global placarO, placarX
    if comp(dadosO, ltop) or comp(dadosO, lcenter) or comp(dadosO, ldwon) or comp(dadosO, cleft) or comp(dadosO, ccenter) or comp(dadosO, cright) or comp(dadosO, d1) or comp(dadosO, d2):
        conslusao('O')
        placarO += 1
        game.placarO.setText(str(placarO).zfill(2))

    elif comp(dadosX, ltop) or comp(dadosX, lcenter) or comp(dadosX, ldwon) or comp(dadosX, cleft) or comp(dadosX, ccenter) or comp(dadosX, cright) or comp(dadosX, d1) or comp(dadosX, d2):
        conslusao('X')
        placarX += 1
        game.placarX.setText(str(placarX).zfill(2))

    elif jogadas == 9:
        conslusao()
    else:
        atualizador()


def atualizador():  # função qua atualiza a vez do jogador na partida
    x = choice(restantes)
    if contador % 2 == 0:
        game.informacao.setText('Turno do -> O')
        game.placar_imgx.setPixmap(QtGui.QPixmap('X.png'))
        game.placar_imgo.setPixmap(QtGui.QPixmap('O_over.png'))
        QtWidgets.QApplication.processEvents()
        if bot and estado == 'O':
            sleep(0.5)
            exec(f'area{x}.marcar()')
    else:
        game.informacao.setText('Turno do -> X')
        game.placar_imgx.setPixmap(QtGui.QPixmap('X_over.png'))
        game.placar_imgo.setPixmap(QtGui.QPixmap('O.png'))
        QtWidgets.QApplication.processEvents()
        if bot and estado == 'X':
            sleep(0.5)
            exec(f'area{x}.marcar()')


def conslusao(m=''):  # função que informa o resultado da partida
    if m == 'X' or m == 'O':
        resultado.show()
        resultado.resultado.setText('VENCEU!')
        resultado.logo.setPixmap(QtGui.QPixmap(f'{m}_over.png'))
    else:
        resultado.show()
        resultado.resultado.setText('EMPATE!')
        resultado.logo.setPixmap(QtGui.QPixmap('velha.png'))


def play_novamente():  # função de reinicialização ou encerramento do jogo
    limpar()
    resultado.close()
    atualizador()


def finalizar():
    resultado.close()
    game.close()
    lobby.show()


def limpar():
    global dadosO, dadosX, jogadas, restantes
    dadosO = []
    dadosX = []
    jogadas = 0
    restantes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for n in range(1, 10):
        exec(f'game.area{n}.setText(" ")')
        exec(f'area{n}.condicao = True')
        exec(f"area{n}.marcado = ''")


def config(c):
    global contador, estado
    if c == 'O':
        contador = 1
        estado = 'O'
    else:
        contador = 0
        estado = 'X'
    escolha.close()
    atualizador()


def comp(li1, li2):
    li = []
    for item1 in li1:
        for item2 in li2:
            if item1 == item2:
                li.append(item1)
    if li == li2:
        return True


def load(n):
    global placarO, placarX, bot
    lobby.close()
    game.show()
    limpar()
    placarX = 0
    game.placarX.setText(str(placarX).zfill(2))
    placarO = 0
    game.placarO.setText(str(placarX).zfill(2))
    game.placar_imgx.setPixmap(QtGui.QPixmap('X.png'))
    game.placar_imgo.setPixmap(QtGui.QPixmap('O_over.png'))
    if n == 1:
        bot = True
        escolha.show()
        escolha.caixax.setPixmap(QtGui.QPixmap('X_over.png'))
        escolha.caixao.setPixmap(QtGui.QPixmap('O_over.png'))
    else:
        bot = False


for n in range(1, 10):
    exec(f'area{n} = Area(n)')

# INICIALIZAÇÃO DO GAME

app = QtWidgets.QApplication([])

# Configurando as janelas

lobby = uic.loadUi('Looby.ui')  # janela de entrada
lobby.setFixedSize(800, 600)
lobby.show()

escolha = uic.loadUi('Escolha.ui')  # janela de escolha de peças
escolha.setWindowFlags(Qt.WindowType.FramelessWindowHint)
escolha.setWindowModality(Qt.WindowModality.ApplicationModal)
escolha.close()

game = uic.loadUi('Game.ui')  # janela principal do jogo
game.setFixedSize(800, 600)
game.close()

resultado = uic.loadUi('Resultado.ui')  # janela final que mostra o resultado
resultado.setWindowFlags(Qt.WindowType.FramelessWindowHint)
resultado.setWindowModality(Qt.WindowModality.ApplicationModal)
resultado.close()

# Configurando botões

lobby.pessoaxrobo.clicked.connect(lambda: load(1))
lobby.pessoacontra.clicked.connect(lambda: load(2))

escolha.btn_caixax.clicked.connect(lambda: config('O'))
escolha.btn_caixao.clicked.connect(lambda: config('X'))

for num in range(1, 10):
    exec(f'game.btn{num}.clicked.connect(lambda: area{num}.marcar())')

resultado.jogar_novamente.clicked.connect(play_novamente)
resultado.finalizar.clicked.connect(finalizar)

app.exec()
