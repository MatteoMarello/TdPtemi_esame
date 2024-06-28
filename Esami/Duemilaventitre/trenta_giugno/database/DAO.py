from Esami.Duemilaventitre.trenta_giugno.database.DB_connect import DBConnect


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
            query = """
                SELECT DISTINCT name 
                FROM teams t 
                order by name ASC
                                                """
            cursor.execute(query)
            for row in cursor:
                result.append(row["name"])
            cursor.close()
            cnx.close()
            return result



    @staticmethod
    def getNodes(team):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT t.`year`  
                from teams t 
                WHERE t.name = %s
                                                """
            cursor.execute(query, (team,))
            for row in cursor:
                result.append(row["year"])
            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def getWeight(firstYear, secondYear, team):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT COUNT(DISTINCT a2.playerID) as peso
                FROM appearances a, teams t, appearances a2 , teams t2 
                WHERE a.teamID = t.ID AND a2.teamID = t2.ID 
                AND t.name = %s AND t2.name = %s 
                AND a2.`year` = %s AND a.`year`= %s
                AND a.playerID = a2.playerID 
                GROUP BY a.`year`, a2.`year`
                                                """
            cursor.execute(query, (team, team, firstYear, secondYear))
            for row in cursor:
                result.append(row["peso"])
            cursor.close()
            cnx.close()
            if result:
                return result[0]
            else:
                return None


