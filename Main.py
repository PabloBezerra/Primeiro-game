# JOGO DA VELHA #

# IMPORTAÇÕES

from PyQt6 import uic, QtWidgets, QtGui

# VARIÁVEIS E LISTAS

contador = 0
jogadas = 0
placarX = 00
placarO = 00
dadosX = []
dadosO = []

ltop = [1, 2, 3]
lcenter = [4, 5, 6]
ldwon = [7, 8, 9]
cleft= [1, 4, 7]
ccenter = [2, 5, 8]
cright = [3, 6, 9]
d1 = [1, 5, 9]
d2 = [3, 5, 7]

# FUNÇÕES DE OPERAÇÃO

class Area():
    def __init__(self, numero, marcado='', condicao=True):
        self.numero = numero
        self.marcado = marcado
        self.condicao = condicao

    def marcar(self):
        global contador, jogadas
        self.marcado = 'O' if contador % 2 == 0 else 'X'
        
        if self.condicao == True:
            exec(f"game.area{self.numero}.setPixmap(QtGui.QPixmap('{self.marcado}.png'))")
            self.condicao = False
            game.informacao.setText('')
            contador += 1
            jogadas += 1
        else:
            game.informacao.setText('Casa já selecionada. Por favor escolha outra!')

        if self.marcado == 'X':
            dadosX.append(self.numero)
            dadosX.sort()
        elif self.marcado == 'O':
            dadosO.append(self.numero)
            dadosO.sort()
        verificador()
        atualizador()
    

def verificador():
    if comp(dadosO, ltop) or comp(dadosO, lcenter) or comp(dadosO, ldwon) or comp(dadosO, cleft) or comp(dadosO, ccenter) or comp(dadosO, cright) or comp(dadosO, d1) or comp(dadosO, d2):
        conslusao('O')
    elif comp(dadosX, ltop) or comp(dadosX, lcenter) or comp(dadosX, ldwon) or comp(dadosX, cleft) or comp(dadosX, ccenter) or comp(dadosX, cright) or comp(dadosX, d1) or comp(dadosX, d2):
        conslusao('X')
    elif jogadas == 9:
        conslusao()


def atualizador():
    if contador % 2 == 0:
        game.informacao.setText('Turno do -> O')
        game.placar_imgx.setPixmap(QtGui.QPixmap('X.png'))
        game.placar_imgo.setPixmap(QtGui.QPixmap('O_over.png'))
    else:
        game.informacao.setText('Turno do -> X')
        game.placar_imgx.setPixmap(QtGui.QPixmap('X_over.png'))
        game.placar_imgo.setPixmap(QtGui.QPixmap('O.png'))


def conslusao(m=''):
    if m == 'X' or m == 'O':
        resultado.show()
        resultado.resultado.setText('VENCEU!')
        resultado.logo.setPixmap(QtGui.QPixmap(f'{m}_over.png'))
    else:
        resultado.show()
        resultado.resultado.setText('EMPATE!')
        resultado.logo.setPixmap(QtGui.QPixmap('velha.png'))


def play_novamente():
    limpar()
    resultado.close()


def finalizar():
    resultado.close()
    game.close()
    lobby.show()


def limpar():
    global dadosO, dadosX , jogadas
    dadosO = []
    dadosX = []
    jogadas = 0

    for n in range(1, 10):
        exec(f'game.area{n}.setText(" ")')
        exec(f'area{n}.condicao = True')
        exec(f"area{n}.marcado = ''")


def comp(li1, li2):
    li = []
    for item1 in li1:
        for item2 in li2:
            if item1 == item2:
                li.append(item1)
    if li == li2:
        return True


def load(n):
    lobby.close()
    game.show()
    if jogadas != 0:
        limpar()
    game.placar_imgx.setPixmap(QtGui.QPixmap('X.png'))
    game.placar_imgo.setPixmap(QtGui.QPixmap('O_over.png'))


# INICIALIZAÇÃO DO GAME

app = QtWidgets.QApplication([])
lobby = uic.loadUi('Looby.ui')
game = uic.loadUi('Game.ui')
resultado = uic.loadUi('Resultado.ui')

lobby.show()
game.close()
resultado.close()

lobby.pessoaxrobo.clicked.connect(lambda: load(1))
lobby.pessoacontra.clicked.connect(lambda: load(2))

for n in range(1, 10):
    exec(f'area{n} = Area(n)')
    exec(f'game.btn{n}.clicked.connect(lambda: area{n}.marcar())')

resultado.jogar_novamente.clicked.connect(play_novamente)
resultado.finalizar.clicked.connect(finalizar)

app.exec()
