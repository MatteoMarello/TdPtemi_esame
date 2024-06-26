import copy

import networkx as nx

from Esami.Duemilaventidue.ventiquattro_maggio.database.DAO import DAO
class Model:
    def __init__(self):
        self._generi = DAO.getGeneri()
        self._graph = nx.Graph()
        self._bestLista = []
        self._bestLength = 0


    def buildGraph(self, g):
        self._graph.clear()
        nodes = DAO.getNodes(g)
        self._graph.add_nodes_from(nodes)

        for t in self._graph.nodes:
            for t2 in self._graph.nodes:
                if t != t2 and t.MediaTypeId == t2.MediaTypeId:
                    pesoGrafo = abs(t.Milliseconds - t2.Milliseconds)
                    self._graph.add_edge(t, t2, weight=pesoGrafo)


    def getDeltaMax(self):
        archi = list(self._graph.edges(data=True))
        archi.sort(key=lambda x: x[2]["weight"], reverse=True)
        res = []
        res.append(archi[0])
        pesoMax = archi[0][2]["weight"]
        for otherArco in archi[1:]:
            if otherArco[2]["weight"] == pesoMax:
                res.append(otherArco)
            if otherArco[2]["weight"] < pesoMax:
                break

        return res


    def getLista(self, track, memoriaMax):
        self._bestLista = []
        self._bestLength = 0
        parziale = [track]
        comp = list(nx.node_connected_component(self._graph, track))
        comp.sort(key=lambda t: t.Bytes)
        for t in comp:
            if t != track:
                parziale.append(t)
                self._ricorsione(parziale, memoriaMax, comp)


        return self._bestLista, self._calcolaMemoria(self._bestLista)


    def _ricorsione(self, parziale, memoriaMax, comp):
        memoriaParziale = self._calcolaMemoria(parziale)
        if memoriaParziale > memoriaMax:
            return

        if len(parziale) > self._bestLength:
            self._bestLista = copy.deepcopy(parziale)
            self._bestLength = len(parziale)

        for t in comp:
            if t not in parziale:
                parziale.append(t)
                self._ricorsione(parziale, memoriaMax, comp)
                return

    def _calcolaMemoria(self, listaOfTracks):
        tot = 0
        for t in listaOfTracks:
            tot += t.Bytes
        return tot



    def getTracks(self):
        return list(self._graph.nodes)


    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getGeneri(self):
        return self._generi