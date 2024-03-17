import voto
# import voto esegue il file voto.py
# da questo momento in poi potrò utilizzare nel main le classi, funzioni, variabili ecc. definite all'interno del modulo voto.py!

# Prima di creare un oggetto di tipo voto usando la classe voto e il suo metodo __init__,
# devo scrivere il nome del modulo importato da cui sto prendendo quel metodo.
# Dato che il modulo importato si chiama voto, dovrò scrivere voto.Voto per chiamare il metodo __init__ della classe Voto!
v1 = voto.Voto("Tecniche di Programmazione", 8, 28, False, '2024-03-11')
print(v1)