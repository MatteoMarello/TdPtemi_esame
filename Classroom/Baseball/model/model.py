import copy
import itertools

import networkx as nx

from Classroom.Baseball.database.DAO import DAO

class Model:
    def __init__(self):
        self.allTeams = None
        self._idMapTeams = None
        self.grafo = nx.Graph()
        self._idMapTeams = {}
        self._bestPath = []
        self._bestObjVal = 0

    def getPercorso(self, v0):
        self._bestPath = []
        self._bestObjVal = 0
        parziale = [v0]

        listaVicini = []
        for v in self.grafo.neighbors(parziale[-1]):
            edgeV = self.grafo[parziale[-1]][v]["weight"]
            listaVicini.append((v, edgeV))

        listaVicini.sort(key=lambda x: x[1], reverse=True)
        parziale.append(listaVicini[0][0]) # Metto il primo elemento della lista in parziale. Sicuramente il primo elemento della lista è quello che mi garantisce la soluzione migliore.
        self._ricorsioneV2(parziale)
        parziale.pop()

        return self.getWeightsOfPath(self._bestPath)

    def _ricorsione(self, parziale):
        if self._getScore(parziale) > self._bestObjVal:
            self._bestObjVal = self._getScore(parziale)
            self._bestPath = copy.deepcopy(parziale)

        for v in self.grafo.neighbors(parziale[-1]):
            edgeW = self.grafo[parziale[-1]][v]["weight"]
            if v not in parziale and self.grafo[parziale[-2]][parziale[-1]]["weight"] > edgeW:
                parziale.append(v)
                self._ricorsione(parziale)
                parziale.pop()

    def _ricorsioneV2(self, parziale):
        if self._getScore(parziale) > self._bestObjVal:
            self._bestObjVal = self._getScore(parziale)
            self._bestPath = copy.deepcopy(parziale)

        listaVicini = []
        for v in self.grafo.neighbors(parziale[-1]):
            edgeV = self.grafo[parziale[-1]][v]["weight"]
            listaVicini.append( (v, edgeV) )
        listaVicini.sort(key=lambda x: x[1], reverse=True)

        for v1 in listaVicini:
            if v1[0] not in parziale and self.grafo[parziale[-2]][parziale[-1]]["weight"] > v1[1]:
                parziale.append(v1[0])
                self._ricorsioneV2(parziale)
                parziale.pop()
                # se entro nell'if posso mettere il return perchè sicuramente questo caso mi garantiscela soluzione migliore
                # perchè la soluzione migliore è quella che mi ordina tutti gli archi possibili in ordine decrescente di peso.
                return


    def _getScore(self, listOfNodes):
        if len(listOfNodes) == 1:
            return 0
        score = 0
        for i in range(0, len(listOfNodes)-1):
            score += self.grafo[listOfNodes[i]][listOfNodes[i+1]]["weight"]
        return score


    def buildGraph(self, year):
        self.grafo.clear()
        if len(self.allTeams) == 0:
            print("Lista squadre vuota")
            return

        self.grafo.add_nodes_from(self.allTeams)

        # Modo 1
        """
        for t1 in self.grafo.nodes:
            for t2 in self.grafo.nodes:
                if t1 != t2:
                    self.grafo.add_edge(t1, t2)
        """

        # Modo 2 - usando la libreria itertools di Python, che fornisce una serie di metodi comodi per lavorare sugli iteratori.
        # Possiamo usare il metodo .combinations(), che ci restituisce le combinazioni degli elementi di una lista che gli passiamo
        # come argomento. Questo ci permette di non avere ripetizioni, quindi se ho (a,b) non potrò avere (b,a).

        myedges = list(itertools.combinations(self.allTeams, 2))
        self.grafo.add_edges_from(myedges)

        # Aggiungere i pesi
        salariesOfTeams = DAO.getSalaryOfTeams(year, self._idMapTeams)
        for e in self.grafo.edges:
            # L'arco fra due squadre corrisponde alla somma dei salari dei giocatori che hanno giocato per le due squadre nell'anno indicato.
            self.grafo[e[0]][e[1]]["weight"] = salariesOfTeams[e[0]] + salariesOfTeams[e[1]]

    def getWeightsOfPath(self, path):
        listTuples = [(path[0], 0)]
        for i in range(0, len(path)-1):
            listTuples.append( (path[i+1], self.grafo[path[i]][path[i+1]]["weight"]) )

        return listTuples

    def getSortedNeighbors(self, v0):
        vicini = self.grafo.neighbors(v0)
        viciniTuple = []
        for v in vicini:
            viciniTuple.append( (v, self.grafo[v0][v]["weight"]) )

        viciniTuple.sort(key=lambda x: x[1], reverse=True)
        return viciniTuple

    def getYears(self):
        return DAO.getAllYears()

    def getTeamsOfYear(self, year):
        self.allTeams = DAO.getTeamsOfYear(year)
        self._idMapTeams = {t.ID: t for t in self.allTeams}
        return self.allTeams

    def printGraphDetails(self):
        print(f"Grafo creato con {len(self.grafo.nodes)} nodi e {len(self.grafo.edges)} archi")

    def getGraphDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)


if __name__ == "__main__":
    model = Model()
    model.getTeamsOfYear(2015)
    model.buildGraph(2015)
    model.printGraphDetails()
    v0 = list(model.grafo.nodes)[2]
    vicini = model.getSortedNeighbors(v0)
    for v in vicini:
        print(f"{v[1]} -> {v[0]}")

    path = model.getPercorso(v0)
    print(len(path))
