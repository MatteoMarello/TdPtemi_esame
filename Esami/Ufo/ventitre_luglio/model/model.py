import networkx as nx

from Esami.Ufo.ventitre_luglio.database.DAO import DAO
class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._states = DAO.getStati()
        self._idMap = {s.id: s for s in self._states}

    def buildGraph(self, anno, giorni):
        self._graph.clear()
        self._graph.add_nodes_from(self._states)
        edges = DAO.getEdges(self._idMap)
        self._graph.add_edges_from(edges)
        for edge in edges:
            s1 = edge[0].id
            s2 = edge[1].id
            peso = DAO.getEdgeWeight(giorni, anno, s1, s2)
            self._graph[edge[0]][edge[1]]["weight"] = peso

    def getPesoArchiAdiacenti(self):
        res = []
        for n in self._graph.nodes:
            res.append((n, self.calcolaPesoArchiAdiacenti(n)))

        res.sort(key=lambda x: x[0].Name)
        return res


    def calcolaPesoArchiAdiacenti(self, stato):
        tot = 0
        for n in self._graph.neighbors(stato):
            tot+=self._graph[stato][n]["weight"]

        return tot

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)
