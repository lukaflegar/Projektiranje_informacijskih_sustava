class MatematickeOperacije:
    def zbroji(self, operand1, operand2):
        return operand1 + operand2

    def oduzmi(self, operand1, operand2):
        return operand1 - operand2

    def mnozi(self, operand1, operand2):
        return operand1 * operand2

    def dijeli(self, operand1, operand2):
        if operand2 == 0:
            raise ValueError("Dijeljenje s nulom nije dozvoljeno.")
        return operand1 / operand2
