import networkx as nx

from Classroom.FlightDelays.database.DAO import DAO
class Model:
    def __init__(self):
        self._airports = DAO.getAllAirports()
        self._idMap = {}
        for a in self._airports:
            self._idMap[a.ID] = a

        self._grafo = nx.Graph()


    def buildGraph(self, nMin):
        self._nodi = DAO.getAllNodes(nMin, self._idMap)
        self._grafo.add_nodes_from(self._nodi)
        self.addEdgesV2()



    def addEdgesV1(self):
        allConnessioni = DAO.getAllEdgesV1(self._idMap)
        for c in allConnessioni:
            v0 = c.v0
            v1 = c.v1
            peso = c.N
            if v0 in self._grafo and v1 in self._grafo:
                if self._grafo.has_edge(c.v0, c.v1):
                    self._grafo[v0][v1]["weight"] += peso
                else:
                    self._grafo.add_edge(v0,v1,weight=peso)

    def addEdgesV2(self):
        allConnessioni = DAO.getAllEdgesV2(self._idMap)
        for c in allConnessioni:
            v0 = c.v0
            v1 = c.v1
            peso = c.N
            if v0 in self._grafo and v1 in self._grafo:
                self._grafo.add_edge(v0, v1, weight=peso)


    def getSortedVicini(self, v0):
        vicini = self._grafo.neighbors(v0)
        viciniTuple = []
        for v in vicini:
            # viciniTuple sarà una lista di tuple del tipo oggetto - numero, dove l'oggetto è l'aeroporto e il numero e il peso
            # dell'arco tra v0, ricevuto in input, e v.
            viciniTuple.append((v, self._grafo[v0][v]["weight"]))

        viciniTuple.sort(key=lambda x: x[1], reverse=True)
        return viciniTuple


    def printGraphDetails(self):
        print(f"Il grafo ha {len(self._grafo.nodes)} nodi e {len(self._grafo.edges)} archi.")


    def getNumNodi(self):
        return len(self._grafo.nodes)
    def getNumArchi(self):
        return len(self._grafo.edges)

    def getAllNodes(self):
        return self._nodi


if __name__ == "__main__":
    model=Model()
    model.buildGraph(5)
    model.printGraphDetails()
