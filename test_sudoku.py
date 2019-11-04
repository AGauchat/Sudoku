import unittest
from parameterized import parameterized
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

#TEST FUNCIONES

    @parameterized.expand([
        ('6', 0, 6),
        ('5', 8, 6),
        ('4', 8, 5),
        ('3', 5, 3),
        ('1', 5, 7)])
    def test_verif_bloque_mal(self, num, fila, columna):
        self.assertFalse(self.juego.verificar_bloque(num, fila, columna))

    @parameterized.expand([
        ('7', 0, 2),
        ('8', 3, 1),
        ('9', 8, 3),
        ('2', 5, 7),
        ('6', 6, 3)])
    def test_fila_incorrecto(self, num, fila, columna):
        self.assertFalse(self.juego.verificar_fila_columna(fila, columna, num))

    @parameterized.expand([
        ('8', 0, 2),
        ('6', 3, 1),
        ('1', 8, 3),
        ('7', 5, 7),
        ('1', 6, 3)])
    def test_columna_incorrecto(self, num, fila, columna):
        self.assertFalse(self.juego.verificar_fila_columna(fila, columna, num))

    @parameterized.expand([
        (3, 4),
        (3, 8),
        (4, 0),
        (4, 3),
        (4, 5)])
    def test_pos_incorrecta(self, fila, columna):
        self.assertFalse(self.juego.verificar_x(fila, columna))

    def test_nogana(self):
        self.assertFalse(self.juego.gano())

    @parameterized.expand([
        ('2', 0, 2),
        ('3', 0, 6),
        ('1', 8, 0),
        ('1', 8, 6),
        ('5', 3, 1)])
    def test_verif_bloque_bien(self, num, fila, columna):
        self.assertTrue(self.juego.verificar_bloque(num, fila, columna))
    
    @parameterized.expand([
        ('1', 0, 2),
        ('5', 3, 1),
        ('2', 8, 3),
        ('1', 5, 7),
        ('3', 6, 3)])
    def test_filaycolumna_correcto(self, num, fila, columna):
        self.assertTrue(self.juego.verificar_fila_columna(fila, columna, num))

#TEST DE INGRESO DE NUMERO

    @parameterized.expand([
        ('7', 0, 2),
        ('8', 3, 1),
        ('9', 8, 3),
        ('2', 5, 7),
        ('6', 6, 3)])
    def test_fila_incorrecto(self, num, fila, columna):
        self.assertEqual(self.juego.insertar_numero(num, fila, columna), "-- El numero se repite en la fila o en la columna --")

        self.assertEqual(self.juego.tablero, [
            ['5', '3', 'x', 'x', '7', 'x', 'x', 'x', 'x'],
            ['6', 'x', 'x', '1', '9', '5', 'x', 'x', 'x'],
            ['x', '9', '8', 'x', 'x', 'x', 'x', '6', 'x'],
            ['8', 'x', 'x', 'x', '6', 'x', 'x', 'x', '3'],
            ['4', 'x', 'x', '8', 'x', '3', 'x', 'x', '1'],
            ['7', 'x', 'x', 'x', '2', 'x', 'x', 'x', '6'],
            ['x', '6', 'x', 'x', 'x', 'x', '2', '8', 'x'],
            ['x', 'x', 'x', '4', '1', '9', 'x', 'x', '5'],
            ['x', 'x', 'x', 'x', '8', 'x', 'x', '7', '9']])

        self.assertEqual(False, self.juego.gano())

    @parameterized.expand([
        ('8', 0, 2),
        ('6', 3, 1),
        ('1', 8, 3),
        ('7', 5, 7),
        ('1', 6, 3)])
    def test_columna_incorrecto(self, num, fila, columna):
        self.assertEqual(self.juego.insertar_numero(num, fila, columna), "-- El numero se repite en la fila o en la columna --")

        self.assertEqual(self.juego.tablero, [
            ['5', '3', 'x', 'x', '7', 'x', 'x', 'x', 'x'],
            ['6', 'x', 'x', '1', '9', '5', 'x', 'x', 'x'],
            ['x', '9', '8', 'x', 'x', 'x', 'x', '6', 'x'],
            ['8', 'x', 'x', 'x', '6', 'x', 'x', 'x', '3'],
            ['4', 'x', 'x', '8', 'x', '3', 'x', 'x', '1'],
            ['7', 'x', 'x', 'x', '2', 'x', 'x', 'x', '6'],
            ['x', '6', 'x', 'x', 'x', 'x', '2', '8', 'x'],
            ['x', 'x', 'x', '4', '1', '9', 'x', 'x', '5'],
            ['x', 'x', 'x', 'x', '8', 'x', 'x', '7', '9']])

        self.assertEqual(False, self.juego.gano())

    @parameterized.expand([
        ('6', 0, 6),
        ('5', 8, 6),
        ('4', 8, 5),
        ('3', 5, 3),
        ('1', 5, 7)])
    def test_bloque_incorrecto(self, num, fila, columna):
        self.assertEqual(self.juego.insertar_numero(num, fila, columna), "-- El numero se encuentra dentro del bloque --")

        self.assertEqual(self.juego.tablero, [
            ['5', '3', 'x', 'x', '7', 'x', 'x', 'x', 'x'],
            ['6', 'x', 'x', '1', '9', '5', 'x', 'x', 'x'],
            ['x', '9', '8', 'x', 'x', 'x', 'x', '6', 'x'],
            ['8', 'x', 'x', 'x', '6', 'x', 'x', 'x', '3'],
            ['4', 'x', 'x', '8', 'x', '3', 'x', 'x', '1'],
            ['7', 'x', 'x', 'x', '2', 'x', 'x', 'x', '6'],
            ['x', '6', 'x', 'x', 'x', 'x', '2', '8', 'x'],
            ['x', 'x', 'x', '4', '1', '9', 'x', 'x', '5'],
            ['x', 'x', 'x', 'x', '8', 'x', 'x', '7', '9']])

        self.assertEqual(False, self.juego.gano())

    @parameterized.expand([
        ('4', 3, 4),
        ('6', 3, 8),
        ('1', 4, 0),
        ('5', 4, 3),
        ('7', 4, 5)])
    def test_valor_fijo(self, num, fila, columna):
        self.assertEqual(self.juego.insertar_numero(num, fila, columna), "-- Esa posición es fija --")

        self.assertEqual(self.juego.tablero, [
            ['5', '3', 'x', 'x', '7', 'x', 'x', 'x', 'x'],
            ['6', 'x', 'x', '1', '9', '5', 'x', 'x', 'x'],
            ['x', '9', '8', 'x', 'x', 'x', 'x', '6', 'x'],
            ['8', 'x', 'x', 'x', '6', 'x', 'x', 'x', '3'],
            ['4', 'x', 'x', '8', 'x', '3', 'x', 'x', '1'],
            ['7', 'x', 'x', 'x', '2', 'x', 'x', 'x', '6'],
            ['x', '6', 'x', 'x', 'x', 'x', '2', '8', 'x'],
            ['x', 'x', 'x', '4', '1', '9', 'x', 'x', '5'],
            ['x', 'x', 'x', 'x', '8', 'x', 'x', '7', '9']])

        self.assertEqual(False, self.juego.gano())

    @parameterized.expand([
        ('2', 0, 2),
        ('4', 1, 1),
        ('1', 8, 2),
        ('3', 7, 7),
        ('4', 0, 8)])
    def test_numero_ingresado(self, num, fila, columna):
        self.assertEqual(self.juego.insertar_numero(num, fila, columna), "-- Numero ingresado --")

        self.assertEqual(False, self.juego.gano())

    def test_gano(self):
        self.juego = Sudok([
            '531171111',
            '611195111',
            '198111161',
            '811161113',
            '411813111',
            '711121116',
            '161111281',
            '111419115',
            '111181171'
        ])

        self.assertTrue(self.juego.gano())


if __name__ == "__main__":
    unittest.main()
