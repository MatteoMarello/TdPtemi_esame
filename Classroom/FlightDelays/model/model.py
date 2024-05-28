import copy
import time

import networkx as nx

from Classroom.FlightDelays.database.DAO import DAO
class Model:
    def __init__(self):
        self._airports = DAO.getAllAirports()
        self._idMap = {}
        for a in self._airports:
            self._idMap[a.ID] = a

        self._grafo = nx.Graph()

        self._bestPath = []
        self._bestObjFun = 0


    def getCamminoOttimo(self, v0, v1, t):
        self._bestPath = []
        self._bestObjFun = 0
        parziale = [v0]

        self.ricorsione(parziale, v1, t)
        return self._bestPath, self._bestObjFun

    def ricorsione(self, parziale, target, t):
        # Verificare che parziale sia una possibile soluzione
        # Verificare se parziale è meglio di best
        # t è il numero di archi, ma dato che in parziale aggiungo i nodi, impongo len(parziale) == t+1 come condizione di terminazione.

        if parziale[-1] == target and self.getObjFun(parziale) > self._bestObjFun:
            self._bestObjFun = self.getObjFun(parziale)
            self._bestPath = copy.deepcopy(parziale)
            return

        if len(parziale) == t + 1:
            # Esco
            return
        # Posso ancora aggiungere nodi
        # Prendo i vicini e provo ad aggiungere
        # Ricorsione
        for n in self._grafo.neighbors(parziale[-1]):
            if n not in parziale:
                parziale.append(n)
                self.ricorsione(parziale, target, t)
                parziale.pop()


    def getObjFun(self, listOfNodes):
        objVal = 0
        for i in range(0, len(listOfNodes)-1):
            objVal += self._grafo[listOfNodes[i]][listOfNodes[i+1]]["weight"]

        return objVal


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


    def esistePercorso(self, v0, v1):
        connComp = nx.node_connected_component(self._grafo, v0)
        return v1 in connComp


    def trovaCamminoDijkstra(self, v0, v1):
        # Dijkstra ci restituisce il cammino ottimo (per quanto riguarda somma dei pesi degli archi) tra un nodo di partenza
        # e un nodo di arrivo
        return nx.dijkstra_path(self._grafo, v0, v1)

    def trovaCamminoBFS(self, v0, v1):
        # BFS ci restituisce il cammino con il numero di archi MINORE per raggiungere un certo nodo. (cammino + BREVE)
        tree = nx.bfs_tree(self._grafo, v0)
        if v1 in tree:
            print(f"{v1} è presente nell'albero di visita BFS")

        path = [v1]
        while path[-1] != v0:
            path.append(list(tree.predecessors(path[-1]))[0])

        path.reverse()

        return path

    def trovaCamminoDFS(self, v0, v1):
        # DFS ci restituisce il cammino con il numero di archi MAGGIORE per raggiungere un certo nodo. (cammino + LUNGO)
        tree = nx.dfs_tree(self._grafo, v0)
        if v1 in tree:
            print(f"{v1} è presente nell'albero di visita DFS")

        path = [v1]
        while path[-1] != v0:
            path.append(list(tree.predecessors(path[-1]))[0])

        path.reverse()

        return path



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

    v0 = model.getAllNodes()[0]
    connessa = list(nx.node_connected_component(model._grafo, v0))
    v1 = connessa[10]

    pathD = model.trovaCamminoDijkstra(v0,v1)
    pathBFS = model.trovaCamminoBFS(v0,v1)
    pathDFS = model.trovaCamminoDFS(v0,v1)

    print("Dijkstra:")
    print(*pathD, sep=" \n")
    print('-------------------')
    print("BFS:")
    print(*pathBFS, sep=" \n")
    print('-------------------')
    print("DFS:")
    print(*pathDFS, sep=" \n")
    print('-------------------')
    print("RICORSIONE:")
    tic = time.time()
    bestPath, bestScore = model.getCamminoOttimo(v0, v1, 4)
    tac = time.time()
    print(f"Cammino ottimo ha peso = {bestScore}. Trovato in {tac-tic} secondi")
    print(*bestPath, sep=" \n")