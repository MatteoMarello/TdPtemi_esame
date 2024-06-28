import networkx as nx
import itertools
from Esami.Duemilaventitre.trenta_giugno.database.DAO import DAO
class Model:
    def __init__(self):
        self._teams = DAO.getTeams()
        self._graph = nx.Graph()


    def buildGraph(self, team):
        self._graph.clear()
        nodes = DAO.getNodes(team)
        self._graph.add_nodes_from(nodes)
        edges = list(itertools.combinations(nodes, 2))
        self._graph.add_edges_from(edges)
        for edge in edges:
            firstYear = edge[0]
            secondYear = edge[1]
            pesoArco = DAO.getWeight(firstYear, secondYear, team)
            if pesoArco:
                self._graph[firstYear][secondYear]["weight"] = pesoArco
            else:
                self._graph[firstYear][secondYear]["weight"] = 0

    def getAnniAdiacenti(self, anno):
        res = []
        for n in self._graph.neighbors(anno):
            res.append((n, self._graph[anno][n]["weight"]))

        res.sort(key=lambda x: x[1], reverse=True)
        return res


    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getAnni(self):
        return list(self._graph.nodes)


    def getTeams(self):
        return self._teams