from Esami.Duemilaventidue.ventinove_giugno.database.DB_connect import DBConnect
from Esami.Duemilaventidue.ventinove_giugno.model.album import Album

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAlbums(n):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT a.AlbumId , a.Title , a.ArtistId, COUNT(DISTINCT t.TrackId) as nCanzoni 
                        FROM track t, album a 
                        WHERE t.AlbumId = a.AlbumId 
                        GROUP BY a.AlbumId , a.Title , a.ArtistId 
                        HAVING nCanzoni > %s
                        """
            cursor.execute(query, (n,))
            for row in cursor:
                result.append(Album(**row))
            cursor.close()
            cnx.close()
            return result
