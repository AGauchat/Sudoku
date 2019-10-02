from Sudoku import Sudoku_inicio


class numero():

    def ingresar_numero(self, numero):
        x = -1
        y = -1
        for fila in self.tablero:
            x += 1
            y = 0
            for valor in fila:
                y += 1
                if self.tableroV[x][y] == 'x':
                    self.tablero = numero
                else:
                    return