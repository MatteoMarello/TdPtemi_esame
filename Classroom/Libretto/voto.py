from dataclasses import dataclass
@dataclass
class Voto:
    esame: str
    cfu: int
    punteggio: int
    lode: bool
    data: str

    def str_punteggio(self):
        """
        Costruisce la stringa che rappresenta in forma leggibile il punteggio,
        tenendo conto della possibilità di lode
        :return: "30 e lode" oppure il punteggio senza lode, sotto forma di stringa.
        """
        if self.punteggio == 30 and self.lode == True:
            return "30 e lode"
        else:
            return str(self.punteggio)

class Libretto:
    def __init__(self):
        self._voti = []
        # Con ._ prima dell'attributo lo rendo "privato" anche se rimane comunque accessibile.
        # Viene usata questa notazione per proteggere degli attributi che preferisco non vengano modificati dall'esterno.

    def append(self, voto):
        self._voti.append(voto)

    def media(self):
        if len(self._voti) == 0:
            raise ValueError("Elenco voti vuoto")
        else:
            punteggi = [v.punteggio for v in self._voti]
            # Con l'istruzione sopra mi costruisco direttamente una lista dei punteggi di tutti i voti:
            # Itero sui voti (for v in self.voti) e costruisco la lista dei punteggi (v.punteggio).
            return sum(punteggi)/len(punteggi)

    def findByPunti(self, punteggio, lode):
        """
        Seleziona i soli voti che hanno un punteggio definito.
        :param punteggio: Numero intero che rappresenta il punteggio
        :param lode: Booleano che indica la presenza della lode
        :return: Lista di oggetti di tipo Voto che hanno il punteggio specificato (può anche essere vuota)
        """
        # Con la cosa fatta sopra (che avrò mettendo le triple virgolette subito dopo il nome del metodo) potrò scrivere la documentazione
        # del metodo, che serve per chi chiama il metodo --> gli viene specificato a cosa serve il metodo, cosa sono i parametri in input e cosa ritorna in output.
        corsi = []
        for voto in self._voti:
            if voto.punteggio == punteggio and voto.lode == lode:
                corsi.append(voto)
        return corsi

    def findByEsame(self, esame):
        """
        Ritorna un oggetto di tipo Voto dato il nome dell'esame.
        :param esame: Nome dell'esame di cui sto cercando il punteggio
        :return: Oggetto Voto, se esiste. Altrimenti None.
        """
        for v in self._voti:
            if v.esame == esame:
                return v
        return None

    def findByEsame2(self, esame):
        """
        Ritorna un oggetto di tipo Voto dato il nome dell'esame.
        :param esame: Nome dell'esame di cui sto cercando il punteggio
        :return: Oggetto Voto, se esiste. Altrimenti genera un'eccezione che non fa andare avanti il programma.
        """
        # Questa versione del metodo è molto meglio perchè gestisco in modo migliore il caso in cui l'oggetto Voto con esame
        # passato in input non venisse trovato, perchè non restituirò None ma genererò un eccezione che bloccherà il mio programma.
        for v in self._voti:
            if v.esame == esame:
                return v
        raise ValueError(f"Esame {esame} non presente nel libretto")




    def has_voto(self, voto):
        """
        Ricerca se nel libretto esiste già un esame con lo stesso nome e lo stesso punteggio
        :param voto: Oggetto voto da confrontare
        :return: True se esiste, False altrimenti
        """
        for v in self._voti:
            if v.esame == voto.esame and v.punteggio == voto.punteggio and v.lode == voto.lode:
                return True
        return False

    def has_conflitto(self, voto):
        """
        Ricerca se nel libretto esiste già un esame con lo stesso nome ma punteggio diverso
        :param voto: Oggetto voto da confrontare
        :return: True se esiste, False altrimenti
        """
        for v in self._voti:
            if v.esame == voto.esame and not (v.punteggio == voto.punteggio and v.lode == voto.lode):
                return True
        return False
