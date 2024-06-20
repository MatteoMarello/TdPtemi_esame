import copy

import networkx as nx
from Esami.Duemilaventi.quattro_settembre.database.DAO import DAO

class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self.movies = DAO.getMoviesWithRank()
        self.idMap = {}
        for m in self.movies:
            self.idMap[m.id] = m
        self._bestPath = []

    # First version, with list --> no efficiency
    def buildGraph(self, rank):
        self._grafo.clear()
        moviesWithRank = DAO.getMoviesWithRank()
        self._grafo.add_nodes_from(moviesWithRank)

        for m in self._grafo.nodes:
            for m2 in self._grafo.nodes:
                if m != m2:
                    if not self._grafo.has_edge(m, m2):
                        if m.rank >= rank and m2.rank >= rank:
                            a = DAO.getActorsFilm(m.id)
                            a2 = DAO.getActorsFilm(m2.id)
                            if self.has_common_element(a,a2):
                                self._grafo.add_edge(m, m2, weight=0)

                            if self._grafo.has_edge(m,m2):
                                for cnt in a:
                                    self._grafo[m][m2]["weight"] += 1
                                for actor2 in a2:
                                    if actor2 not in a:
                                        self._grafo[m][m2]["weight"] += 1

    # V2, with sets --> more efficiency
    def buildGraphV2(self, rank):
        self._grafo.clear()
        moviesWithRank = DAO.getMoviesWithRank()
        self._grafo.add_nodes_from(moviesWithRank)

        # Caching gli attori per ogni film
        movie_actors = {m.id: set(DAO.getActorsFilm(m.id)) for m in self._grafo.nodes}

        nodes_list = list(self._grafo.nodes)
        for i in range(len(nodes_list)):
            m = nodes_list[i]
            if m.rank < rank:
                continue
            for j in range(i + 1, len(nodes_list)):
                m2 = nodes_list[j]
                if m2.rank < rank:
                    continue

                actors_m = movie_actors[m.id]
                actors_m2 = movie_actors[m2.id]
                common_actors = actors_m & actors_m2

                if common_actors:
                    # Aggiungi l'arco con peso iniziale 0
                    self._grafo.add_edge(m, m2, weight=0)

                    # Calcola il peso dell'arco
                    self._grafo[m][m2]["weight"] = len(common_actors)

                    # Incrementa il peso per ogni attore comune

    # Metodo per verificare elementi comuni utilizzando set
    def has_common_element(self, set1, set2):
        return bool(set1 & set2)


    #Third version --> with a bigger query
    def buildGraphV3(self, rank):
        self._grafo.clear()
        moviesWithRank = DAO.getMoviesWithRank()
        self._grafo.add_nodes_from(moviesWithRank)
        edges = DAO.getEdges(rank, self.idMap)
        self._grafo.add_weighted_edges_from(edges)

    def getFilms(self):
        return list(self._grafo.nodes)

    def getFilmGradoMax(self):
        res = []
        for n in self._grafo.nodes:
            cnt = 0
            for neighbor in self._grafo.neighbors(n):
                cnt+=self._grafo[n][neighbor]['weight']
            res.append((n,cnt))

        res.sort(key=lambda x: x[1], reverse=True)
        film = res[0][0]
        grado = res[0][1]
        return film, grado

    def getCammino(self, film):
        self._bestPath = []
        parziale = [film]
        for n in self._grafo.neighbors(film):
            parziale.append(n)
            self._ricorsione(parziale)
            parziale.pop()

        res = []
        for i in range(0, len(self._bestPath)-1):
            res.append((self._bestPath[i], self._bestPath[i+1], self._grafo[self._bestPath[i]][self._bestPath[i+1]]["weight"]))

        return res

    def _ricorsione(self, parziale):
        if len(parziale) > len(self._bestPath):
            self._bestPath = copy.deepcopy(parziale)

        lastEdgeW = self._grafo[parziale[-2]][parziale[-1]]['weight']
        lastNode = parziale[-1]
        for neigbor in self._grafo.neighbors(lastNode):
            if self._grafo[lastNode][neigbor]["weight"] > lastEdgeW and neigbor not in parziale:
                parziale.append(neigbor)
                self._ricorsione(parziale)
                parziale.pop()


    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)
