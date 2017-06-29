import texto
import unittest


class test_convertirTextoABts(unittest.TestCase):
    def test_funcionConvierteTextoABinario(self):
        texto = "hola"
        self.assertEqual(texto.convertirTextoAbytes(texto), 1101000110111111011001100001)

    def test_funcionDevuelveBytes(self):
        texto = "hola"
        self.assertIsInstance(texto.convertirTextoAbytes(texto), bytes)


