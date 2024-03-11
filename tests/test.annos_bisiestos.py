import sys
from pathlib import Path
import unittest

# Agregamos el directorio padre al path para importar el módulo correctamente
root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(root_path))

# Importamos la función que queremos probar
from ejercicios.AnnosBisiestos import evaluar

class TestAnnosBisiestos(unittest.TestCase):
    def test_1988(self):
        valor_esperado = "1988 es bisiesto"
        valor_actual = evaluar(1988)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_2004(self):
        valor_esperado = "2004 es bisiesto"
        valor_actual = evaluar(2004)
        self.assertEqual(valor_esperado, valor_actual)

    def test_1960(self):
        valor_esperado = "1960 es bisiesto"
        valor_actual = evaluar(1960)
        self.assertEqual(valor_esperado, valor_actual)

    def test_2020(self):
        valor_esperado = "2020 es bisiesto"
        valor_actual = evaluar(2020)
        self.assertEqual(valor_esperado, valor_actual)

    def test_2100(self):
        valor_esperado = "2100 no es bisiesto"
        valor_actual = evaluar(2100)
        self.assertEqual(valor_esperado, valor_actual)

    def test_1999(self):
        valor_esperado = "1999 no es bisiesto"
        valor_actual = evaluar(1999)
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()