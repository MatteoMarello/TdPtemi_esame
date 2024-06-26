import copy
import random

import networkx as nx
from geopy.distance import distance
from Esami.Duemilaventidue.diciotto_gennaio.database.DAO import DAO
class Model:
    def __init__(self):
        self._providers = DAO.getProviders()
        self._graph = nx.Graph()
        self._bestPercorso = []

    def buildGraph(self, provider, km):
        self._graph.clear()
        nodes = DAO.getLocations(provider)
        self._graph.add_nodes_from(nodes)
        for loc in self._graph.nodes:
            for loc2 in self._graph.nodes:
                if loc != loc2:
                    dist = distance((loc.Latitude, loc.Longitude), (loc2.Latitude, loc2.Longitude)).km
                    if dist <= km:
                        self._graph.add_edge(loc, loc2, weight = dist)

    def getNodiMostVicini(self):
        res = []
        for l in self._graph.nodes:
            res.append((l, len(list(self._graph.neighbors(l)))))

        res.sort(key=lambda l: l[1], reverse=True)
        mostVicini = res[0][1]
        listaMostVicini = [l for l in res if l[1] == mostVicini]
        return listaMostVicini


    def getPercorso(self, string, localitaTarget):
        self._bestPercorso = []
        nodiMostVicini = self.getNodiMostVicini()
        localitaPossibili = [l[0] for l in nodiMostVicini]
        localitaPartenza = localitaPossibili[random.randint(0, len(localitaPossibili)-1)]
        if not nx.has_path(self._graph, localitaPartenza, localitaTarget):
            return None

        parziale = [localitaPartenza]
        self._ricorsione(parziale, string, localitaTarget)

        return self._bestPercorso


    def _ricorsione(self, parziale, string, localitaTarget):
        lastNode = parziale[-1]
        if lastNode == localitaTarget:
            if len(parziale) > len(self._bestPercorso):
                self._bestPercorso = copy.deepcopy(parziale)
            return

        for neighbor in self._graph.neighbors(lastNode):
            if neighbor not in parziale and string not in neighbor.Location:
                parziale.append(neighbor)
                self._ricorsione(parziale, string, localitaTarget)
                parziale.pop()


    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getProviders(self):
        return self._providers

    def getLocalita(self):
        return list(self._graph.nodes)
