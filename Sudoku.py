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

        # Verifica cuantos espacios vacios (x) hay, si no hay ninguno pasa al siguiente bloque

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

        # Verifica que no se repita el numero en el bloque

        try:
            for i in range(self.n3, self.n4):
                for j in range(self.n1, self.n2):
                    k = self.tablero[i][j]
                    if num == k:
                        return False
        except:
            return

    def verificar_fila_columna(self, i, j, num):

        # Verifica que no se repita el numero en el filas y columnas

        for columna in range(0, 9):
            if num == self.tablero[i][columna]:
                return False
        for fila in range(0, 9):
            if num == self.tablero[fila][j]:
                return False

    def verificar_espacio(self):

        # Se fija si hay un espacio vacio (x) para poder colocar un numero y devulve sus coordenadas

        for i in range(self.n3, self.n4):
            for j in range(self.n1, self.n2):
                if self.tablero[i][j] == 'x' or self.tablero[i][j] == ' ':
                    return i, j

    def borrar_numero(self, fila, columna):
        try:
            for i in range(self.n3, self.n4):
                for j in range(self.n1, self.n2):
                    if self.tableroV[i][j] == 'x':
                        self.tablero[int(fila)][int(columna)] = 'x'
                    else:
                        print('Ese numero no se puede borrar')
        except:
            return
