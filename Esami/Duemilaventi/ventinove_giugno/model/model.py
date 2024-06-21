import copy

import networkx as nx

from Esami.Duemilaventi.ventinove_giugno.database.DAO import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()


    def buildGraph(self, year):
        self._graph.clear()
        directors = DAO.getDirectors(year)
        self.idMap = {d.id: d for d in directors}
        self._graph.add_nodes_from(directors)
        edges = DAO.getEdges(year, self.idMap)
        self._graph.add_weighted_edges_from(edges)
        self._bestPath = []
        self._attoriCond = 0


    def getRegistiAdiacenti(self, r):
        res = []
        for neighbor in self._graph.neighbors(r):
            res.append((neighbor, self._graph[neighbor][r]["weight"]))

        res.sort(key=lambda x: x[1], reverse=True)
        return res


    def cercaRegistiAffini(self, lim, registraPart):
        self._bestPath = []
        self._attoriCond = 0
        edges = set()
        parziale = [registraPart]
        for r in self._graph.neighbors(registraPart):
            if self._graph[registraPart][r]['weight'] <= lim:
                parziale.append(r)
                edges.add((registraPart, r))
                edges.add((r, registraPart))
                self._ricorsione(parziale, lim, edges)
                parziale.pop()
                edges.remove((registraPart, r))
                edges.remove((r, registraPart))

        return self._bestPath, self._attoriCond

    def _ricorsione(self, parziale, lim, edges):
        attoriCondivisi = self.calcolaAttoriCondivisi(parziale)
        if attoriCondivisi > lim:
            return

        if len(parziale) > len(self._bestPath):
            self._bestPath = copy.deepcopy(parziale)
            self._attoriCond = attoriCondivisi

        lastN = parziale[-1]
        for neigbor in self._graph.neighbors(lastN):
            if (lastN, neigbor) not in edges:
                edges.add((lastN, neigbor))
                edges.add((neigbor,lastN))
                parziale.append(neigbor)
                self._ricorsione(parziale, lim, edges)
                edges.remove((lastN, neigbor))
                edges.remove((neigbor, lastN))
                parziale.pop()



    def calcolaAttoriCondivisi(self, listOfNodes):
        tot = 0
        for i in range(0, len(listOfNodes)-1):
            tot+=self._graph[listOfNodes[i]][listOfNodes[i+1]]['weight']
        return tot



    def getDirectors(self):
        return list(self._graph.nodes)

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)
