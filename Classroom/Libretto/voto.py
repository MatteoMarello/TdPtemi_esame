import operator
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

    def copy(self):
        return Voto(self.esame, self.cfu, self.punteggio, self.lode, self.data)

    def __str__(self):
        return f'{self.esame} ({self.cfu} CFU): voto {self.str_punteggio()} in {self.data}'

def estrai_campo_esame(v):
    return v.esame

class Libretto:
    def __init__(self):
        self._voti = []
        # Con ._ prima dell'attributo lo rendo "privato" anche se rimane comunque accessibile.
        # Viene usata questa notazione per proteggere degli attributi che preferisco non vengano modificati dall'esterno.

    def append(self, voto):
        if self.has_voto(voto) == False and self.has_conflitto(voto) == False:
            self._voti.append(voto)
        else:
            raise ValueError("Voto non valido")

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

    def copy(self):
        nuovo = Libretto()
        for v in self._voti:
            nuovo._voti.append(v.copy())

        return nuovo

    def crea_migliorato(self):
        """
        Crea una copia del libretto e migliora i voti in esso presenti.
        :return: Oggetto Libretto migliorato
        """
        nuovo = Libretto()
        # nuovo._voti = self._voti.copy() # self._voti è una lista. Col metodo .copy() copio la lista dei voti per il mio nuovo libretto, tale e quale.
        # Con .copy() copio la list dei voti del libretto non migliorato. Però è una lista di riferimenti agli oggetti voto esistenti,
        # Quindi se poi modifico i voti del libretto migliorato, verranno modificati in automatico anche i voti del libretto non migliorato
        # (perchè sto agendo sui riferimenti agli stessi oggetti Voto). Quindi quello che devo fare è creare dei nuovi oggetti Voto, uguali a quelli del libretto standard.
        for v in self._voti:
            nuovo._voti.append(v.copy())

        for v in nuovo._voti:
            if 18 <= v.punteggio <= 23:
                v.punteggio += 1
            elif 24 <= v.punteggio <= 28:
                v.punteggio += 2
            elif v.punteggio == 29:
                v.punteggio = 30

        return nuovo

    def crea_ordinato_per_esame(self):
        nuovo = self.copy()
        nuovo.ordina_per_esame() # Chiamo il metodo ordina_per_esame che modifica la mia copia della lista dei voti, ordinandoli per esame.
        return nuovo

    def ordina_per_esame(self):
        # Ordina self._voti per nome esame
        # Se voglio ordinare una lista di oggetti utilizzando il metodo .sort() oppure .sorted(), dovrò prima definire il metodo
        # __lt__ all'interno della classe Voto che specifica come andranno confrontati gli oggetti Voto quando viene riordinata la lista.
        # Altrimenti posso usare il parametro key = operator.attrgetter(), e come parametro al metodo attrgetter passo l'attributo sul quale
        # voglio confrontare gli oggetti della struttura dati che sto ordinando! In questo caso passo 'esame', dato che voglio ordinare
        # gli oggetti Voto nella lista _voti in funzione del nome dell'esame
        self._voti.sort(key=operator.attrgetter('esame'))

    def crea_ordinato_per_punteggio(self):
        nuovo = self.copy()
        self._voti.sort(key=lambda v: (v.punteggio, v.lode), reverse=True) # Metto reverse=True perchè voglio l'ordinamento decrescente
        return nuovo




    def stampa(self):
        print(f'Hai {len(self._voti)} voti')
        for v in self._voti:
            print(v)
        print(f'La media vale: {self.media()}')


    def stampaGUI(self):
        outList = []
        outList.append(f'Hai {len(self._voti)} voti')
        for v in self._voti:
            outList.append(v)
        outList.append(f'La media vale: {self.media()}')
        return outList

    def cancella_inferiori_a_punteggio(self, punteggio):
        """
        for v in self._voti:
            if v.punteggio < punteggio:
                self._voti.remove(v)
        for i in range(len(self._voti)):
            if self._voti[i] < punteggio:
                self._voti.pop(i)
        """
        # I metodi scritti sopra NON vanno bene! Perché non bisogna mai ciclare su una lista cancellandone gli elementi.
        # Conviene ragionare al contrario --> Creo una lista nuova in cui aggiungo SOLAMENTE gli elementi che NON devo
        # cancellare della lista di partenza!
        voti_nuovi=[]
        for v in self._voti:
            if v.punteggio >= punteggio:
                voti_nuovi.append(v)

        # La lista voti_nuovi avrei potuto scriverla in egual modo con la sola istruzione:
        # voti_nuovi = [v for v in self._voti if v.punteggio >= punteggio]
        # Posso fare questa cosa quando devo creare una lista a partire da un altra con un if di mezzo!

        self._voti = voti_nuovi