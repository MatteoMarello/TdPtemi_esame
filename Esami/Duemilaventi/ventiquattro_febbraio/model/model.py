import networkx as nx

from Esami.Duemilaventi.ventiquattro_febbraio.database.DAO import DAO
class Model:
    def __init__(self):
        self._matches = DAO.getMatches()
        self._graph = nx.DiGraph()


    def buildGraph(self, matchID):
        self._graph.clear()
        players = DAO.getPlayers(matchID)
        self._graph.add_nodes_from(players)
        for p1 in self._graph.nodes:
            for p2 in self._graph.nodes:
                if not self._graph.has_edge(p1,p2) and not self._graph.has_edge(p2,p1):
                    t1 = p1.teamID
                    t2 = p2.teamID
                    if t1 != t2:
                        e1 = p1.efficiency
                        e2 = p2.efficiency
                        if e1 > e2:
                            self._graph.add_edge(p1,p2,weight=e1-e2)
                        elif e2 > e1:
                            self._graph.add_edge(p2,p1,weight=e2-e1)
                        else:
                            self._graph.add_edge(p1,p2,weight=0)


    def getBestPlayer(self):
        res = []
        for p in self._graph.nodes:
            efficienzaPositiva = self.getPesoArchiUscenti(p)
            efficienzaNegativa = self.getPesoArchiEntranti(p)
            res.append((p, efficienzaPositiva-efficienzaNegativa))

        res.sort(key=lambda e: e[1], reverse=True)
        return res[0][0], res[0][1]


    def getPesoArchiUscenti(self, p):
        tot = 0
        for n in self._graph.successors(p):
            tot += self._graph[p][n]["weight"]
        return tot

    def getPesoArchiEntranti(self,p):
        tot=0
        for n in self._graph.predecessors(p):
            tot+=self._graph[n][p]["weight"]
        return tot


    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getMatches(self):
        return self._matches