from Sudoku import Sudok
from Api import api


class Interfaz():

    def __init__(self):
        self.tablero = api()
        self.Su = Sudok(self.tablero)
        self.coord = ()

    def reglas(self):
        print("--REGLAS--")
        print("Llenaremos los espacios por bloques de 3x3, al terminar un bloque se podra pasar al siguiente")

    def jugar(self):
        print("Ingrese numero en el espacio vacio")
        self.coord = self.Su.verificar_espacio()
        self.Su.tablero[self.coord[0]][self.coord[1]] = " "
        for i in range(0, 9):
            for j in range(0, 9):
                print(self.Su.tablero[i][j], end=" ")
            print(" ")

        n = input(">>")
        self.ingresar_numero(n)

    def ingresar_numero(self, num):
        if self.Su.verificar_bloque(num) == None and self.Su.verificar_fila_columna(self.coord[0], self.coord[1], num) == None:
            self.Su.tablero[self.coord[0]][self.coord[1]] = num
            self.Su.verificar_x()

            print("Numero ingresado")
        else:
            print("Ingrese otro numero")

    def terminado(self):
        if self.coord == (8, 8) and self.Su.verificar_x() == 0:
            return True


juego = Interfaz()
t = juego.terminado()
juego.reglas()
while t != True:

    juego.jugar()
