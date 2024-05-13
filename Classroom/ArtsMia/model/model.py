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


    def getConnessa(self, v0int):
        # Modo 1: verifichiamo i successori di v0 con un algoritmo DFS
        v0 = self._idMap[v0int]
        successors = nx.dfs_successors(self._grafo, v0)
        allSucc = []
        for v in successors.values():
            allSucc.extend(v)
            # se aggiungo una lista con .extend(), aggiungo i singoli elementi della lista che riceve in input alla lista su cui chiamo il metodo.

        print(f'Metodo 1 (successors): {len(allSucc)}')

        # Modo 2: verifichiamo i predecessori di v0 con un algoritmo DFS.
        # Essendo che il grafo non è orientato, verificare successori e predecessori è la stessa cosa.

        predecessors = nx.dfs_predecessors(self._grafo, v0)
        print(f'Metodo 1 (predecessors): {len(predecessors.values())}')

        # Modo 3: recupero direttamente l'albero di visita del DFS, e conto i nodi di questo albero
        tree: nx.DiGraph = nx.dfs_tree(self._grafo, v0)
        print(f'Metodo 3 (tree): {len(tree.nodes)}')

        # N.B: .predecessors() mi restituisce un dizionario in cui le chiavi sono i nodi e i valori sono i nodi predecessori
        # .successors() invece mi restituisce un dizionario in cui le chiavi sono i nodi e i valori sono liste contenenti tutti i nodi successori
        # Questo perchè in un ALBERO (componente connessa), un nodo può avere più successori, ma avrà sempre un solo predecessore.

        # Modo 4: uso direttamente il metodo node_connected_component(n), che mi genera in automatico la componente connessa che contiene il nodo n passato in input.
        connComp = nx.node_connected_component(self._grafo, v0)
        print(f'Metodo 4 (connected component): {len(connComp)}')

        return len(connComp)


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
    model.getConnessa(1234)