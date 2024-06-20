from Esami.Duemilaventi.quattro_settembre.database.DB_connect import DBConnect
from Esami.Duemilaventi.quattro_settembre.model.movie import Movie

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getMoviesWithRank():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                    FROM movies m 
                    where m.`rank` IS NOT NULL 
                    
                                                """
            cursor.execute(query)
            for row in cursor:
                result.append(Movie(**row))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getActorsFilm(idFilm):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT r.actor_id  
                        FROM movies m , roles r
                        WHERE m.id = r.movie_id 
                        AND m.id = %s
                                                """
            cursor.execute(query, (idFilm,))
            for row in cursor:
                result.append(row['actor_id'])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getEdges(rank, idMap):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT m.id as m1, m2.id as m2, COUNT(r2.actor_id) as peso 
FROM movies m , roles r, movies m2 , roles r2 
WHERE m.`rank` >= %s AND m2.`rank` >= %s
AND m.id = r.movie_id  AND m2.id = r2.movie_id 
AND m.id < m2.id 
AND r2.actor_id = r.actor_id
GROUP BY m.id, m2.id
HAVING COUNT(r2.actor_id) > 0 
                                                """
            cursor.execute(query, (rank,rank))
            for row in cursor:
                m1 = idMap[row["m1"]]
                m2 = idMap[row["m2"]]
                result.append((m1,m2,row["peso"]))
            cursor.close()
            cnx.close()
            return result


