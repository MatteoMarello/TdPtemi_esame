import networkx as nx
from Lab.Lab10.database.DAO import DAO
class Model:

    def __init__(self):
        self._countries = DAO.getAllCountries()
        self._idMap = {}
        for country in self._countries:
            self._idMap[country.CCode] = country



    def creaGrafo(self, anno):
        self._graph = nx.Graph()

        countriesExistingNumbers = DAO.getCountriesExisting(anno)
        for countryNumber in countriesExistingNumbers:
            self._graph.add_node(self._idMap[countryNumber])

        countriesExistingContiguities = DAO.getContiguitiesExisting(anno)
        for countries in countriesExistingContiguities:
            firstCountry = self._idMap[countries[0]]
            secondCountry = self._idMap[countries[1]]
            self._graph.add_edge(firstCountry, secondCountry)

    def calcolaDettagliNodi(self):
        res = []
        for country in self._graph.nodes:
            res.append((country, self._graph.degree[country]))
        return res

    def getCountries(self):
        return self._graph.nodes

    def getNumConnectedComp(self):
        return nx.number_connected_components(self._graph)

if __name__ == "__main__":
    model = Model()
    model.creaGrafo(1980)
    print(len(model._graph.nodes))
    print(len(model._graph.edges))
    model.calcolaDettagliNodi()
