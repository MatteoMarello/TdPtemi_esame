from Esami.Ufo.quattro_giugno.database.DB_connect import DBConnect
from Esami.Ufo.quattro_giugno.model.state import State

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT year(s.`datetime`) as anno
                        from sighting s 
                        order by anno
                        """
            cursor.execute(query)
            for row in cursor:
                result.append(row["anno"])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getShapesYear(year):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT s.shape 
                        from sighting s 
                        WHERE YEAR (s.`datetime`)=%s
                        order by s.shape 
                            """
            cursor.execute(query, (year,))
            for row in cursor:
                result.append(row["shape"])
            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def getStates():
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
                    where state1 < state2
                            """
            cursor.execute(query)
            for row in cursor:
                s1 = idMap[row["state1"]]
                s2 = idMap[row["state2"]]
                result.append((s1,s2))
            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def getNumeroAvvistamenti(year, shape, s1, s2):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT t1.a1 + t2.a2 as peso
                FROM (
                SELECT count(*) as a1
                FROM sighting s 
                WHERE year(s.`datetime`) = %s and s.shape = %s and s.state = %s ) as t1,
                (SELECT count(*) as a2
                FROM sighting s 
                WHERE year(s.`datetime`) = %s and s.shape = %s and s.state = %s) as t2
                            """
            cursor.execute(query, (year, shape, s1, year, shape, s2))
            for row in cursor:
                if row["peso"]:
                    result.append(row["peso"])
                else:
                    result.append(0)
            cursor.close()
            cnx.close()
            return result[0]