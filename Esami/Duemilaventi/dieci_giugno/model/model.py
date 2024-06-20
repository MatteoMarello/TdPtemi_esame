import networkx as nx

from Esami.Duemilaventi.dieci_giugno.database.DAO import DAO

class Model:
    def __init__(self):
        self.graph = nx.Graph()
        self.actors = DAO.getActors()
        self.idMap = {}
        for a in self.actors:
            self.idMap[a.id] = a


    def getGeneri(self):
        return DAO.getGeneri()

    def buildGraph(self, g):
        self.graph.clear()
        nodes = DAO.getNodes(g)
        self.graph.add_nodes_from(nodes)
        edges = DAO.getEdges(g, self.idMap)
        self.graph.add_weighted_edges_from(edges)


    def getAttoriSimili(self, a):
        connComp = list(nx.node_connected_component(self.graph, a))
        connComp.sort(key=lambda x: x.last_name)
        return connComp


    def getActorsNodes(self):
        return list(self.graph.nodes)


    def getGraphDetails(self):
        return len(self.graph.nodes), len(self.graph.edges)
