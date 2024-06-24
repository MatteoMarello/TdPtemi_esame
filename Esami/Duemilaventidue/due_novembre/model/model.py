import copy

import networkx as nx

from Esami.Duemilaventidue.due_novembre.database.DAO import DAO
class Model:
    def __init__(self):
        self._generi = DAO.getGeneri()
        self._graph = nx.Graph()

        self._tracks = DAO.getAllTracks()
        self._idMap = {t.TrackId : t for t in self._tracks}
        self._playlist = []


    def buildGraph(self, genere, dMin, dMax):
        self._graph.clear()
        tracks = DAO.getTrack(genere, dMin, dMax)
        self._graph.add_nodes_from(tracks)
        edges = DAO.getEdges(genere, dMin, dMax, self._idMap)
        self._graph.add_edges_from(edges)

        connComp = list(nx.connected_components(self._graph))
        res = []
        for comp in connComp:
            track = list(comp)[0]
            nPlaylist = DAO.getNPlaylistTrack(track.TrackId)
            res.append((len(comp), nPlaylist))

        res.sort(key=lambda x: x[0], reverse=True)
        return res


    def getPlaylist(self, dTOT):
        self._playlist = []
        setOfNodes = self.getBestConnComp()
        parziale = []
        firstTrack = self.getTrackMinimumDuration(setOfNodes)
        parziale.append(firstTrack)

        self._ricorsione(parziale, dTOT, setOfNodes)

        return self._playlist, self._calcolaDurataPlaylist(self._playlist) / 1000

    def _ricorsione(self, parziale, dTOT, setOfNodes):

        durataPlaylist = self._calcolaDurataPlaylist(parziale)
        if durataPlaylist > dTOT:
            return

        if len(parziale) > len(self._playlist):
            self._playlist = copy.deepcopy(parziale)

        sortedTracks = self.getSortedTracks(setOfNodes)
        for track in sortedTracks:
            if track not in parziale:
                parziale.append(track)
                self._ricorsione(parziale, dTOT, setOfNodes)
                parziale.pop()
                return

    def getTrackMinimumDuration(self, tracks):
        tracks.sort(key=lambda x: x.Milliseconds)
        return tracks[0]

    def getSortedTracks(self, tracks):
        tracks.sort(key=lambda x: x.Milliseconds)
        return tracks



    def _calcolaDurataPlaylist(self, listOfTracks):
        tot = 0
        for t in listOfTracks:
            tot += t.Milliseconds
        return tot


    def getBestConnComp(self):
        connComp = list(nx.connected_components(self._graph))
        res = []
        for comp in connComp:
            track = list(comp)[0]
            nPlaylist = DAO.getNPlaylistTrack(track.TrackId)
            res.append((comp, nPlaylist))

        res.sort(key=lambda x: len(x[0]), reverse=True)
        return list(res[0][0])

    def graphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getGeneri(self):
        return self._generi