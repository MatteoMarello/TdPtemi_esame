import networkx as nx

from Esami.Duemilaventitre.trenta_maggio.database.DAO import DAO
class Model:
    def __init__(self):
        self._countries = DAO.getNations()
        self._graph = nx.Graph()

    def buildGraph(self, anno, nazione, m):
        self._graph.clear()
        retailers = DAO.getRetailers(nazione)
        self._idMap = {r.Retailer_code: r for r in retailers}
        self._graph.add_nodes_from(retailers)
        edges = DAO.getEdges(anno,nazione,m, self._idMap)
        self._graph.add_weighted_edges_from(edges)


    def analizzaGrafo(self, retailer):
        tot = 0
        connComp = list(nx.node_connected_component(self._graph,retailer))
        for i in range(0, len(connComp)):
            r1 = connComp[i]
            for j in range(i + 1, len(connComp)):
                r2 = connComp[j]
                if self._graph.has_edge(r1,r2):
                    tot+=self._graph[r1][r2]["weight"]


        return len(connComp), tot


    def getNodes(self):
        nodes = list(self._graph.nodes)
        nodes.sort(key=lambda x: x.Retailer_name)
        return nodes

    def getEdges(self):
        edges = list(self._graph.edges(data=True))
        edges.sort(key=lambda x: x[2]["weight"])
        return edges



    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getCountries(self):
        return self._countries