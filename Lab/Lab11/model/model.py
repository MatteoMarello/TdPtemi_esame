import networkx as nx

from Lab.Lab11.database.DAO import DAO
class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._products = DAO.getProducts()
        self._mapProducts = {}
        for p in self._products:
            self._mapProducts[p.Product_number] = p

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
        return edges_ordinati[0], edges_ordinati[1], edges_ordinati[2]




if __name__ == "__main__":
    model = Model()
    model.buildGraph(2018, "White")
    print(len(model._graph.nodes))
    print(len(model._graph.edges))
    model.getThreeMostWeight()

