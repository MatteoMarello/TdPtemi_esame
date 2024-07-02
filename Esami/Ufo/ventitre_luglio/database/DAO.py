from Esami.Ufo.ventitre_luglio.database.DB_connect import DBConnect
from Esami.Ufo.ventitre_luglio.model.state import State

class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getStati():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                        FROM state s 
                        """
            cursor.execute(query)
            for row in cursor:
                result.append(State(**row))
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
            query = """SELECT *
                        FROM neighbor n  
                        """
            cursor.execute(query)
            for row in cursor:
                s1 = idMap[row["state1"]]
                s2 = idMap[row["state2"]]
                result.append((s1, s2))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getEdgeWeight(giorni, anno, s1, s2):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT count(*) as peso
                        FROM sighting s , sighting s2 
                        WHERE abs(DATEDIFF(s.`datetime`, s2.`datetime`)) <= %s
                        AND YEAR(s2.`datetime`) = %s and year (s.`datetime`) = %s 
                        AND s.state = %s AND s2.state = %s
                        """
            cursor.execute(query, (giorni, anno, anno, s1, s2))
            for row in cursor:
                if row["peso"]:
                    result.append(row["peso"])
                else:
                    result.append(0)
            cursor.close()
            cnx.close()
            return result[0]