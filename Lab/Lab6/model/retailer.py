from dataclasses import dataclass

@dataclass
class Retailer:
    codice: int
    nome: str
    tipo: str
    paese: str


    def __hash__(self):
        return hash(self.codice)

    def __eq__(self, other):
        return self.codice == other.codice

    def __str__(self):
        return f'{self.nome} ({self.codice})'