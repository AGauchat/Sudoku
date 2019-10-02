class Sudoku():

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

    def verificar__valor_fijo(self, x, y):

        if self.tableroV[x][y] == 'x':
            return True
        else:
            return False

    def verificar_bloque(self, i, j):
        x = -1
        y = -1