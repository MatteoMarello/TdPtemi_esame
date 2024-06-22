from Esami.Duemilaventi.quattordici_luglio.database.DB_connect import DBConnect
from Esami.Duemilaventi.quattordici_luglio.model.team import Team

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getTeams():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT *
                        FROM Teams t 
                            """
            cursor.execute(query)
            for row in cursor:
                result.append(Team(**row))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getMatches():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT m.TeamHomeID , m.TeamAwayID , m.ResultOfTeamHome 
                        FROM Matches m 
                            """
            cursor.execute(query)
            for row in cursor:
                result.append((row["TeamHomeID"], row["TeamAwayID"], row["ResultOfTeamHome"]))
            cursor.close()
            cnx.close()
            return result
