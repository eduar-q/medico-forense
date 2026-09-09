import unittest
# 1. Importamos la nueva función
from medico_forense import chequear_disco, chequear_ram, chequear_puertos, chequear_ssh

class TestMedicoForense(unittest.TestCase):

    def test_estructura_chequear_disco(self):
        resultado = chequear_disco()
        self.assertEqual(len(resultado), 5)

    def test_estructura_chequear_ram(self):
        resultado = chequear_ram()
        self.assertEqual(len(resultado), 5)

    def test_estructura_chequear_puertos(self):
        resultado = chequear_puertos()
        self.assertEqual(len(resultado), 5)

    # 2. Agregamos la prueba para SSH
    def test_estructura_chequear_ssh(self):
        resultado = chequear_ssh()
        self.assertEqual(len(resultado), 5)

if __name__ == '__main__':
    unittest.main()
