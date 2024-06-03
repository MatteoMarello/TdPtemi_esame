import networkx as nx
from Classroom.iTunes.database.DAO import DAO

class Model:
    def __init__(self):
        self.graph = nx.Graph()

    def buildGraph(self, d):
        self.graph.clear()
        self.graph.add_nodes_from(DAO.getAlbums(d))


    def getGraphDetails(self):
        return len(self.graph.nodes), len(self.graph.edges)

if __name__ == "__main__":
    mymodel = Model()
    mymodel.buildGraph(120*60*1000)
    print(mymodel.getGraphDetails())
