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

        print("Ingrese fila donde desea poner el numero (0 a 8)")
        f = int(input(">>"))
        print("Ingrese columna donde desea poner el numero (0 a 8)")
        c = int(input(">>"))
        print("Ingrese numero")
        n = input(">>")

        print(self.Su.insertar_numero(n, f, c))

    def estado_juego(self):
        if self.Su.gano() is True:
            return True
        return False


juego = Interfaz()
while juego.estado_juego() is not True:
    juego.jugar()
