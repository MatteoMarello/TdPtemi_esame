from voto import Libretto, Voto

# import voto esegue il file voto.py
# da questo momento in poi potrò utilizzare nel main le classi, funzioni, variabili ecc. definite all'interno del modulo voto.py!

# Prima di creare un oggetto di tipo voto usando la classe voto e il suo metodo __init__,
# devo scrivere il nome del modulo importato da cui sto prendendo quel metodo.
# Dato che il modulo importato si chiama voto, dovrò scrivere voto.Voto per chiamare il metodo __init__ della classe Voto!

lib = Libretto()
v1 = Voto("Analisi I", 10, 28, False, '2022-01-30')
lib.append(v1) # Aggiungo il voto al libretto!

lib.append(Voto("Fisica I", 10, 25, False, '2022-07-12'))
lib.append(Voto("Analisi II", 8, 30, True, '2023-02-15'))

voti25 = lib.findByPunti(25, False)
for v in voti25:
    print(v.esame)

voto_analisi2 = lib.findByEsame("Analisi II")
if voto_analisi2 is None:
    print("Nessun voto trovato!")
else:
    print(f'Hai preso {voto_analisi2.str_punteggio()}')

# Con try - except gestisco l'eccezione che può essere generata dal metodo findByEsame2 nel caso in cui non dovesse
# trovare un voto dell'esame passato in input!
# Se l'istruzione del try genera un eccezione vado nell'except -- e il codice all'interno del blocco try non viene runnato.
# Altrimenti, se non genera l'eccezione, l'except viene ignorato e viene runnato il codice nel try.
try:
    voto_analisi2 = lib.findByEsame2("Analisi III")
    # In questo caso il programma, poichè non ho controllato il risultato, e il metodo genera un'eccezione, quest'eccezione
    # non viene gestita dal mio programma chiamante e Python interrompe l'esecuzione!
except ValueError:
    print("Nessun voto trovato!")



nuovo_voto = Voto("Fisica I", 10, 25, False, '2022-07-13')
nuovo_voto2 = Voto("Fisica II", 10, 25, False, '2022-07-13')
print("1)", lib.has_voto(nuovo_voto))
print("2)", lib.has_voto(nuovo_voto2))

