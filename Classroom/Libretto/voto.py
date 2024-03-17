from dataclasses import dataclass
@dataclass
class Voto:
    esame: str
    cfu: int
    punteggio: int
    lode: bool
    data: str

class Libretto:
    def __init__(self):
        self._voti = []
        # Con ._ prima dell'attributo lo rendo "privato" anche se rimane comunque accessibile.
        # Viene usata questa notazione per proteggere degli attributi che preferisco non vengano modificati dall'esterno.

    def append(self, voto):
        self._voti.append(voto)

    def media(self):
        if (len(self._voti) == 0):
            raise ValueError("Elenco voti vuoto")
        else:
            punteggi = [v.punteggio for v in self._voti]
            # Con l'istruzione sopra mi costruisco direttamente una lista dei punteggi di tutti i voti:
            # Itero sui voti (for v in self.voti) e costruisco la lista dei punteggi (v.punteggio).
            return sum(punteggi)/len(punteggi)