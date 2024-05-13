import networkx as nx
from Classroom.ArtsMia.database.DAO import DAO

class Model:
    def __init__(self):
        self._artObjectList = DAO.getAllObjects()
        self._grafo = nx.Graph()
        self._grafo.add_nodes_from(self._artObjectList)
        self._idMap = {}
        for v in self._artObjectList:
            self._idMap[v.object_id] = v

    def creaGrafo(self):
        self.addEdges()

    def addEdges(self):
        # Soluzione 1: ciclare sui nodi -- da usare solo se ho pochi nodi e la query per ottenere gli archi è complicata!
        """
        for u in self._artObjectList:
            for v in self._artObjectList:
                peso = DAO.getPeso(u, v)
                self._grafo.add_edge(u, v, weight = peso)
        """

        # Soluzione 2 - una singola query in cui ottengo tutti gli archi. Da usare se la query non è troppo complicata e ci sono tanti nodi.
        allEdges = DAO.getAllConnessioni(self._idMap)
        for edge in allEdges:
            self._grafo.add_edge(edge.v1, edge.v2, weight=edge.peso)


    def checkExistence(self, id):
        if id in self._idMap:
            return True
        return False


    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)


if __name__ == "__main__":
    model = Model()
    model.creaGrafo()
    numNodes = model.getNumNodes()
    numEdges = model.getNumEdges()
    print(numNodes)
    print(numEdges)