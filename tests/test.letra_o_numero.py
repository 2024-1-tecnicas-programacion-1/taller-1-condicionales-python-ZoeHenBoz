import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(_file_).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.letra_o_numero import evaluar

class TestLetraONumero(unittest.TestCase):
    def test_es_numero(self):
        valor_esperado = "Es numero"
        valor_actual = evaluar('9')
        self.assertEqual(valor_esperado, valor_actual)

    # TODO: Agrega tus otros casos de prueba aquí

class TestSetDeTenis(unittest.TestCase):
    def test_es_leta_mayuscula(self):
        valor_esperado = "Es letra Mayuscula"
        valor_actual = evaluar('C')
        self.assertEqual(valor_esperado, valor_actual)

class TestSetDeTenis(unittest.TestCase):
    def test_es_leta_mayuscula(self):
        valor_esperado = "Es letra Minuscula"
        valor_actual = evaluar('f')
        self.assertEqual(valor_esperado, valor_actual)

class TestSetDeTenis(unittest.TestCase):
    def test_no_es_letra_ni_numero(self):
        valor_esperado = "No es letra ni número"
        valor_actual = evaluar('#')
        self.assertEqual(valor_esperado, valor_actual)


if _name_ == '_main_':
    unittest.main()