from Esami.Duemilaventidue.due_novembre.database.DB_connect import DBConnect
from Esami.Duemilaventidue.due_novembre.model.track import Track

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getGeneri():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT Name 
                        FROM genre g 
                        order by Name ASC  

                                                """
            cursor.execute(query)
            for row in cursor:
                result.append(row["Name"])
            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def getTrack(genere, dMin, dMax):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT t.*
                        FROM track t, genre g 
                        WHERE t.GenreId = g.GenreId 
                        AND g.Name = %s 
                        AND t.Milliseconds >= %s
                        AND t.Milliseconds <= %s 

                                                """
            cursor.execute(query, (genere, dMin, dMax))
            for row in cursor:
                result.append(Track(**row))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getAllTracks():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT *
                FROM track t

                                                """
            cursor.execute(query)
            for row in cursor:
                result.append(Track(**row))
            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def getEdges(genere, dMin, dMax, idMap):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT table1.t1, table2.t2
                FROM (SELECT t.TrackId as t1, COUNT(DISTINCT p.PlaylistId) as nPlaylist1
                FROM track t, genre g, playlisttrack p
                WHERE t.GenreId = g.GenreId 
                AND t.TrackId = p.TrackId 
                AND g.Name = %s 
                AND t.Milliseconds >= %s
                AND t.Milliseconds <= %s
                GROUP BY t.TrackId) as table1, 
                (SELECT t2.TrackId as t2, COUNT(DISTINCT p2.PlaylistId) as nPlaylist2
                FROM track t2, genre g2, playlisttrack p2
                WHERE t2.GenreId  = g2.GenreId 
                AND t2.TrackId = p2.TrackId  AND g2.Name = %s 
                AND t2.Milliseconds >= %s AND t2.Milliseconds <= %s
                GROUP BY t2.TrackId) as table2
                WHERE table1.t1 < table2.t2 AND table1.nPlaylist1 = table2.nPlaylist2

                                                """
            cursor.execute(query, (genere, dMin, dMax, genere, dMin, dMax))
            for row in cursor:
                track1 = idMap[row["t1"]]
                track2 = idMap[row["t2"]]
                result.append((track1, track2))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getNPlaylistTrack(TrackId):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT COUNT(DISTINCT p.PlaylistId) as nPlaylist
                    FROM track t, playlisttrack p 
                    WHERE t.TrackId = %s
                    AND t.TrackId = p.TrackId 

                

                                                """
            cursor.execute(query, (TrackId,))
            for row in cursor:
                result.append(row["nPlaylist"])
            cursor.close()
            cnx.close()
            return result[0]
