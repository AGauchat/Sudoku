import os
from Sudoku import Sudok
from Api import api


class Interfaz():

    def __init__(self):
        self.tablero = api()
        self.Su = Sudok(self.tablero)

    def jugar(self):
        print('\n-SUDOKU-')
        for i in range(0, 9):
            for j in range(0, 9):
                print(self.Su.tablero[i][j], end=" ")
            print(" ")

        try:
            print("\nIngrese fila donde desea poner el numero (0 a 8)")
            f = int(input(">>"))
            if self.verificar_fyc(f) is True:
                print("\nIngrese columna donde desea poner el numero (0 a 8)")
                c = int(input(">>"))
                if self.verificar_fyc(c) is True:
                    print("\nIngrese numero")
                    n = int(input(">>"))
                    if self.verificar_num(n) is True:
                        os.system("clear")
                        n = str(n)
                        print(self.Su.insertar_numero(n, f, c))
                    else:
                        os.system("clear")
                        print('-- Numero incorrecto --')
                else:
                    os.system("clear")
                    print('-- Fila o columna no válida --')
            else:
                os.system("clear")
                print('-- Fila o columna no válida --')
        except:
            os.system("clear")
            print('-- Ingrese un numero --')

    def verificar_num(self, n):
        if 1 <= n <= 9:
            return True
        else:
            return False

    def verificar_fyc(self, foc):
        if 0 <= foc <= 8:
            return True
        else:
            return False

    def estado_juego(self):
        if self.Su.gano() is True:
            return True
        return False


juego = Interfaz()
while juego.estado_juego() is not True:
    juego.jugar()
