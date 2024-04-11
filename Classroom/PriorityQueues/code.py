import queue
class Coda_prioritaria:
    def __init__(self):
        self._lista = []

    def push(self, valore):
        self._lista.append(valore)

    def pop(self):
        """
        Restituisce il valore minimo presente nella lista e lo cancella dalla lista stessa
        :return:
        """
        "[2, 5, 1, 9]"
        "enumerate restituisce [(0,2), (1,5), (2,1), (3,9)] --> lista di tuple in cui il primo elemento rappresenta l'indice e il secondo l'elemento che si trova in quella posizione!"
        (pos_min, val_min) = min(enumerate(self._lista), key=lambda t: t[1]) # --> con key=lambda t: t[1] confronto le tuple, ma io voglio confrontare i valori in posizioni 1 delle tuple, e non gli indici. Per questo uso la lambda!
        self._lista.pop(pos_min)
        return val_min

c = Coda_prioritaria()
c.push(2)
c.push(5)
c.push(1)
print(c.pop())
c.push(3)
print(c.pop())
print(c.pop())
print(c.pop())
print()

c.push("Paolo")
c.push("Giulia")
c.push("Antonio")
c.push("Anna")
print(c.pop())
print(c.pop())
print(c.pop())
print(c.pop())

# Ho fatto tutto io... però sarebbe stato più efficiente utilizzare un oggetto PriorityQueue.
# c = queue.PriorityQueue() --> c è un oggetto della classe PriorityQueue.