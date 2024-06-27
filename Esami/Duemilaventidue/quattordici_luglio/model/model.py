import networkx as nx

from Esami.Duemilaventidue.quattordici_luglio.database.DAO import DAO

class Model:
    def __init__(self):
        self._borghi = DAO.getBorghi()
        self._graph = nx.Graph()


    def buildGraph(self, borgo):
        self._graph.clear()
        nodes = DAO.getNodes(borgo)
        self._graph.add_nodes_from(nodes)
        for nta in self._graph.nodes:
            for nta2 in self._graph.nodes:
                if nta != nta2:
                    ssid = DAO.getSSIDV2(nta.NTACode, nta2.NTACode)
                    if len(ssid) != 0:
                        self._graph.add_edge(nta, nta2, weight = len(ssid))


    def analisiArchi(self):
        edges = self._graph.edges(data=True)
        sum = 0
        for e in edges:
            sum += e[2]["weight"]

        pesoMedio = sum/len(edges)

        listArchiPesoMaggiore = [e for e in edges if e[2]["weight"] > pesoMedio]
        listArchiPesoMaggiore.sort(key=lambda x: x[2]["weight"], reverse=True)

        return pesoMedio, listArchiPesoMaggiore


    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getBorghi(self):
        return self._borghi