"""
Scrivere un programma Python che permetta di gestire un libretto universitario.
Il programma dovrà definire una classe Voto, che rappresenta un singolo esame superato,
ed una classe Libretto, che contiene l'elenco dei voti di uno studente.
"""

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
