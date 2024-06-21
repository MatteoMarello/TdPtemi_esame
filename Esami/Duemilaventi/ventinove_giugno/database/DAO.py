from Esami.Duemilaventi.ventinove_giugno.database.DB_connect import DBConnect
from Esami.Duemilaventi.ventinove_giugno.model.director import Director

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getDirectors(year):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT  d.id , d.first_name , d.last_name
                        FROM movies m , directors d , movies_directors md 
                        WHERE m.`year` = %s
                        AND md.movie_id = m.id AND md.director_id = d.id 
                        """
            cursor.execute(query, (year,))
            for row in cursor:
                result.append(Director(**row))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getEdges(year, idMap):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT md.director_id as d1, md2.director_id as d2, COUNT(DISTINCT r2.actor_id) as weight
                        FROM movies_directors md , roles r , roles r2 , movies_directors md2, movies m , movies m2 
                        WHERE r.movie_id = md.movie_id AND md2.movie_id = r2.movie_id 
                        AND md.director_id < md2.director_id AND r2.actor_id = r.actor_id
                        and m.id = md.movie_id and md2.movie_id = m2.id 
                        AND m2.`year` = %s and m.`year`= %s
                        GROUP BY md.director_id, md2.director_id
                        """
            cursor.execute(query, (year,year))
            for row in cursor:
                d1 = idMap[row["d1"]]
                d2 = idMap[row["d2"]]
                result.append((d1, d2, row["weight"]))
            cursor.close()
            cnx.close()
            return result
