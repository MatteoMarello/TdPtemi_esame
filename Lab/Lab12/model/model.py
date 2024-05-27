import copy

import networkx as nx

from Lab.Lab12.database.DAO import DAO
class Model:
    def __init__(self):
        self.countries = None
        self.graph = nx.Graph()
        self.retailers = DAO.getRetailers()
        self.idMap = {}
        for r in self.retailers:
            self.idMap[r.Retailer_code] = r
        self.bestWeight = 0
        self.bestPath = []


    def getCountries(self):
        self.countries = DAO.getCountries()
        return self.countries

    def createGraph(self, year, country):
        self.graph.clear()
        for r in self.retailers:
            if r.Country == country:
                self.graph.add_node(r)

        edges = DAO.getEdges(year, country, self.idMap)
        for edge in edges:
            self.graph.add_edge(edge.r1, edge.r2, weight=edge.peso)

        return self.getNumNodi(), self.getNumArchi()


    def getVolumi(self):
        res = []
        for r in self.graph.nodes:
            volume = 0
            for n in self.graph.neighbors(r):
                volume += self.graph[r][n]["weight"]

            res.append((r, volume))

        res.sort(key=lambda x: x[1], reverse=True)

        return res

    def getPercorso(self, l):
        self.bestWeight = 0
        self.bestPath.clear()
        edges = []
        nodes = []
        for n in self.graph.nodes:
            nodes.append(n)
            self.ricorsione(l, nodes, edges)
            nodes.pop()

        print(self.bestPath)
        print(self.bestWeight)
        for edge in self.bestPath:
            print(f"{edge[0]} --> {edge[1]}, peso: {self.graph[edge[0]][edge[1]]["weight"]}")


    def ricorsione(self, l, nodes, edges):
        if len(edges) == l:
            if nodes[0] != nodes[-1]:
                return
            else:
                peso = self.getWeightEdges(edges)
                if peso > self.bestWeight:
                    self.bestWeight = peso
                    self.bestPath = copy.deepcopy(edges)

        else:
            current_node = nodes[-1]
            for neighbor in self.graph.neighbors(current_node):
                if self.controllo(neighbor, nodes, edges, l):
                    edges.append((current_node, neighbor))
                    nodes.append(neighbor)
                    self.ricorsione(l, nodes, edges)
                    nodes.pop()
                    edges.pop()


    def controllo(self, n, nodes, edges, l):
        if len(edges) < l-1:
            if n in nodes:
                return False

        elif len(edges) == l-1:
            if n != nodes[0]:
                return False

        return True

    def getWeightEdges(self, edges):
        weight = 0
        for edge in edges:
            weight += self.graph[edge[0]][edge[1]]["weight"]

        return weight


    def getNumNodi(self):
        return len(self.graph.nodes)

    def getNumArchi(self):
        return len(self.graph.edges)


if __name__ == "__main__":
    model = Model()
    model.getCountries()
    edges = model.createGraph(2017, "France")
    print(edges)