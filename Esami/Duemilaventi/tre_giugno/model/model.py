import copy

import networkx as nx

from Esami.Duemilaventi.tre_giugno.database.DAO import DAO

class Model:
    def __init__(self):
        self._players = DAO.getPlayers()
        self._idMap = {p.PlayerID : p for p in self._players}
        self._grafo = nx.DiGraph()
        self._dreamTeam = []
        self._bestGradoTitolarita = 0


    def buildGraph(self, avgGoals):
        self._grafo.clear()
        nodes = DAO.getNodes(avgGoals, self._idMap)
        self._grafo.add_nodes_from(nodes)

        for p in self._grafo.nodes:
            for p2 in self._grafo.nodes:
                if p != p2:
                    if not self._grafo.has_edge(p, p2):
                        minutesPlayed = DAO.getEdge(p.PlayerID, p2.PlayerID)
                        if minutesPlayed:
                            t1 = minutesPlayed[0][0]
                            t2 = minutesPlayed[0][1]
                            if t1 > t2:
                                self._grafo.add_edge(p, p2, weight=t1-t2)
                            elif t2 > t1:
                                self._grafo.add_edge(p2,p,weight=t2-t1)

    def getTopPlayer(self):
        list_p = []
        for p in self._grafo.nodes:
            giocatoriBattuti = len(list((self._grafo.successors(p))))
            list_p.append((p, giocatoriBattuti))

        list_p.sort(key=lambda x: x[1], reverse=True)
        topPlayer = list_p[0][0]

        res = []
        for battuto in self._grafo.successors(topPlayer):
            res.append((battuto, self._grafo[topPlayer][battuto]["weight"]))

        res.sort(key=lambda y: y[1], reverse=True)

        return topPlayer, res


    def getDreamTeam(self, k):
        self._dreamTeam = []
        self._bestGradoTitolarita = 0
        parziale = []
        for player in self._grafo.nodes:
            parziale.append(player)
            availableNodes = [n for n in self._grafo.predecessors(player)]
            self._ricorsione(k, parziale, availableNodes)
            parziale.pop()

        return self._dreamTeam, self._bestGradoTitolarita


    def _ricorsione(self, k, parziale, availableNodes):
        gradoTitolarita = self.getGradoTitolarita(parziale)
        if gradoTitolarita > self._bestGradoTitolarita:
            self._bestGradoTitolarita = gradoTitolarita
            self._dreamTeam = copy.deepcopy(parziale)

        if len(parziale) == k:
            return

        for player in availableNodes:
            parziale.append(player)
            availableNodes = [n for n in self._grafo.predecessors(player)]
            self._ricorsione(k, parziale, availableNodes)
            parziale.pop()




    def getGradoTitolarita(self, listOfNodes):
        gradoTot = 0
        for player in listOfNodes:
            pesoArchiUscenti = self.getPesoArchiUscenti(player)
            pesoArchiEntranti = self.getPesoArchiEntranti(player)
            gradoPlayer = pesoArchiUscenti - pesoArchiEntranti
            gradoTot += gradoPlayer

        return gradoTot


    def getPesoArchiUscenti(self, player):
        tot = 0
        for n in self._grafo.successors(player):
            tot += self._grafo[player][n]["weight"]

        return tot

    def getPesoArchiEntranti(self, player):
        tot = 0
        for n in self._grafo.predecessors(player):
            tot += self._grafo[n][player]["weight"]

        return tot


    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)
