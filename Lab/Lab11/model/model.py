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
        self._solMigliore = 0
        parziale = [prodottoPartenza]
        for n in self._graph.neighbors(prodottoPartenza):
            parziale.append(n)
            self.ricorsione(parziale)
            parziale.pop()
        return self._solMigliore

    def ricorsione(self, parziale):
        if len(parziale) > self._solMigliore:
            self._solMigliore = len(parziale)

        if self._graph[parziale[-1]][parziale[-2]]["weight"] == self._mostWeightEdge:
            return

        for product in self._graph.neighbors(parziale[-1]):
            if product not in parziale\
            and self._graph[parziale[-1]][product]["weight"] >= self._graph[parziale[-1]][parziale[-2]]["weight"]:
                parziale.append(product)
                self.ricorsione(parziale)
                parziale.pop()


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


