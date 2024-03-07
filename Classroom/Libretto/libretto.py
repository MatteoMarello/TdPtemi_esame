"""
Scrivere un programma Python che permetta di gestire un libretto universitario.
Il programma dovrà definire una classe Voto, che rappresenta un singolo esame superato,
ed una classe Libretto, che contiene l'elenco dei voti di uno studente.
"""

class Voto:
    def __init__(self, esame, cfu, punteggio, lode, data):
        # N.B: GLI ATTRIBUTI IN PYTHON SONO SEMPRE PUBBLICI ! MAI PRIVATE!
        # Quindi posso sempre accedere agli attributi di una classe, anche in classi diverse!
        self.esame = esame
        self.cfu = cfu
        self.punteggio = punteggio
        self.lode = lode
        self.data = data

        if self.lode and self.punteggio != 30:
            raise ValueError("Lode non applicabile")
            # raise è l'equivalente Python di throw per generare le eccezioni!

    def __str__(self): # il metodo __str__() è equivalente al metodo toString() di java!
        return f"Esame {self.esame} superato con {self.punteggio}"

    def __repr__(self):
        return f"Voto: ('{self.esame}', {self.cfu}, {self.punteggio}, {self.lode}, '{self.data})"


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


voto_1 = Voto("Analisi Matematica 1", 10, 28, False, '2022-02-10')
# Chiamare la classe in questo modo, con Voto e basta (senza new, come in Java), chiama automaticamente il metodo __init__
# di quella classe, che serve a definire gli attributi dell'oggetto in questione.

voto_2 = Voto("Basi di dati", 8, 30, True, '2023-06-15')

print(voto_1) # In questo modo il print mi stampa il riferimento all'oggetto... non le informazioni sull'oggetto!

print(voto_1.__str__()) # Chiamo il metodo "stampa()", definito nella classe Voto per stampare le informazioni sul voto di un esame.
# N.B: Se definisco il metodo __str__, allora posso anche evitare di chiamare il metodo sull'oggetto che sto stampando...
# basta scrivere print(nome_oggetto) e viene automaticamente stampata la stringa restituita dal metodo __str__()!

miei_voti = (voto_1, voto_2)
print(miei_voti) # Quando faccio print(miei_voti), viene automaticamente chiamato il metodo __repr__() sui voti, quindi con print
                 # stampo le stringhe che mi vengono restituite da repr!

mio_libretto = Libretto()
mio_libretto.append(voto_1)
mio_libretto.append(voto_2)

print(f'La tua media è: {mio_libretto.media()}')
