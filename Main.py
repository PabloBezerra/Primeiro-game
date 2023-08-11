# JOGO DA VELHA #

# IMPORTAÇÕES

from PyQt6 import uic, QtWidgets, QtGui
from random import randint

# VARIÁVEIS E LISTAS

contador = 0
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
        global contador
        self.marcado = 'O' if contador % 2 == 0 else 'X'

        if self.condicao == True:
            exec(f"game.area{self.numero}.setPixmap(QtGui.QPixmap('{self.marcado}.png'))")
            self.condicao = False
            game.informacao.setText('')
            contador += 1
        else:
            game.informacao.setText('Casa já selecionada. Por favor escolha outra!')

        if self.marcado == 'X':
            dadosX.append(self.numero)
            dadosX.sort()
        elif self.marcado == 'O':
            dadosO.append(self.numero)
            dadosO.sort()
        verificador()


def verificador():
    if comp(dadosO, ltop) or comp(dadosO, lcenter) or comp(dadosO, ldwon) or comp(dadosO, cleft) or comp(dadosO, ccenter) or comp(dadosO, cright) or comp(dadosO, d1) or comp(dadosO, d2):
        print('O venceu')
    elif comp(dadosO, ltop) or comp(dadosO, lcenter) or comp(dadosO, ldwon) or comp(dadosO, cleft) or comp(dadosO, ccenter) or comp(dadosO, cright) or comp(dadosO, d1) or comp(dadosO, d2):
        print('X venceu')
    else:
        print('Empate')


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


# INICIALIZAÇÃO DO GAME

app = QtWidgets.QApplication([])
lobby = uic.loadUi('Looby.ui')
game = uic.loadUi('Game.ui')

lobby.show()
game.close()

lobby.pessoaxrobo.clicked.connect(lambda: load(1))
lobby.pessoacontra.clicked.connect(lambda: load(2))

for n in range(1, 10):
    exec(f'area{n} = Area({n})\n'
        f'game.btn{n}.clicked.connect(lambda: area{n}.marcar())')

app.exec()
