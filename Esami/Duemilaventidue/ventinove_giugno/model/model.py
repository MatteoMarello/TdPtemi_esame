import copy

import networkx as nx

from Esami.Duemilaventidue.ventinove_giugno.database.DAO import DAO
class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._bestScore = 0
        self._bestPath = []


    def buildGraph(self, n):
        self._graph.clear()
        self._albums = DAO.getAlbums(n)
        self._graph.add_nodes_from(self._albums)
        for album in self._graph.nodes:
            for album2 in self._graph.nodes:
                c1 = album.nCanzoni
                c2 = album2.nCanzoni
                if c1 > c2:
                    self._graph.add_edge(album2, album, weight=c1-c2)
                elif c2 > c1:
                    self._graph.add_edge(album, album2, weight=c2-c1)


    def getAdiacenze(self, a1):
        res = []
        for s in self._graph.successors(a1):
            bilancio = self.calcolaBilancio(s)
            res.append((s, bilancio))

        res.sort(key=lambda x: x[1], reverse=True)

        return res


    def getPercorso(self, a1, a2, x):
        self._bestScore = 0
        self._bestPath = []
        parziale = [a1]
        bil = self.calcolaBilancio(a1)
        self._ricorsione(parziale, bil, a2, x)

        res = []
        for i in range(0, len(self._bestPath)-1):
            res.append((self._bestPath[i], self._bestPath[i+1], self._graph[self._bestPath[i]][self._bestPath[i+1]]["weight"]))

        return res

    def _ricorsione(self, parziale, bil, a2, x):

        if parziale[-1] == a2:
            score = 0
            for a in parziale:
                bilancioAlbum = self.calcolaBilancio(a)
                if bilancioAlbum > bil:
                    score += 1

            if score > self._bestScore:
                self._bestScore = score
                self._bestPath = copy.deepcopy(parziale)

            return


        lastNode = parziale[-1]
        for succ in self._graph.successors(lastNode):
            if succ not in parziale and self._graph[lastNode][succ]["weight"] >= x:
                parziale.append(succ)
                self._ricorsione(parziale, bil, a2, x)
                parziale.pop()


    def has_path(self, a1, a2):
       return nx.has_path(self._graph, a1, a2)

    def calcolaBilancio(self, album):
        sommaPesiArchiEntranti = 0
        sommaPesiArchiUscenti = 0
        for p in self._graph.predecessors(album):
            sommaPesiArchiEntranti += self._graph[p][album]["weight"]
        for s in self._graph.successors(album):
            sommaPesiArchiUscenti += self._graph[album][s]["weight"]

        return sommaPesiArchiEntranti - sommaPesiArchiUscenti

    def getAlbums(self):
        return self._albums

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)
