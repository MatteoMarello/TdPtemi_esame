from Esami.Duemilaventi.dieci_giugno.database.DB_connect import DBConnect
from Esami.Duemilaventi.dieci_giugno.model.actor import Actor

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
            query = """ SELECT DISTINCT mg.genre 
                        FROM movies_genres mg 
                            """
            cursor.execute(query)
            for row in cursor:
                result.append(row['genre'])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getActors():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ 
                    SELECT * FROM actors a  
                                                    """
            cursor.execute(query)
            for row in cursor:
                result.append(Actor(**row))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getNodes(g):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT DISTINCT a.id, a.first_name, a.last_name , a.gender 
                    FROM movies_genres mg , roles r , actors a 
                    WHERE mg.movie_id = r.movie_id 
                    AND a.id = r.actor_id 
                    AND mg.genre = %s  
                                """
            cursor.execute(query, (g,))
            for row in cursor:
                result.append(Actor(**row))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getEdges(g, idMap):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT r.actor_id as a1, r2.actor_id as a2, COUNT(*) as peso 
                FROM roles r, movies_genres mg, roles r2  
                WHERE r.movie_id = mg.movie_id 
                AND mg.genre = %s
                AND r.actor_id < r2.actor_id 
                AND r.movie_id = r2.movie_id 
                GROUP BY r.actor_id, r2.actor_id  
                                                """
            cursor.execute(query, (g,))
            for row in cursor:
                a1 = idMap[row['a1']]
                a2 = idMap[row['a2']]
                result.append( (a1, a2, row['peso']) )
            cursor.close()
            cnx.close()
            return result


