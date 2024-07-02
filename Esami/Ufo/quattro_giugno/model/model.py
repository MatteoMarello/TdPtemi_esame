import copy

import networkx as nx
from geopy.distance import distance
from Esami.Ufo.quattro_giugno.database.DAO import DAO
class Model:
    def __init__(self):
        self._anni = DAO.getAnni()
        self._graph = nx.Graph()
        self._states = DAO.getStates()
        self._idMap = {s.id : s for s in self._states}
        self._edges = DAO.getEdges(self._idMap)
        self._bestPath = []
        self._bestDistance = 0


    def buildGraph(self, year, shape):
        self._graph.clear()
        self._graph.add_nodes_from(self._states)
        self._graph.add_edges_from(self._edges)

        for edge in self._graph.edges:
            s1 = edge[0].id.lower()
            s2 = edge[1].id.lower()
            pesoArco = DAO.getNumeroAvvistamenti(year, shape, s1, s2)
            self._graph[edge[0]][edge[1]]["weight"] = pesoArco
            self._graph[edge[0]][edge[1]]["distance"] = self.calcolaDistanzaStati(edge[0], edge[1])

        res = []
        for n in self._graph.nodes:
            pesoArchiAdiacenti = self.getPesoArchiAdiacenti(n)
            res.append((n, pesoArchiAdiacenti))
        res.sort(key=lambda x: x[0].id)
        return res

    def getPesoArchiAdiacenti(self, n):
        tot=0
        for neighbor in self._graph.neighbors(n):
            tot += self._graph[n][neighbor]["weight"]

        return tot

    def calcolaDistanzaStati(self, s1, s2):
        coordS1 = (s1.Lat, s1.Lng)
        coordS2 = (s2.Lat, s2.Lng)
        return distance(coordS1, coordS2).km


    def getBestPath(self):
        self._bestDistance = 0
        self._bestPath = []
        parziale = []
        for n in self._graph.nodes:
            parziale.append(n)
            self._ricorsione(parziale)
            parziale.pop()

        res = []
        for i in range(0, len(self._bestPath)-1):
            res.append((self._bestPath[i], self._bestPath[i+1], self._graph[self._bestPath[i]][self._bestPath[i+1]]["weight"], self._graph[self._bestPath[i]][self._bestPath[i+1]]["distance"]))

        return res, self._bestDistance


    def _ricorsione(self, parziale):
        distanzaParziale = self.calcolaDistanzaParziale(parziale)
        if distanzaParziale > self._bestDistance:
            self._bestDistance = distanzaParziale
            self._bestPath = copy.deepcopy(parziale)

        lastNode = parziale[-1]

        for neighbor in self._graph.neighbors(lastNode):
            if len(parziale) == 1:
                parziale.append(neighbor)
                self._ricorsione(parziale)
                parziale.pop()

            else:
                lastEdgeW = self._graph[parziale[-2]][parziale[-1]]["weight"]
                if neighbor not in parziale and self._graph[neighbor][lastNode]["weight"] > lastEdgeW:
                    parziale.append(neighbor)
                    self._ricorsione(parziale)
                    parziale.pop()


    def calcolaDistanzaParziale(self, listOfStates):
        if len(listOfStates) == 1:
            return 0
        tot = 0
        for i in range(0, len(listOfStates)-1):
            tot+=self._graph[listOfStates[i]][listOfStates[i+1]]["distance"]
        return tot


    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getAnni(self):
        return self._anni

    def getShapesYear(self, year):
        return DAO.getShapesYear(year)
