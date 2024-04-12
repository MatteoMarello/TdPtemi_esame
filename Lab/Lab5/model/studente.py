import dataclasses

@dataclasses.dataclass
class Studente:
    matricola: int
    nome: str
    cognome: str
    CDS: str
    corsi: list = None

    def __str__(self):
        return self.nome + ", " + self.cognome + " ("+str(self.matricola)+")"

    def __eq__(self, other):
        return self.matricola == other.matricola

    def __hash__(self):
        return hash(self.matricola)
