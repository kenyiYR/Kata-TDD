import unittest
from  logica import  
class TestCalculadoraPromedio(unittest.TestCase):
    def setUp(self):
        self.calculadora = CalculadoraPromedio()

    def test_promedio_arreglo_vacio(self):
        conjunto = []
        self.assertEqual(self.calculadora.calcular_promedio(conjunto), 0)

    def test_promedio_un_solo_numero(self):
        conjunto = [5]
        self.assertEqual(self.calculadora.calcular_promedio(conjunto), 5)

    def test_promedio_numeros_positivos(self):
        conjunto = [3, 5, 7, 9, 11]
        self.assertEqual(self.calculadora.calcular_promedio(conjunto), 7)

    def test_promedio_numeros_positivos_y_negativos(self):
        conjunto = [-2, 4, -6, 8]
        self.assertEqual(self.calculadora.calcular_promedio(conjunto), 1)

    def test_promedio_decimal(self):
        conjunto = [2, 3, 4, 5]
        self.assertEqual(self.calculadora.calcular_promedio(conjunto), 3.5)

if __name__ == '__main__':
    unittest.main()
