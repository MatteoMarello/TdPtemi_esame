import networkx as nx

from Esami.Duemilaventuno.uno_giugno.database.DAO import DAO
class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._essentialGenes = DAO.getEssentialGenes()


    def buildGraph(self):
        self._essentialGenes.sort()
        self._graph.add_nodes_from(self._essentialGenes)
        edges = DAO.getEdges()
        self._graph.add_edges_from(edges)

        for edge in self._graph.edges:
            g1 = edge[0]
            g2 = edge[1]
            tupleEdgeW = DAO.getEdgeWeight(g1, g2)
            if not tupleEdgeW:
                tupleEdgeW = DAO.getEdgeWeight(g2,g1)
            c1 = tupleEdgeW[0][1]
            c2 = tupleEdgeW[0][2]
            edgeW = tupleEdgeW[0][0]
            if c1 == c2:
                if edgeW > 0:
                    self._graph[g1][g2]["weight"] = 2 * edgeW
                else:
                    self._graph[g1][g2]["weight"] = -2 * edgeW
            else:
                if edgeW > 0:
                    self._graph[g1][g2]["weight"] = edgeW
                else:
                    self._graph[g1][g2]["weight"] = -1 * edgeW



    def getGeniAdiacenti(self, gene):
        res = []
        for neighbor in self._graph.neighbors(gene):
            res.append((neighbor, self._graph[gene][neighbor]["weight"]))

        res.sort(key=lambda g: g[1], reverse=True)
        return res


    def getGenes(self):
        return self._essentialGenes

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)
