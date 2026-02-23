import unittest
from kalkulator.izrsavanje_operacije import IzrsavanjeOperacije
from kalkulator.file_writer import IWriter

# Create a stub implementation of IWriter
class StubWriter(IWriter):
    def __init__(self):
        self.saved_result = None
        self.saved_filename = None
    
    def spremi(self, rezultat, filename):
        self.saved_result = rezultat
        self.saved_filename = filename

class TestIzrsavanjeOperacije(unittest.TestCase):
    
    def setUp(self):
        # Use the stub writer instead of real FileWriter
        self.stub_writer = StubWriter()
        self.izrsavanje = IzrsavanjeOperacije(self.stub_writer)
    
    def test_izvrsi_operaciju_zbrajanje(self):
        # Test zbrajanje (operacija 1)
        rezultat = self.izrsavanje.izvrsi_operaciju_spremi(5, 3, 1)
        
        # Check the result value
        self.assertEqual(rezultat, 8)
        
        # Check if result was saved through the writer
        self.assertEqual(self.stub_writer.saved_result, 8)
        self.assertEqual(self.stub_writer.saved_filename, "spremi.txt")
    
    def test_izvrsi_operaciju_oduzimanje(self):
        # Test oduzimanje (operacija 2)
        rezultat = self.izrsavanje.izvrsi_operaciju_spremi(5, 3, 2)
        
        # Check the result value
        self.assertEqual(rezultat, 2)
        
        # Check if result was saved through the writer
        self.assertEqual(self.stub_writer.saved_result, 2)
        self.assertEqual(self.stub_writer.saved_filename, "spremi.txt")
    
    def test_izvrsi_operaciju_mnozenje(self):
        # Test množenje (operacija 3)
        rezultat = self.izrsavanje.izvrsi_operaciju_spremi(5, 3, 3)
        
        # Check the result value
        self.assertEqual(rezultat, 15)
        
        # Check if result was saved through the writer
        self.assertEqual(self.stub_writer.saved_result, 15)
        self.assertEqual(self.stub_writer.saved_filename, "spremi.txt")
    
    def test_izvrsi_operaciju_dijeljenje(self):
        # Test dijeljenje (operacija 4)
        rezultat = self.izrsavanje.izvrsi_operaciju_spremi(6, 3, 4)
        
        # Check the result value
        self.assertEqual(rezultat, 2)
        
        # Check if result was saved through the writer
        self.assertEqual(self.stub_writer.saved_result, 2)
        self.assertEqual(self.stub_writer.saved_filename, "spremi.txt")