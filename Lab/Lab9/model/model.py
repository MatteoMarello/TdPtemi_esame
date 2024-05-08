from Lab.Lab9.database.DAO import DAO
import networkx as nx
class Model:
    def __init__(self):
        self._airports = DAO.getAllAirports()
        self._airportsMap = {}
        for a in self._airports:
            self._airportsMap[a.id] = a


    def buildGraph(self, distanza_min):
        self._graphAirports = nx.Graph()
        for airport in self._airportsMap.values():
            self._graphAirports.add_node(airport)

        flights = DAO.getFlights()

        for volo in flights:
            if volo['distanza_media'] >= distanza_min:
                airportU = self._airportsMap[volo['ORIGIN_AIRPORT_ID']]
                airportV = self._airportsMap[volo['DESTINATION_AIRPORT_ID']]

                if not self._graphAirports.has_edge(airportU, airportV):
                    self._graphAirports.add_edge(airportU, airportV, distanza=volo['distanza_media'])

        return self._graphAirports



if __name__ == "__main__":
    model = Model()
    graph: nx.Graph = model.buildGraph(300)
    print(graph)
    for edge in graph.edges:
        print(edge[0])

