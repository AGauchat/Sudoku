import unittest
from Sudoku import Sudoku_inicio


class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.juego = Sudoku_inicio([
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

    def test_ingresar_numero_correcto(self):
        



if __name__ == "__main__":
    unittest.main()