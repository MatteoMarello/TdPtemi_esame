import copy

import networkx as nx
from Classroom.iTunes.database.DAO import DAO

class Model:
    def __init__(self):
        self.graph = nx.Graph()
        self._idMap = {}
        self._bestSet = None
        self._bestScore = 0

    def getSetAlbum(self, a1, dTOT):
        self._bestSet = None
        self._bestScore = 0
        connessa = nx.node_connected_component(self.graph, a1)
        parziale = set()
        parziale.add(a1)
        connessa.remove(a1)
        self._ricorsione(parziale, connessa, dTOT)

        return self._bestSet, self.durataTot(self._bestSet)

    def _ricorsione(self, parziale, connessa, dTOT):
        # Verifico se parziale è una soluzione ammissibile
        if self.durataTot(parziale) > dTOT:
            return

        # Verifico se parziale è migliore del best
        if len(parziale) > self._bestScore:
            self._bestScore = len(parziale)
            self._bestSet = copy.deepcopy(parziale)

        # Ciclo su nodi aggiungibili -- ricorsione
        for c in connessa:
            if c not in parziale:
                parziale.add(c)
                self._ricorsione(parziale, connessa, dTOT)
                parziale.remove(c)

    def durataTot(self, setOfNodes):
        dtot = 0
        for n in setOfNodes:
            dtot += n.totD
        return toMinutes(dtot)

    def buildGraph(self, d):
        self.graph.clear()
        self.graph.add_nodes_from(DAO.getAlbums(toMillisec(d)))
        self._idMap = {a.AlbumId : a for a in self.graph.nodes}
        edges = DAO.getEdges(self._idMap)
        self.graph.add_edges_from(edges)


    def getConnessaDetails(self, v0):
        conn = nx.node_connected_component(self.graph, v0)
        durataTOT = 0
        for album in conn:
            durataTOT += toMinutes(album.totD)

        return len(conn), durataTOT

    def getGraphSize(self):
        return len(self.graph.nodes), len(self.graph.edges)

    def getNodes(self):
        return list(self.graph.nodes)

def toMillisec(d):
    return d*60*1000

def toMinutes(d):
    return d/1000/60

if __name__ == "__main__":
    mymodel = Model()
    mymodel.buildGraph(60*60*1000)
    print(mymodel.getGraphSize())


