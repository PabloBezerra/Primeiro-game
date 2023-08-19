# JOGO DA VELHA #

# IMPORTAÇÕES

from PyQt6 import uic, QtWidgets, QtGui
from PyQt6.QtCore import Qt
from random import choice
from time import sleep

# VARIÁVEIS E LISTAS

contador = jogadas = 0
dadosX = []
listaO = []
restantes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
estado = turno = ''

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

    def marcar(self):  # função interna de marcação das aeras
        global contador, jogadas, restantes
        self.marcado = turno

        if self.condicao == False:
            game.informacao.setText('Casa já selecionada. Por favor escolha outra!')
        else:
            contador += 1
            jogadas += 1
            self.condicao = False
            
            if self.marcado == 'X':
                X.mostrar(eval(f'game.area{self.numero}')) 
                dadosX.append(self.numero)
                dadosX.sort()
            else:
                O.mostrar(eval(f'game.area{self.numero}')) 
                listaO.append(self.numero)
                listaO.sort()
            restantes.remove(self.numero)
            verificador()
        QtWidgets.QApplication.processEvents()

class Tipo():  # classe de criação dos simbolos e suas caracteristicas
    def __init__(self, tipo, player='' ,placar=0 ):
        self.tipo = tipo
        self.player = player
        self.placar = placar
    
    def mostrar(self, jan):
        jan.setPixmap(QtGui.QPixmap(f'{self.tipo}.png'))

    def mostrar_over(self,var):
        var.setPixmap(QtGui.QPixmap(f'{self.tipo}_over.png'))


def load(n):  # Função responsavel por dar inicio ao jogo
    global contador
    lobby.close()
    game.show()
    game.placar_playerx.setText('')
    game.placar_playero.setText('')
    X.mostrar(game.placar_imgx)
    O.mostrar(game.placar_imgo)
    limpar()
    game.cortina.show()
    O.placar = X.placar = 00
    game.placarO.setText(str(O.placar).zfill(2))
    game.placarX.setText(str(X.placar).zfill(2))
    O.player = X.player = ''
    contador = 0

    if n == 1:
        escolha.show()
        escolha.btn_caixax.clicked.connect(lambda: config_pvr(1))
        escolha.btn_caixao.clicked.connect(lambda: config_pvr(2))
        escolha.play_robo.clicked.connect(lambda: config_pvr(3))
        escolha.erro_escolha.setText('')
        O.mostrar(escolha.caixaO)
        X.mostrar(escolha.caixaX)
    else:
        pvp.show()
        X.mostrar(pvp.caixaX)
        O.mostrar(pvp.caixaO)
        pvp.play.clicked.connect(config_pvp)


def config_pvp():  # Configurações do modo de jogo pessoa contra pessoa
    global estado
    O.player = str(pvp.player_1.text()).capitalize() if pvp.player_1.text() != '' else 'Player 1'
    X.player = str(pvp.player_2.text()).capitalize() if pvp.player_2.text() != '' else 'Player 2'
    game.cortina.close()
    pvp.close()
    estado = ''
    atualizador()


def config_pvr(n):  # Configurações do modo de jogo pessoa contra robô
    global estado
    if n == 1:
        X.mostrar_over(escolha.caixaX)
        O.mostrar(escolha.caixaO)
        O.player = 'Robô'
        estado = O.tipo
    elif n == 2:
        X.mostrar(escolha.caixaX)
        O.mostrar_over(escolha.caixaO)
        X.player = 'Robô'
        estado = X.tipo
    else:
        if estado == '':
            escolha.erro_escolha.setText('🔺  Por favor! Escolha   🔺')
        else:
            if estado == O.tipo:
                X.player = str(escolha.player_robo.text()).capitalize() if escolha.player_robo.text() != '' else 'Player 1'
            else:
                O.player = str(escolha.player_robo.text()).capitalize() if escolha.player_robo.text() != '' else 'Player 1'
            game.cortina.close()
            escolha.close()
            atualizador()


def atualizador():  # Função respondavel pela atualização do jogo
    global turno
    turno = O.tipo if contador % 2 == 0 else X.tipo
    x = choice(restantes)
    game.placar_playerx.setText(X.player)
    game.placar_playero.setText(O.player)

    if turno == 'O':
        game.informacao.setText(f'Turno de {O.player}') if O.player != 'Robô' else game.informacao.setText(f'Turno do {O.player}')
        O.mostrar_over(game.placar_imgo)
        X.mostrar(game.placar_imgx)
        QtWidgets.QApplication.processEvents()
        if estado == 'O':
            sleep(0.5)
            exec(f'area{x}.marcar()')
    else:
        game.informacao.setText(f'Turno de {X.player}') if X.player != 'Robô' else game.informacao.setText(f'Turno do {X.player}')
        O.mostrar(game.placar_imgo)
        X.mostrar_over(game.placar_imgx)
        QtWidgets.QApplication.processEvents()
        if estado == 'X':
            sleep(0.5)
            exec(f'area{x}.marcar()')


def verificador():  # função que verifica a posição das areas marcadas
    global listaO, placarX
    if comp(listaO, ltop, 'O') or comp(listaO, lcenter, 'O') or comp(listaO, ldwon, 'O') or comp(listaO, cleft, 'O') or comp(listaO, ccenter, 'O') or comp(listaO, cright, 'O') or comp(listaO, d1, 'O') or comp(listaO, d2, 'O'):
        conclusao(1)
        O.placar += 1
        game.placarO.setText(str(O.placar).zfill(2))

    elif comp(dadosX, ltop, 'X') or comp(dadosX, lcenter, 'X') or comp(dadosX, ldwon, 'X') or comp(dadosX, cleft, 'X') or comp(dadosX, ccenter, 'X') or comp(dadosX, cright, 'X') or comp(dadosX, d1, 'X') or comp(dadosX, d2, 'X'):
        conclusao(2)
        X.placar += 1
        game.placarX.setText(str(X.placar).zfill(2))

    elif jogadas == 9:
        conclusao()
    else:
        atualizador()


def comp(li1, li2, l):  # faz análise das posições marcadas com as possiveis possições de vitória e destaca a jogada vitoriosa
    li = []
    for item1 in li1:
        for item2 in li2:
            if item1 == item2:
                li.append(item1)
    if li == li2:
        for n in li2:
            exec(f'{l}.mostrar_over(game.area{n})')
        QtWidgets.QApplication.processEvents()
        sleep(1)
        return True


def conclusao(n= 0):  # Função responsavel pela conclusão da partida e exibição do jogador vitorioso
    game.cortina.show()
    resultado.show()
    if n == 1:
        O.mostrar_over(resultado.logo)
        resultado.resultado.setText(f'{O.player} Venceu!')
    elif n == 2:
        X.mostrar_over(resultado.logo)
        resultado.resultado.setText(f'{X.player} Venceu!')
    else:
        resultado.logo.setPixmap(QtGui.QPixmap('velha.png'))
        resultado.resultado.setText('Deu velha!')


def limpar():  # Função que reseta as configurações para uma nova partida
    global listaO, dadosX, restantes, jogadas, contador
    listaO = []
    dadosX = []
    jogadas = 0
    restantes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    game.cortina.close()
    for n in range(1, 10):
            exec(f'game.area{n}.setText(" ")')
            exec(f'area{n}.condicao = True')
            exec(f"area{n}.marcado = ''")


def reiniciar(n):  #Função de dá inicio a uma nova partida ou retorna ao inicio para acessar outro modo de jogo
    if n == 1:
        limpar()
        atualizador()
    else:
        game.close()
        lobby.show()
        lobby.img_inicial.setPixmap(QtGui.QPixmap('velha.png'))
    resultado.close()


for n in range(1, 10):  # criação da sintâncias das areas
    exec(f'area{n} = Area(n)')

X = Tipo('X')
O = Tipo('O')

# INICIALIZAÇÃO DO GAME

app = QtWidgets.QApplication([])

# Configurando as janelas

lobby = uic.loadUi('Looby.ui')  # janela de entrada
lobby.setFixedSize(1080, 720)
lobby.img_inicial.setPixmap(QtGui.QPixmap('velha.png'))
lobby.setWindowIcon(QtGui.QIcon('velha.png'))
lobby.show()

pvp = uic.loadUi('PvP.ui')  # janela de seleção para pessoa vsrsus pessoa
pvp.setWindowFlags(Qt.WindowType.FramelessWindowHint)
pvp.setWindowModality(Qt.WindowModality.ApplicationModal)
pvp.close()

escolha = uic.loadUi('Escolha.ui')  # janela de seleção conta o pc
escolha.setWindowFlags(Qt.WindowType.FramelessWindowHint)
escolha.setWindowModality(Qt.WindowModality.ApplicationModal)
escolha.close()

game = uic.loadUi('Game.ui')  # janela principal do jogo
game.setFixedSize(1080, 720)
game.setWindowIcon(QtGui.QIcon('velha.png'))
game.close()

resultado = uic.loadUi('Resultado.ui')  # janela final que mostra o resultado
resultado.setWindowFlags(Qt.WindowType.FramelessWindowHint)
resultado.setWindowModality(Qt.WindowModality.ApplicationModal)
resultado.close()

# Configurando botões

lobby.pessoaxrobo.clicked.connect(lambda: load(1))
lobby.pessoacontra.clicked.connect(lambda: load(2))

for num in range(1, 10):
    exec(f'game.btn{num}.clicked.connect(lambda: area{num}.marcar())')

resultado.jogar_novamente.clicked.connect(lambda: reiniciar(1))
resultado.finalizar.clicked.connect(lambda: reiniciar(2))

app.exec()
