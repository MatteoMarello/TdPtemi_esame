from Classroom.iTunes.database.DB_connect import DBConnect
from Classroom.iTunes.model.album import Album

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
            query = """ SELECT a.AlbumId , a.Title, a.ArtistId, SUM(t.Milliseconds) as totD 
                        FROM album a , track t 
                        WHERE a.AlbumId = t.AlbumId 
                        GROUP BY a.AlbumId 
                        HAVING totD > %s"""
            cursor.execute(query, (d,))
            for row in cursor:
                result.append(Album(**row))
            cursor.close()
            cnx.close()
            return result
