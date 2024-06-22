import networkx as nx

from Esami.Duemilaventi.quattordici_luglio.database.DAO import DAO

class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        self._teams = DAO.getTeams()
        self._idMap = {t.TeamID : t for t in self._teams}


    def buildGraph(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._teams)
        teamPoints = self.defineRanking()

        for team in teamPoints.keys():
            for otherT in teamPoints.keys():
                differenzaPunti = teamPoints[team] - teamPoints[otherT]
                if team != otherT and differenzaPunti > 0:
                    t1 = self._idMap[team]
                    t2 = self._idMap[otherT]
                    self._grafo.add_edge(t1, t2, weight=differenzaPunti)


    def defineRanking(self):
        matches = DAO.getMatches()
        teamPoints = {t.TeamID : 0 for t in self._teams}
        for m in matches:
            if m[2] == 1:
                teamPoints[m[0]] += 3
            elif m[2] == 0:
                teamPoints[m[0]] += 1
                teamPoints[m[1]] += 1
            else:
                teamPoints[m[1]] += 3

        return teamPoints

    def getClassifiche(self, team):
        classificaMigliori = []
        for p in self._grafo.predecessors(team):
            classificaMigliori.append((p, self._grafo[p][team]["weight"]))

        classificaPeggiori = []
        for s in self._grafo.successors(team):
            classificaPeggiori.append((s, self._grafo[team][s]["weight"]))

        classificaMigliori.sort(key=lambda x: x[1])
        classificaPeggiori.sort(key=lambda y: y[1])

        return classificaMigliori, classificaPeggiori

    def getTeams(self):
        return self._teams

    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)
