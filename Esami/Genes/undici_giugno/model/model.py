import copy

import networkx as nx

from Esami.Genes.undici_giugno.database.DAO import DAO

class Model:
    def __init__(self):
        self._cromosomi = DAO.getCromosomi()
        self._cromosomi.sort()
        self._graph = nx.DiGraph()
        self._bestPath = []
        self._bestLenght = 0

    def buildGraph(self):
        self._graph.clear()
        self._graph.add_nodes_from(self._cromosomi)
        edges = DAO.getEdges()
        self._graph.add_edges_from(edges)
        for e in edges:
            c1 = e[0]
            c2 = e[1]
            peso = DAO.getEdgeWeight(c1,c2)
            self._graph[c1][c2]["weight"] = peso

    def getConfrontoSoglia(self, soglia):
        edges = list(self._graph.edges(data=True))
        pesoMin = 0
        pesoMagg = 0
        for e in edges:
            if e[2]["weight"] > soglia:
                pesoMagg += 1
            elif e[2]["weight"] < soglia:
                pesoMin += 1

        return pesoMagg, pesoMin

    def getArchiEstremi(self):
        edges = list(self._graph.edges(data=True))
        edges.sort(key=lambda x: x[2]["weight"], reverse=True)
        return edges[0], edges[-1]


    def getBestPath(self, soglia):
        self._bestPath = []
        self._bestLenght = 0
        parziale = []
        edges = set()
        for c in self._graph.nodes:
            parziale.append(c)
            self._ricorsione(parziale, soglia, edges)
            parziale.pop()

        res = []
        for i in range(0, len(self._bestPath)-1):
            peso = self._graph[self._bestPath[i]][self._bestPath[i+1]]
            res.append((self._bestPath[i], self._bestPath[i+1], peso))

        return res, self._bestLenght

    def _ricorsione(self, parziale, soglia, edges):
        lunghezzaPerc = self._calcolaLunghezza(parziale)
        if lunghezzaPerc > self._bestLenght:
            self._bestLenght = lunghezzaPerc
            self._bestPath = copy.deepcopy(parziale)

        lastNode = parziale[-1]
        for neighbor in self._graph.neighbors(lastNode):
            if (lastNode, neighbor) not in edges and self._graph[lastNode][neighbor]["weight"] > soglia:
                parziale.append(neighbor)
                edges.add((lastNode, neighbor))
                self._ricorsione(parziale, soglia, edges)
                parziale.pop()
                edges.remove((lastNode, neighbor))

    def _calcolaLunghezza(self, listOfChromo):
        tot = 0
        for i in range(0, len(listOfChromo)-1):
            tot += self._graph[listOfChromo[i]][listOfChromo[i+1]]["weight"]
        return tot
    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)
