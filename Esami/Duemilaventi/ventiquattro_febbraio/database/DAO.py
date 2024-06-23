from Esami.Duemilaventi.ventiquattro_febbraio.database.DB_connect import DBConnect
from Esami.Duemilaventi.ventiquattro_febbraio.model.match import Match
from Esami.Duemilaventi.ventiquattro_febbraio.model.player import Player


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getMatches():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT m.MatchID , t.Name as n1, t.TeamID as t1 , t2.Name as n2, t2.TeamID as t2
                        FROM Matches m, Teams t, Teams t2 
                        WHERE m.TeamHomeID = t.TeamID AND t2.TeamID = m.TeamAwayID 
                        """
            cursor.execute(query)
            for row in cursor:
                result.append(Match(row["MatchID"], row["n1"], row["t1"], row["n2"], row["t2"]))
            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def getPlayers(matchID):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT a.PlayerID , p.Name , ( (a.Assists + a.TotalSuccessfulPassesAll) / a.TimePlayed ) as efficiency, a.TeamID
                    FROM Actions a, Players p 
                    WHERE a.MatchID = %s and p.PlayerID = a.PlayerID  
                    """
            cursor.execute(query, (matchID, ))
            for row in cursor:
                result.append(Player(row["PlayerID"], row["Name"], row["efficiency"], row["TeamID"]))
            cursor.close()
            cnx.close()
            return result
