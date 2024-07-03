import copy

import networkx as nx

from Esami.Genes.trenta_giugno.database.DAO import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._localizzazioni = DAO.getLocalizzazioni()
        self._graph.add_nodes_from(self._localizzazioni)
        edges = DAO.getEdges()
        self._graph.add_edges_from(edges)
        for e in self._graph.edges:
            l1 = e[0]
            l2 = e[1]
            peso = DAO.getEdgeWeight(l1,l2)
            self._graph[l1][l2]["weight"] = peso

        self._bestPath = []
        self._bestLenght = 0

    def getStatistiche(self, loc):
        res = []
        for l in self._graph.neighbors(loc):
            res.append((l, self._graph[loc][l]["weight"]))
        res.sort(key=lambda x: x[1], reverse=True)
        return res


    def getBestPath(self, localita):
        self._bestPath = []
        self._bestLenght = 0
        parziale = [localita]
        self._ricorsione(parziale)

        return self._bestPath, self._bestLenght


    def _ricorsione(self, parziale):
        lunghezzaPercorso = self._calcolaLunghezzaPercorso(parziale)
        if lunghezzaPercorso > self._bestLenght:
            self._bestPath = copy.deepcopy(parziale)
            self._bestLenght = lunghezzaPercorso

        lastNode = parziale[-1]
        for neighbor in self._graph.neighbors(lastNode):
            if neighbor not in parziale:
                parziale.append(neighbor)
                self._ricorsione(parziale)
                parziale.pop()


    def _calcolaLunghezzaPercorso(self, listOfLocs):
        tot = 0
        for i in range(0, len(listOfLocs)-1):
            tot += self._graph[listOfLocs[i]][listOfLocs[i+1]]["weight"]

        return tot


    def getLocalizzazioni(self):
        return list(self._graph.nodes)
    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)
