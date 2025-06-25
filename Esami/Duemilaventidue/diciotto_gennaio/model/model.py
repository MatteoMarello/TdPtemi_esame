import copy
import random

import networkx as nx
from geopy.distance import distance

from Esami.Duemilaventidue.diciotto_gennaio.database.DAO import DAO
class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idmap = {}
        self.bestSol = []
        self.bestScore = 0


    def build_graph(self, providernome, distanza):
        self._grafo.clear()
        self._idmap.clear()
        nodi = DAO.getNodi(providernome)
        for n in nodi:
            self._idmap[n.Location] = n
        self._grafo.add_nodes_from(nodi)
        from itertools import combinations
        for u, v in combinations(nodi, 2):
            distanza_km = distance((u.Latitude, u.Longitude), (v.Latitude, v.Longitude)).km
            if distanza_km <= distanza:
                self._grafo.add_edge(u, v, weight = distanza_km)

    def get_provider(self):
        return DAO.getProvider()

    def getGraphDetails(self):
        return self._grafo.number_of_nodes(), self._grafo.number_of_edges()

    def getVerticiParticolari(self):
        bestNumeroVicini = 0
        for n in self._idmap.values():
            vicini = self._grafo.neighbors(n)
            lunghezzaista= len(list(vicini))
            if lunghezzaista > bestNumeroVicini:
                bestNumeroVicini = lunghezzaista

        listaMigliori =[]
        for n in self._idmap.values():
            vicini = self._grafo.neighbors(n)
            if len(list(vicini)) == bestNumeroVicini:
                listaMigliori.append(f"nodo di località: {n.Location}, con numero vicini {bestNumeroVicini}")
        return listaMigliori





