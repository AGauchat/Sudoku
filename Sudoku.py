class Sudok():

    def __init__(self, tablero):

        self.tablero = [[0 for __ in range(9)] for _ in range(9)]
        self.tableroV = tablero

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

    def verificar_bloque(self, num, fila, columna):

        # Verifica que no se repita el numero en el bloque

        if (fila < 3):
            fila = 0

        elif (fila >= 3 and fila <= 5):
            fila = 3

        else:
            fila = 6

        if (columna < 3):
            columna = 0

        elif (columna >= 3 and columna <= 5):
            columna = 3

        else:
            columna = 6

        for i in range(3):
            for j in range(3):
                if self.tablero[fila + i][columna + j] == num:
                    return False

        return True

    def verificar_fila_columna(self, i, j, num):

        # Verifica que no se repita el numero en el filas y columnas

        for columna in range(0, 9):
            if num == self.tablero[i][columna]:
                return False
        for fila in range(0, 9):
            if num == self.tablero[fila][j]:
                return False

        return True

    def verificar_x(self, i, j):
        if self.tableroV[i][j] == 'x':
            return True

        return False

    def gano(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.tablero[i][j] == 'x':
                    return False

        return True

    def insertar_numero(self, num, i, j):

        if self.gano is True:
            return 'Ganaste'

        if self.verificar_x(i, j) is True:
            if self.verificar_fila_columna(i, j, num) is True:
                if self.verificar_bloque(num, i, j) is True:

                    self.tablero[i][j] = num
                    return("Numero ingresado")

                else:
                    return("Ingrese otro numero")

            else:
                return("Ingrese otro numero")

        else:
            return("Ingrese otro numero")
