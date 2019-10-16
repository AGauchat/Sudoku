import unittest

from Interfaz import Interfaz


class Test_Interfaz_Sudoku(unittest.TestCase):

    def setUp(self):
        self.int = Interfaz()

    def test_filaocolumna_incorrecta(self):
        self.assertFalse(self.int.verificar_fyc(23))

    def test_filaocolumna_correcta(self):
        self.assertTrue(self.int.verificar_fyc(3))

    def test_numero_incorrecto(self):
        self.assertFalse(self.int.verificar_num(49))

    def test_numero_correcto(self):
        self.assertTrue(self.int.verificar_num(9))



if __name__ == "__main__":
    unittest.main()
