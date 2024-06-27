import networkx as nx

from Esami.Duemilaventidue.trentuno_maggio.database.DAO import DAO
from geopy.distance import distance
class Model:
    def __init__(self):
        self._providers = DAO.getProviders()
        self._graph = nx.Graph()


    def buildGraph(self, provider):
        self._graph.clear()
        cities = DAO.getCities(provider)
        self._graph.add_nodes_from(cities)
        for n in self._graph.nodes:
            for n2 in self._graph.nodes:
                if n != n2:
                    dist = distance((n.latitude, n.longitude), (n2.latitude, n2.longitude)).km
                    self._graph.add_edge(n, n2, weight=dist)


    def getQuartieriAdiacenti(self, quartiere):
        res = []
        for n in self._graph.neighbors(quartiere):
            res.append((n, self._graph[quartiere][n]["weight"]))

        res.sort(key=lambda x: x[1])
        return res


    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getCities(self):
        return list(self._graph.nodes)

    def getProviders(self):
        return self._providers