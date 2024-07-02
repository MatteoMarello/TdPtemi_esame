from Esami.Ufo.undici_giugno.database.DB_connect import DBConnect
from Esami.Ufo.undici_giugno.model.state import State

class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getAnniWithAvvistamenti():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT YEAR (s.`datetime`) as anno, count(*) as numAvvistamenti
                        FROM sighting s 
                        group by anno 
                        """
            cursor.execute(query)
            for row in cursor:
                result.append((row["anno"], row["numAvvistamenti"]))
            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def getStati(anno):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT s2.*
                        FROM sighting s, state s2 
                        WHERE YEAR (s.`datetime`) = %s
                        AND s2.id = s.state 
                        """
            cursor.execute(query, (anno,))
            for row in cursor:
                result.append(State(**row))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getEdges(anno, idMap):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.state as s1, s2.state as s2
                    FROM sighting s , sighting s2 
                    WHERE YEAR (s.`datetime`) = %s and YEAR (s2.`datetime`) = %s
                    AND s2.`datetime` > s.`datetime`
                    and s.state != s2.state
                    GROUP BY s.state, s2.state 

                        """
            cursor.execute(query, (anno,anno))
            for row in cursor:
                s1 = idMap[row["s1"].upper()]
                s2 = idMap[row["s2"].upper()]
                result.append((s1,s2))
            cursor.close()
            cnx.close()
            return result