from Sudoku import Sudok
from Api import api


class Interfaz():

    def __init__(self):
        self.tablero = api()
        self.Su = Sudok(self.tablero)

    def jugar(self):
        for i in range(0, 9):
            for j in range(0, 9):
                print(self.Su.tablero[i][j], end=" ")
            print(" ")

        try:
            print("Ingrese fila donde desea poner el numero (0 a 8)")
            f = int(input(">>"))
            print("Ingrese columna donde desea poner el numero (0 a 8)")
            c = int(input(">>"))
            print("Ingrese numero")
            n = input(">>")
            if 1 <= n <= 9:
                print(self.Su.insertar_numero(n, f, c))
            else:
                print('Ingrese un numero correcto')
        except:
            print('Ingrese un numero correcto')

    def estado_juego(self):
        if self.Su.gano() is True:
            return True
        return False


juego = Interfaz()
while juego.estado_juego() is not True:
    juego.jugar()
