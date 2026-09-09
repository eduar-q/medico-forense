import unittest
from medico_forense import chequear_disco, chequear_ram, chequear_puertos

class TestMedicoForense(unittest.TestCase):

    def test_estructura_chequear_disco(self):
        # Verifica que la función devuelva exactamente 5 valores
        resultado = chequear_disco()
        self.assertEqual(len(resultado), 5)

    def test_estructura_chequear_ram(self):
        resultado = chequear_ram()
        self.assertEqual(len(resultado), 5)

    def test_estructura_chequear_puertos(self):
        resultado = chequear_puertos()
        self.assertEqual(len(resultado), 5)

if __name__ == '__main__':
    unittest.main()
