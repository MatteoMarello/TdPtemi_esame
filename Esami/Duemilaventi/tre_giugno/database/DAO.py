from Esami.Duemilaventi.tre_giugno.database.DB_connect import DBConnect
from Esami.Duemilaventi.tre_giugno.model.player import Player

class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getPlayers():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT *
FROM Players p   
                        """
            cursor.execute(query)
            for row in cursor:
                result.append(Player(**row))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getNodes(x, idMap):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT a.PlayerID
                        FROM Actions a 
                        group by a.PlayerID 
                        HAVING AVG(a.Goals) > %s  
                        """
            cursor.execute(query, (x,))
            for row in cursor:
                player = idMap[row["PlayerID"]]
                result.append(player)
            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def getEdge(p1, p2):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT a.PlayerID as p1, a2.PlayerID as p2, sum(a.TimePlayed) as t1, sum(a2.TimePlayed) as t2
                        FROM Actions a , Actions a2 
                        WHERE a.PlayerID = %s and a2.PlayerID = %s
                        and a.Starts = 1 and a2.Starts = 1
                        and a.TeamID != a2.TeamID
                        and a.MatchID = a2.MatchID 
                        group by a.PlayerID, a2.PlayerID           
                        """
            cursor.execute(query, (p1,p2))
            for row in cursor:
                result.append((row["t1"], row["t2"]))
            cursor.close()
            cnx.close()
            return result
