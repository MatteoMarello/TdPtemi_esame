import copy

import networkx as nx
import geopy.distance
from Lab.Lab13.database.DAO import DAO
class Model:
    def __init__(self):
        self.graph = nx.Graph()
        self._states = DAO.getStates()
        self._idMap = {s.id: s for s in self._states}
        self.graph.add_nodes_from(self._states)
        edges = DAO.getEdges(self._idMap)
        self.graph.add_edges_from(edges)


    def getYears(self):
        return DAO.getYears()

    def getShapes(self):
        return DAO.getShapes()

    def buildGraph(self, year, shape):
        for edge in self.graph.edges:
            s1 = edge[0].id
            s2 = edge[1].id
            try :
                avvS1 = int(DAO.getNumAvvistamenti(s1, year, shape))
            except ValueError:
                avvS1 = 0
            try:
                avvS2 = int(DAO.getNumAvvistamenti(s2, year, shape))
            except ValueError:
                avvS2 = 0

            self.graph[edge[0]][edge[1]]["weight"] = avvS2 + avvS1
            self.graph[edge[0]][edge[1]]["distance"] = self.getDistanceBetweenStates(edge[0], edge[1])

    def getGraphDetails(self):
        res = []
        for node in self.graph.nodes:
            pesoArchiAdiacenti = 0
            for neighbor in self.graph.neighbors(node):
                pesoArchiAdiacenti += self.graph[node][neighbor]["weight"]

            res.append((node, pesoArchiAdiacenti))

        return res


    def getPercorso(self):
        parziale = []
        self._bestSol = []
        self._distMax = 0
        for stato in self.graph.nodes:
            parziale.append(stato)
            self._ricorsione(parziale)
            parziale.pop()

        res = []
        for i in range(0, len(self._bestSol)-1):
            weight = self.graph[self._bestSol[i]][self._bestSol[i+1]]["weight"]
            distanza = self.graph[self._bestSol[i]][self._bestSol[i+1]]["distance"]
            res.append((self._bestSol[i], self._bestSol[i+1], weight, distanza))


        return res, self._distMax


    def _ricorsione(self, parziale):
        distanzaSoluzione = self._distSoluzione(parziale)
        if distanzaSoluzione > self._distMax:
            self._bestSol = copy.deepcopy(parziale)
            self._distMax = distanzaSoluzione

        lastNode = parziale[-1]
        for neighbor in self.graph.neighbors(lastNode):
            if len(parziale) == 1:
                parziale.append(neighbor)
                self._ricorsione(parziale)
                parziale.pop()

            else:
                lastEdgeWeight = self.graph[parziale[-2]][parziale[-1]]["weight"]
                if neighbor not in parziale and self.graph[lastNode][neighbor]["weight"] > lastEdgeWeight:
                    parziale.append(neighbor)
                    self._ricorsione(parziale)
                    parziale.pop()





    def _distSoluzione(self, listOfNodes):
        dist = 0
        if len(listOfNodes) == 1:
            return 0
        for i in range(0, len(listOfNodes)-1):
            dist += self.graph[listOfNodes[i]][listOfNodes[i+1]]["distance"]
        return dist




    def getDistanceBetweenStates(self, s1, s2):
        p0 = (s1.Lat, s1.Lng)
        p1 = (s2.Lat, s2.Lng)
        dist = geopy.distance.distance(p0, p1).km
        return dist


    def getGraphSizes(self):
        return len(self.graph.nodes), len(self.graph.edges)


if __name__ == "__main__":
    model = Model()
    model.buildGraph(2015, "Circle")