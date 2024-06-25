from Esami.Duemilaventidue.quattordici_settembre.database.DB_connect import DBConnect
from Esami.Duemilaventidue.quattordici_settembre.model.album import Album

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAlbums(d):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                    SELECT a.*, SUM(t.Milliseconds) as durata 
                    FROM track t , album a 
                    WHERE t.AlbumId = a.AlbumId 
                    GROUP BY a.AlbumId , a.Title , a.ArtistId 
                    HAVING SUM(t.Milliseconds) >= %s 
                                                """
            cursor.execute(query, (d,))
            for row in cursor:
                result.append(Album(**row))
            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def getEdges(idMap):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                    SELECT DISTINCT t.AlbumId as a1, t2.AlbumId as a2
                    FROM playlisttrack p , track t , playlisttrack p2 , track t2 
                    WHERE p.TrackId = t.TrackId 
                    AND p2.TrackId = t2.TrackId 
                    AND p.PlaylistId = p2.PlaylistId 
                    AND t.AlbumId < t2.AlbumId 
                                                """
            cursor.execute(query)
            for row in cursor:
                if row["a1"] in idMap and row["a2"] in idMap:
                    result.append((idMap[row["a1"]], idMap[row["a2"]]))
            cursor.close()
            cnx.close()
            return result