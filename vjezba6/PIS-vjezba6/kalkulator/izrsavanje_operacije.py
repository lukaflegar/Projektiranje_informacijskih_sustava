from kalkulator.file_writer import IWriter
from kalkulator.matematicke_operacije import MatematickeOperacije

class IzrsavanjeOperacije:
    def __init__(self, writer: IWriter):
        self.writer = writer

    def izvrsi_operaciju_spremi(self, operand1, operand2, izbor):
        operacije = MatematickeOperacije()
        rezultat = 0

        if izbor == 1:
            rezultat = operacije.zbroji(operand1, operand2)
        elif izbor == 2:
            rezultat = operacije.oduzmi(operand1, operand2)
        elif izbor == 3:
            rezultat = operacije.mnozi(operand1, operand2)
        elif izbor == 4:
            rezultat = operacije.dijeli(operand1, operand2)

        self.writer.spremi(rezultat, "spremi.txt")
        return rezultat
