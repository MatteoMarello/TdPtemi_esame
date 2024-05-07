from Classroom.MetroParis.database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo = nx.DiGraph()
        self._idMap = {}
        for f in self._fermate:
            self._idMap[f.id_fermata] = f

    def buildGraph(self):
        self._grafo.add_nodes_from(self._fermate)

        # Modo 1 per aggiungere gli archi: doppio loop sui nodi e query per ogni coppia di nodi per vedere se c'è una linea che collega le due fermate.
        # Se ci sono tanti nodi come in questo caso, il doppio ciclo sui nodi NON va bene! Quindi bisogna pensare a un altro modo, eventualmente senza
        # doppio ciclo ma rendendo la query leggermente più complicata...
        """
        for u in self._fermate:
            for v in self._fermate:
                res = DAO.getEdge(u,v)
                if len(res) > 0:
                    self._grafo.add_edge(u, v)
                    print(f"Added edge between {u} and {v}")
        """

        # Modo 2 per aggiungere gli archi: rendo la query un po' più complicata, ma ciclo una sola volta sui nodi.
        # Ciclo sui nodi, mi prendo i vicini di ogni singolo nodo, e aggiungo gli archi tra il nodo e i suoi vicini.

        """
        for u in self._fermate:
            vicini = DAO.getEdgesVicini(u)
            for v in vicini:
                # -> vicini è una lista di connessioni. Mi devo prendere l'oggetto fermata v_nodo dalla _idMap, in cui
                # -> ho come chiavi gli id delle fermate e come valori gli oggetti Fermata corrispondenti a quell'id.
                v_nodo = self._idMap[v.id_stazA]
                self._grafo.add_edge(u, v_nodo)
                print(f"Added edge between {u} and {v_nodo}")
        """

        # Modo 3 per aggiungere gli archi: singola query che mi restituisce direttamente le connessioni e costruisco il grafo
        # -> senza effettuare alcun loop sulle fermate, ma solo sulle connessioni!
        # Leggo direttamente tutta la tabella delle connessioni e la gestisco nel model aggiungendo i diversi archi tra i nodi: lo posso fare perchè ho una lista con tutte le connessioni!

        all_connessioni = DAO.getAllConnessioni()
        for c in all_connessioni:
            u_nodo = self._idMap[c.id_stazP]
            v_nodo = self._idMap[c.id_stazA]
            self._grafo.add_edge(u_nodo, v_nodo)
            # print(f"Added edge between {u_nodo} and {v_nodo}")


    @property
    def fermate(self):
        return self._fermate

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)


if __name__ == "__main__":
    mymodel = Model()
    mymodel.buildGraph()
    print(f'The graph has {mymodel.getNumNodes()} nodes.')
    print(f'The graph has {mymodel.getNumEdges()} edges.')