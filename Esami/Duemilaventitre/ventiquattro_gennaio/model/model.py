import copy

import networkx as nx

from Esami.Duemilaventitre.ventiquattro_gennaio.database.DAO import DAO
class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._products = DAO.getAllProducts()
        self._idMap = {p.Product_number : p for p in self._products}
        self._bestPath = []


    def buildGraph(self, anno, metodo, s):
        self._graph.clear()
        nodes = DAO.getNodes(anno, metodo, self._idMap)
        nodes.sort(key=lambda p: p.Product)
        self._graph.add_nodes_from(nodes)

        for n in self._graph.nodes:
            for n2 in self._graph.nodes:
                if n2.ricaviTotali > (n.ricaviTotali + s*n.ricaviTotali):
                    self._graph.add_edge(n, n2)


    def getProdottiRedditizi(self):
        listWPredecessors = []
        for n in self._graph.nodes:
            listWPredecessors.append((n, len(list(self._graph.predecessors(n))), len(list(self._graph.successors(n)))))

        listWPredecessors = [p for p in listWPredecessors if p[2] == 0]
        listWPredecessors.sort(key=lambda x: x[1], reverse=True)

        return listWPredecessors[0:5]


    def getPercorso(self):
        self._bestPath = []
        setNodesWithNoPredecessors = set([p for p in self._graph.nodes if len(list(self._graph.predecessors(p))) == 0])
        setNodesWithNoSuccesors = set([p for p in self._graph.nodes if len(list(self._graph.successors(p))) == 0])
        parziale = []

        for p in setNodesWithNoPredecessors:
            parziale.append(p)
            self._ricorsione(setNodesWithNoSuccesors, parziale)
            parziale.pop()

        return self._bestPath


    def _ricorsione(self, setNodesWithNoSuccesors, parziale):

        if parziale[-1] in setNodesWithNoSuccesors:
            if len(parziale) > len(self._bestPath):
                self._bestPath = copy.deepcopy(parziale)
            return

        lastNode = parziale[-1]

        for neighbor in self._graph.neighbors(lastNode):
            if neighbor not in parziale:
                parziale.append(neighbor)
                self._ricorsione(setNodesWithNoSuccesors, parziale)
                parziale.pop()





    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getMethods(self):
        return DAO.getMethods()