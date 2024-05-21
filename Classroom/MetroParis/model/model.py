from Classroom.MetroParis.database.DAO import DAO
import networkx as nx
import geopy.distance

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo = nx.DiGraph()
        self._idMap = {}
        for f in self._fermate:
            self._idMap[f.id_fermata] = f
        self._linee = DAO.getAllLinee()
        self._lineaMap = {}
        for l in self._linee:
            self._lineaMap[l.id_linea] = l

    def buildGraph(self):
        self._grafo.clear()
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

    def buildGraphPesato(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._fermate)
        self.addEdgePesatiTempo()

    # Con il metodo sotto aggiungo gli archi pesati considerando come peso il numero di linee che collegano due stazioni
    def addEdgePesati(self):
        self._grafo.clear_edges()
        allConnessioni = DAO.getAllConnessioni()
        for c in allConnessioni:
            if self._grafo.has_edge(self._idMap[c.id_stazP], self._idMap[c.id_stazA]):
                # con il metodo sottostante verifico se c'è già un arco tra due nodi; in caso affermativo
                # aumento il peso dell'arco di 1.
                # con graph[u][v]["weight"] accedo all'attributo weight dell'arco presente tra i nodi u e v.
                self._grafo[self._idMap[c.id_stazP]][self._idMap[c.id_stazA]]["weight"] +=1
            else:
                # se l'arco non è ancora stato aggiunto, lo aggiungo e imposto l'attributo weight pari a 1.
                self._grafo.add_edge(self._idMap[c.id_stazP], self._idMap[c.id_stazA], weight = 1)

    # Con questo metodo aggiungo gli archi pesati considerando come peso il tempo che viene impiegato per andare da una stazione ad un'altra
    def addEdgePesatiTempo(self):
        self._grafo.clear_edges()
        allConnessioni = DAO.getAllConnessioni()
        for c in allConnessioni:
            v0 = self._idMap[c.id_stazP]
            v1 = self._idMap[c.id_stazA]
            linea = self._lineaMap[c.id_linea]
            peso = self.getTraversalTime(v0,v1,linea)

            if self._grafo.has_edge(v0, v1):
                if self._grafo[v0][v1]["weight"] > peso:
                    self._grafo[v0][v1]["weight"] = peso

            else:
                self._grafo.add_edge(v0,v1,weight=peso)


    def getTraversalTime(self, v0,v1,linea):
        vel = linea.velocita
        p0 = (v0.coordX, v0.coordY)
        p1 = (v1.coordX, v1.coordY)
        dist = geopy.distance.distance(p0, p1).km
        tempo = dist/vel * 60 # in minuti
        return tempo

    def getBestPath(self, v0, v1):
        costoTot, path = nx.single_source_dijkstra(self._grafo, source=v0, target=v1)
        return costoTot, path


    # Metodo per implementare un algoritmo di tipo BFS per visitare il nostro grafo
    def getBFSNodes(self, source):
        edges = nx.bfs_edges(self._grafo, source=source)
        visited = []
        # il risultato del metodo .bfs_edges è un generatore, su cui posso iterare per ottenere source e target del mio albero di visita!
        # se faccio for u, v in edges: u e v saranno i nodi source e target di ognuno di questi archi risultanti dal metodo .bfs_edges che ha generato l'albero di visita.
        for u, v in edges:
            # u: nodo source
            # v: nodo target
            # aggiungo alla lista dei nodi visitati tutti i nodi "target" degli archi del cammino minimo su cui sto iterando
            visited.append(v)
        return visited

    def getDFSNodes(self, source):
        edges = nx.dfs_edges(self._grafo, source)
        visited = []
        for u,v in edges:
            visited.append(v)
        return visited

    def getArchiPesoMaggiore(self):
        if len(self._grafo.edges) == 0:
            print("Il grafo è vuoto")
            return

        edges = self._grafo.edges
        result = []
        for u, v in edges:
            peso = self._grafo[u][v]["weight"]
            if peso > 1:
                result.append((u,v,peso))

        return result

    def getEdgeWeight(self, v1, v2):
        # questo metodo restituisce il peso dell'arco dati due nodi
        return self._grafo[v1][v2]["weight"]

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

