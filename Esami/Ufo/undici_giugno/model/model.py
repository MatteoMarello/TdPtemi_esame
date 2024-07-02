import copy

import networkx as nx

from Esami.Ufo.undici_giugno.database.DAO import DAO
class Model:
    def __init__(self):
        self._anniWithAvvistamenti = DAO.getAnniWithAvvistamenti()
        self._graph = nx.DiGraph()
        self._sequenza = []


    def buildGraph(self, anno):
        self._graph.clear()
        nodes = DAO.getStati(anno)
        self._graph.add_nodes_from(nodes)
        self._idMap = {s.id: s for s in list(self._graph.nodes)}

        edges = DAO.getEdges(anno, self._idMap)
        self._graph.add_edges_from(edges)


    def getSequenza(self, stato):
        self._sequenza = []
        parziale = [stato]
        numeroNodiRaggiungibili = len(self.getStatiRaggiungibili(stato))

        self._ricorsione(parziale, numeroNodiRaggiungibili)

        return self._sequenza

    def _ricorsione(self, parziale, numeroNodiRaggiungibili):
        if len(parziale) > len(self._sequenza):
            self._sequenza = copy.deepcopy(parziale)

        if len(parziale) == numeroNodiRaggiungibili:
            return

        lastNode = parziale[-1]
        for n in self._graph.neighbors(lastNode):
            if n not in parziale:
                parziale.append(n)
                self._ricorsione(parziale, numeroNodiRaggiungibili)
                parziale.pop()




    def getPredecessors(self, stato):
        res = []
        for p in self._graph.predecessors(stato):
            res.append(p)
        res.sort(key=lambda s: s.id)
        res = [s.id for s in res]
        return res

    def getSuccessors(self, stato):
        res = []
        for s in self._graph.successors(stato):
            res.append(s)
        res.sort(key=lambda s: s.id)
        res = [s.id for s in res]
        return res

    def getStatiRaggiungibili(self, stato):
        nodiRaggiungibili = list(nx.dfs_tree(self._graph, stato).nodes)
        nodiRaggiungibili.remove(stato)
        nodiRaggiungibili.sort(key=lambda s: s.id)
        res = [s.id for s in nodiRaggiungibili]
        return res

    def getStati(self):
        return list(self._graph.nodes)


    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getAnniWithAvvistamenti(self):
        return self._anniWithAvvistamenti