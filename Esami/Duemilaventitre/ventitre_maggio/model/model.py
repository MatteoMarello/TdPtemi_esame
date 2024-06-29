import copy

import networkx as nx

from Esami.Duemilaventitre.ventitre_maggio.database.DAO import DAO
class Model:
    def __init__(self):
        self._anni = DAO.getAnni()
        self._graph = nx.Graph()
        self._dreamTeam = []
        self._bestSalary = 0

    def buildGraph(self, anno, salario):
        self._graph.clear()
        players = DAO.getPlayers(anno, salario)
        self._idMap = {p.playerID: p for p in players}
        self._graph.add_nodes_from(players)
        edges = DAO.getEdges(anno, salario, self._idMap)
        self._graph.add_edges_from(edges)


    def getDreamTeam(self):
        self._dreamTeam = []
        self._bestSalary = 0
        parziale = []
        players = list(self._graph.nodes)
        players.sort(key=lambda p: p.salary, reverse=True)
        parziale.append(players[0])
        self._ricorsione(parziale, players)

        return self._dreamTeam, self._bestSalary


    def _ricorsione(self, parziale, players):
        salarioTOT = self._calcolaSalarioTeam(parziale)
        if salarioTOT > self._bestSalary:
            self._bestSalary = salarioTOT
            self._dreamTeam = copy.deepcopy(parziale)

        playersArruolabili = self.getPlayersArruolabili(parziale, copy.deepcopy(players))
        playersArruolabili.sort(key=lambda p: p.salary, reverse=True)

        for p in playersArruolabili:
            if p not in parziale:
                parziale.append(p)
                self._ricorsione(parziale, playersArruolabili)
                return



    def getPlayersArruolabili(self, listOfPlayers, allPlayers):
        for player in listOfPlayers:
            for teammate in self._graph.neighbors(player):
                if teammate in allPlayers:
                    allPlayers.remove(teammate)

        return allPlayers

    def _calcolaSalarioTeam(self, listOfPlayers):
        tot = 0
        for p in listOfPlayers:
            tot += p.salary
        return tot

    def getPlayerGradoMax(self):
        res = []
        for n in self._graph.nodes:
            res.append((n, self._graph.degree(n)))

        res.sort(key=lambda x: x[1], reverse=True)
        return res[0]


    def getNConnComp(self):
        return len(list(nx.connected_components(self._graph)))

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getAnni(self):
        return self._anni
