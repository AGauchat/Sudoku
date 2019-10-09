class Sudok():

    def __init__(self, tablero):

        self.tablero = [[0 for __ in range(9)] for _ in range(9)]
        self.tableroV = tablero

        self.n1 = 0
        self.n2 = 3
        self.n3 = 0
        self.n4 = 3

        i = -1
        j = -1
        for fila in self.tableroV:
            i += 1
            j = -1
            for valor in fila:
                j += 1
                if valor.isdigit():
                    self.tablero[i][j] = valor
                if valor == 'x':
                    self.tablero[i][j] = valor

        self.tableroV = self.tablero

    def verificar_x(self):
        x = 0
        try:
            for i in range(self.n3, self.n4):
                for j in range(self.n1, self.n2):
                    k = self.tablero[i][j]
                    if k == 'x':
                        x += 1
        except:
            return

        if 0 == x:
            if i == (self.n2 - 1) or self.n2 < 9:
                self.n1 = self.n1 + 3
                self.n2 = self.n2 + 3
            else:
                self.n1 = 0
                self.n2 = 3
                self.n4 = self.n4 + 3
                if self.n4 > 9:
                    return
                else:
                    self.n3 = self.n3 + 3

    def verificar_bloque(self, num):
        try:
            for i in range(self.n3, self.n4):
                for j in range(self.n1, self.n2):
                    k = self.tablero[i][j]
                    if num == k:
                        return False
        except:
            return

    def verificar_fila_columna(self, i, j, num):
        for columna in range(0, 9):
            if num == self.tablero[i][columna]:
                return False
        for fila in range(0, 9):
            if num == self.tablero[fila][j]:
                return False

    def verificar_espacio(self):
        for i in range(self.n3, self.n4):
            for j in range(self.n1, self.n2):
                if self.tablero[i][j] == 'x':
                    return i, j

    def insertar_numero(self, num):
        k = self.verificar_espacio()
        if self.verificar_bloque(num) == None and self.verificar_fila_columna(k[0], k[1], num) == None:
            self.tablero[k[0]][k[1]] = num
            self.verificar_x()

            if k == (8, 8):
                return 'Sudoku completado'

            return "Numero ingresado"
        else:
            return "Ingrese otro numero"
