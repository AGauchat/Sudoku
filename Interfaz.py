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
            if self.verificar_fyc(f) is True:
                print("Ingrese columna donde desea poner el numero (0 a 8)")
                c = int(input(">>"))
                if self.verificar_fyc(c) is True:
                    print("Ingrese numero")
                    n = int(input(">>"))
                    if self.verificar_num(n) is True:
                        print(self.Su.insertar_numero(n, f, c))
                    else:
                        print('Ingrese un numero correcto')
                else:
                    print('Ingrese un numero correcto')
            else:
                print('Ingrese un numero correcto')
        except:
            print('Ingrese un numero correcto')

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


# juego = Interfaz()
# while juego.estado_juego() is not True:
#     juego.jugar()
