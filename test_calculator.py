import unittest
from calculator import sumar, restar, multiplicar, dividir


class TestCalculator(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(5, 3), 8)

    def test_sumar_negativos(self):
        self.assertEqual(sumar(-5, -3), -8)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)

    def test_restar_resultado_negativo(self):
        self.assertEqual(restar(3, 5), -2)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(5, 3), 15)

    def test_multiplicar_por_cero(self):
        self.assertEqual(multiplicar(5, 0), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_decimal(self):
        self.assertAlmostEqual(dividir(5, 2), 2.5)

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            dividir(5, 0)


if __name__ == "__main__":
    unittest.main()
