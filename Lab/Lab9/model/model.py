from Lab.Lab9.database.DAO import DAO
import networkx as nx
class Model:
    def __init__(self):
        self._airports = DAO.getAllAirports()
        self._airportsMap = {}
        for a in self._airports:
            self._airportsMap[a.id] = a


    def buildGraph(self):
        self._graphAirports = nx.Graph()
        for airport in self._airportsMap.values():
            self._graphAirports.add_node(airport)


if __name__ == "__main__":
    model = Model()
    model.buildGraph()
