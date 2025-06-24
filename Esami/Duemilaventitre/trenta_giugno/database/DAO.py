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
            query = """select distinct t.name as name,  t.teamCode as ID
from lahmansbaseballdb.teams t 
group by name
order by t.name
                 """
            cursor.execute(query)
            for row in cursor:
                result.append((row["ID"], row["name"]))
            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def getNodi(id):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select t.year , a.playerID
from lahmansbaseballdb.teams t , lahmansbaseballdb.appearances a 
where t.teamCode = %s and a.teamCode=t.teamCode 
group by t.year, a.playerID """
            cursor.execute(query,(id,))
            for row in cursor:
                result.append((row["year"], row["playerID"]))
            cursor.close()
            cnx.close()
            return result



















if __name__ == "__main__":
    DAO = DAO()
    nodi = DAO.getNodi("PH1")
    setanni = set()
    for nodo in nodi:
        setanni.add(nodo[0])
    print(len(setanni))
    print(len(nodi))
