from abc import ABC, abstractmethod

class IWriter(ABC):
    @abstractmethod
    def spremi(self, rezultat, filename):
        pass

class FileWriter(IWriter):
    def spremi(self, rezultat, filename):
        with open(filename, 'w') as f:
            f.write(str(rezultat))
