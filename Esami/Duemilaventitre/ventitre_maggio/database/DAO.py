from Esami.Duemilaventitre.ventitre_maggio.database.DB_connect import DBConnect
from Esami.Duemilaventitre.ventitre_maggio.model.player import Player

class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getAnni():
        cnx = DBConnect.get_connection()
        result = set()
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT DISTINCT s.`year` 
                FROM salaries s  

                                                """
            cursor.execute(query)
            for row in cursor:
                result.add(row["year"])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getPlayers(anno, salario):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT DISTINCT p.*, s.salary
                FROM salaries s, people p 
                WHERE s.`year` = %s
                AND p.playerID = s.playerID 
                AND s.salary > %s

                                                """
            cursor.execute(query, (anno,salario))
            for row in cursor:
                result.append(Player(**row))
            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def getEdges(anno, salario, idMap):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
            SELECT a.playerID as p1, a2.playerID as p2
            FROM appearances a, appearances a2, salaries s, salaries s2 
            WHERE a.`year` = %s
            AND s.playerID = a.playerID AND s.salary > %s
            AND s2.playerID = a2.playerID and s2.salary > %s
            AND s.`year`= %s and s2.`year` = %s
            AND a2.`year` = %s
            AND a2.teamID = a.teamID
            AND a.playerID < a2.playerID
            GROUP BY a.playerID, a2.playerID 

                                                """
            cursor.execute(query, (anno, salario, salario, anno, anno, anno))
            for row in cursor:
                p1 = idMap[row["p1"]]
                p2 = idMap[row["p2"]]
                result.append((p1, p2))
            cursor.close()
            cnx.close()
            return result


