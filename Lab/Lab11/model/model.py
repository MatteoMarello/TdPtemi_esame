import copy

import networkx as nx

from Lab.Lab11.database.DAO import DAO
class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._products = DAO.getProducts()
        self._mapProducts = {}
        for p in self._products:
            self._mapProducts[p.Product_number] = p
        self._solMigliore = 0
        self._camminoMigliore = []

    def buildGraph(self, anno, color):
        self._graph.clear()
        for p in self._products:
            if p.Product_color == color:
                self._graph.add_node(p)

        for node in self._graph.nodes:
            for node2 in self._graph.nodes:
                if node2 != node and not self._graph.has_edge(node,node2):
                    peso = DAO.getEdgeWeight(anno, node.Product_number, node2.Product_number)
                    if peso!=0:
                        self._graph.add_edge(node, node2, weight=peso)

        self._mostWeightEdge = self.getMostWeightEdge()

    def getPercorsoPiuLungo(self, prodottoPartenza):
        self._camminoMigliore = []
        edges=[]
        self._solMigliore = 0
        parziale = [prodottoPartenza]
        for n in self._graph.neighbors(prodottoPartenza):
            parziale.append(n)
            edges.append((prodottoPartenza,n))
            self.ricorsione(parziale, edges)
            parziale.pop()
            edges.pop()

        return self._solMigliore

    def ricorsione(self, parziale, edges):
        if len(edges) > self._solMigliore:
            self._solMigliore = len(edges)

        for product in self._graph.neighbors(parziale[-1]):
            if not self.edgeConsiderato(edges, parziale[-1], product):
                if self._graph[parziale[-1]][product]["weight"] >= self._graph[parziale[-1]][parziale[-2]]["weight"]:
                    edges.append((parziale[-1], product))
                    parziale.append(product)
                    print(edges)
                    self.ricorsione(parziale, edges)
                    edges.pop()
                    parziale.pop()

    def edgeConsiderato(self, edges, nodo1, nodo2):
        if (nodo1, nodo2) in edges or (nodo2, nodo1) in edges:
            return True
        else:
            return False

    def getColors(self):
        colors = DAO.getColors()
        return colors

    def getNumEdges(self):
        return len(self._graph.edges)

    def getNumNodes(self):
        return len(self._graph.nodes)

    def getThreeMostWeight(self):
        edges = self._graph.edges(data=True)
        edges_ordinati = sorted(edges, key=lambda x: x[2]["weight"], reverse=True)
        if len(edges_ordinati) >=3:
            return edges_ordinati[0], edges_ordinati[1], edges_ordinati[2]
        else:
            return None, None, None

    def getMostWeightEdge(self):
        edges = self._graph.edges(data=True)
        edges_ordinati = sorted(edges, key=lambda x: x[2]["weight"], reverse=True)
        if len(edges_ordinati) >= 1:
            return edges_ordinati[0][2]["weight"]
        else:
            return None


if __name__ == "__main__":
    model = Model()
    model.buildGraph(2018, "White")
    print(len(model._graph.nodes))
    print(len(model._graph.edges))
    model.getThreeMostWeight()


