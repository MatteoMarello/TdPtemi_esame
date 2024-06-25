import copy

import networkx as nx

from Esami.Duemilaventidue.quattordici_settembre.database.DAO import DAO
class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._bestSetAlbum = []
        self._durataBest = 0

    def buildGraph(self, d):
        self._graph.clear()
        albums = DAO.getAlbums(d)
        self._graph.add_nodes_from(albums)
        self._idMap = {a.AlbumId: a for a in self._graph.nodes}
        edges = DAO.getEdges(self._idMap)
        self._graph.add_edges_from(edges)

    def getConnCompInfo(self, album):
        connComp = nx.node_connected_component(self._graph, album)
        durata = self.getDurataConnComp(connComp)

        return len(connComp), durata

    def getSetAlbum(self, album, dTOT):
        self._durataBest = 0
        self._bestSetAlbum = []
        connComp = nx.node_connected_component(self._graph, album)
        parziale = set()
        parziale.add(album)
        self._ricorsione(parziale, connComp, dTOT)
        return self._bestSetAlbum, self._durataBest/60/1000


    def _ricorsione(self, parziale, connComp, dTOT):
        durataParziale = self.getDurataListaAlbumMs(parziale)
        if durataParziale > dTOT:
            return

        if len(parziale) > len(self._bestSetAlbum):
            self._bestSetAlbum = copy.deepcopy(parziale)
            self._durataBest = durataParziale

        listAlbums = list(connComp)
        listAlbums.sort(key=lambda a: a.durata)

        for a in listAlbums:
            if a not in parziale:
                parziale.add(a)
                self._ricorsione(parziale, connComp, dTOT)
                return



    def getDurataConnComp(self, connComp):
        tot = 0
        for a in connComp:
            tot += a.durata

        return tot/60/1000

    def getDurataListaAlbumMs(self, listOfAlbums):
        tot = 0
        for a in listOfAlbums:
            tot += a.durata

        return tot
    def getAlbums(self):
        return list(self._graph.nodes)


    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)
