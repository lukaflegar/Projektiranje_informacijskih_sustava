import unittest
from kalkulator.matematicke_operacije import MatematickeOperacije

class TestMatematickeOperacije(unittest.TestCase):

    def setUp(self):
        self.op = MatematickeOperacije()

    def test_zbroji_dva_broja_vraca_tocan_rezultat(self):
        self.assertEqual(self.op.zbroji(2, 3), 5)
        
    def test_oduzmi_dva_broja_vraca_tocan_rezultat(self):
        self.assertEqual(self.op.oduzmi(5, 3), 2)
        
    def test_mnozi_dva_broja_vraca_tocan_rezultat(self):
        self.assertEqual(self.op.mnozi(2, 3), 6)
        
    def test_dijeli_dva_broja_vraca_tocan_rezultat(self):
        self.assertEqual(self.op.dijeli(6, 3), 2)
        
    def test_dijeli_s_nulom_podize_exception(self):
        with self.assertRaises(ValueError) as context:
            self.op.dijeli(5, 0)
        self.assertIn("Dijeljenje s nulom nije dozvoljeno.", str(context.exception))