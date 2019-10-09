import unittest
from Sudoku import Sudok


class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.juego = Sudok([
            '53xx7xxxx',
            '6xx195xxx',
            'x98xxxx6x',
            '8xxx6xxx3',
            '4xx8x3xx1',
            '7xxx2xxx6',
            'x6xxxx28x',
            'xxx419xx5',
            'xxxx8xx79'
        ])

    def test_fila_incorrecto(self):
        self.assertEqual("Ingrese otro numero", self.juego.insertar_numero('7'))

    def test_columna_incorrecto(self):
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('1'))
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('2'))
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('4'))
        self.assertEqual("Ingrese otro numero", self.juego.insertar_numero('7'))

    def test_bloque_incorrecto(self):
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('1'))
        self.assertEqual("Ingrese otro numero", self.juego.insertar_numero('9'))

    def test_llenar_prox_bloque_fila_incorrecta(self):
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('1'))
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('7'))
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('4'))
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('2'))
        self.assertEqual("Ingrese otro numero", self.juego.insertar_numero('5'))

    def test_llenar_prox_bloque_columna_incorrecta(self):
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('1'))
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('7'))
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('4'))
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('2'))
        self.assertEqual("Ingrese otro numero", self.juego.insertar_numero('8'))

    def test_llenar_prox_bloque_bloque_incorrecta(self):
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('1'))
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('7'))
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('4'))
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('2'))
        self.assertEqual("Ingrese otro numero", self.juego.insertar_numero('9'))

    def test_llenar_prox_bloque_correcto(self):
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('1'))
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('7'))
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('4'))
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('2'))
        self.assertEqual("Numero ingresado", self.juego.insertar_numero('2'))


class TestSudokuCompletado(unittest.TestCase):

    def setUp(self):
        self.juego = Sudok([
            '531171111',
            '611195111',
            '198111161',
            '811161113',
            '411813111',
            '711121116',
            '161111281',
            '111419115',
            '11118117x'
        ])

    # cambiar n1 = 6 n2 = 9 n3 = 6 n4 = 9 para que tome el ultimo bloque

    def test_fila_incorrecto(self):
        self.juego.n1 = 6
        self.juego.n2 = 9
        self.juego.n3 = 6
        self.juego.n4 = 9
        self.assertEqual('Sudoku completado', self.juego.insertar_numero('9'))


if __name__ == "__main__":
    unittest.main()
