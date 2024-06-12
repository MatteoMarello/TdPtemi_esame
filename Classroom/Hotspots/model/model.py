import copy
import random

import networkx as nx

from Classroom.Hotspots.database.DAO import DAO
from geopy.distance import distance

class Model:
    def __init__(self):
        self._providers = DAO.getAllProviders()
        self._graph = nx.Graph()
        self._bestPath = []
        self._bestLen = 0

    def getAllProviders(self):
        return self._providers

    def getAllLocations(self):
        return self._graph.nodes

    def buildGraph(self, provider, soglia):
        self._graph.clear()
        self._nodes = DAO.getLocationsOfProvider(provider)
        self._graph.add_nodes_from(self._nodes)

        # Add Edges.
        # Modo 1: faccio una query che restituisce gli archi
        """
        allEdges = DAO.getAllEdges(provider)
        for edge in allEdges:
            l1 = edge[0]
            l2 = edge[1]
            if distance((l1.latitude, l1.longitude), (l2.latitude, l2.longitude)).km < soglia:
                self._graph.add_edge(l1.Location,l2.Location, weight = distance((l1.latitude, l1.longitude), (l2.latitude, l2.longitude)).km)
        """

        # Modo 2: Modifico il metodo del DAO che legge i nodi e ci aggiungo le coordinate di ogni Location,
        # Dopo... doppio ciclo sui nodi e mi calcolo le distanze in Python
        for u in self._nodes:
            for v in self._nodes:
                if u != v:
                    dist = distance((u.latitude, u.longitude), (v.latitude, v.longitude)).km
                    if dist < soglia:
                        self._graph.add_edge(u, v, weight = dist)

        # Modo 3: Doppio ciclo sui nodi e per ogni possibile arco faccio una query


    def getNodesMostVicini(self):
        listTuple = []
        for v in self._nodes:
            listTuple.append((v, len(list(self._graph.neighbors(v)))))

        listTuple.sort(key=lambda x: x[1], reverse=True)

        # result = filter(lambda x: x[1] == listTuple[0][1] , listTuple)
        result = [x for x in listTuple if x[1] == listTuple[0][1]]
        return result

    def getCammino(self, target, substring):
        sources = self.getNodesMostVicini()
        source = sources[random.randint(0, len(sources)-1)][0]
        if not nx.has_path(self._graph, source, target):
            print(f"{source} e {target} non sono connessi")
            return [], source

        self._bestPath = []
        self._bestLen = 0
        parziale = [source]

        self._ricorsione(parziale, target, substring)

        return self._bestPath, source

    def _ricorsione(self, parziale, target, substring):
        if parziale[-1] == target:
            if len(parziale) > self._bestLen:
                self._bestLen = len(parziale)
                self._bestPath = copy.deepcopy(parziale)
            return

        for v in self._graph.neighbors(parziale[-1]):
            if v not in parziale and substring not in v.Location:
                parziale.append(v)
                self._ricorsione(parziale, target, substring)
                parziale.pop()

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)
