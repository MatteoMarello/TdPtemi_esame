import dataclasses

@dataclasses.dataclass
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: int
    studenti: list = None

    def __eq__(self, other):
        return self.codins == other.codins

    def __hash__(self):
        return hash(self.codins)

    def __str__(self):
        return self.nome + " ("+self.codins+")"
