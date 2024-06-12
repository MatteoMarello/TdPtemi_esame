import copy

import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        cromosomi = DAO.getCromosomi()
        self._grafo.add_nodes_from(cromosomi)
        for c in self._grafo.nodes:
            for c1 in self._grafo.nodes:
                if c != c1:
                    edgeW = DAO.getEdgeWeight(c,c1)
                    if len(edgeW) > 0:
                        self._grafo.add_edge(c, c1, weight=edgeW[0])

        self._camminoOttimo = []
        self._pesoCamminoOttimo = len(self._camminoOttimo)

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def getArchiEstremi(self):
        edges = self._grafo.edges(data=True)
        print(edges)
        edgesSorted = sorted(edges, key= lambda x: x[2]["weight"], reverse=True)

        return edgesSorted[-1][2]["weight"], edgesSorted[0][2]["weight"]

    def getSopraSottoSoglia(self, soglia):
        cntSotto = 0
        cntSopra = 0
        for edge in self._grafo.edges:
            if self._grafo[edge[0]][edge[1]]["weight"] < soglia:
                cntSotto+=1
            elif self._grafo[edge[0]][edge[1]]["weight"] > soglia:
                cntSopra+=1
        return cntSotto, cntSopra

    def getPercorso(self, soglia):
        self._camminoOttimo = []
        self._pesoCamminoOttimo = 0

        parziale = []
        for n in self._grafo.nodes:
            parziale.append(n)
            self._ricorsione(parziale, soglia)
            parziale.pop()

        res = []
        for i in range(0, len(self._camminoOttimo)-1):
            res.append((self._camminoOttimo[i], self._camminoOttimo[i+1], self._grafo[self._camminoOttimo[i]][self._camminoOttimo[i+1]]["weight"]))

        return self._pesoCamminoOttimo, res


    def _ricorsione(self, parziale, soglia):
        pesoCamminoAttuale = self.calcolaLunghezzaPercorso(parziale)
        if  pesoCamminoAttuale > self._pesoCamminoOttimo:
            self._camminoOttimo = copy.deepcopy(parziale)
            self._pesoCamminoOttimo = pesoCamminoAttuale

        lastNode = parziale[-1]
        for neighbor in self._grafo.neighbors(lastNode):
            if not self.edgeConsiderato(lastNode, neighbor, parziale) and self._grafo[lastNode][neighbor]["weight"] > soglia:
                parziale.append(neighbor)
                self._ricorsione(parziale, soglia)
                parziale.pop()

    def edgeConsiderato(self, n1, n2, listOfNodes):
        for i in range(0, len(listOfNodes)-1):
            if (n1, n2) == (listOfNodes[i], listOfNodes[i+1]):
                return True

    def calcolaLunghezzaPercorso(self, listOfNodes):
        sum = 0
        for i in range(0, len(listOfNodes) - 1):
            sum += self._grafo[listOfNodes[i]][listOfNodes[i+1]]["weight"]

        return sum



if __name__ == "__main__":
    model = Model()

