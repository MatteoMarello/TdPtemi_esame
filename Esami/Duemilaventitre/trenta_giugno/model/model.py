import networkx as nx
import itertools
from Esami.Duemilaventitre.trenta_giugno.database.DAO import DAO
class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}
        self.bestSottoinsieme = set()
        self.bestTasso = float('inf')

    def build_graph(self, id):
        self._grafo.clear()
        self._idMap = {}
        tuple = DAO.getNodi(id)
        setnodi = set()
        for tup in tuple:
            setnodi.add(tup[0])

        for tupla in tuple:
            if int(tupla[0]) in self._idMap.keys():
                self._idMap[int(tupla[0])].append(tupla[1])
            else:
                self._idMap[int(tupla[0])] = [tupla[1]]

        self._grafo.add_nodes_from(setnodi)
        if len(setnodi) == 0:
            return

        from itertools import combinations
        for u, v in combinations(setnodi, 2):
            cnt = 0
            for giocatore in self._idMap[u]:
                for giocatore2 in self._idMap[v]:
                    if giocatore == giocatore2:
                        cnt +=1
            if cnt > 0:
                self._grafo.add_edge(u, v, weight= cnt)

    def getGraphDetails(self):
        return self._grafo.number_of_nodes(), self._grafo.number_of_edges()

    def get_teams(self):
        return DAO.getTeams()

