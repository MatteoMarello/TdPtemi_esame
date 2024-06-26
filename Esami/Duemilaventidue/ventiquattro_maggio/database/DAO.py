from Esami.Duemilaventidue.ventiquattro_maggio.database.DB_connect import DBConnect
from Esami.Duemilaventidue.ventiquattro_maggio.model.track import Track

class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getGeneri():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT g.Name 
                        FROM genre g 
                        order by Name 
                        """
            cursor.execute(query)
            for row in cursor:
                result.append(row["Name"])
            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def getNodes(g):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT t.*
                        FROM track t , genre g 
                        WHERE t.GenreId = g.GenreId 
                        AND g.Name = %s
                        """
            cursor.execute(query, (g,))
            for row in cursor:
                result.append(Track(**row))
            cursor.close()
            cnx.close()
            return result

