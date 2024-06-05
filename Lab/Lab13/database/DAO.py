from Lab.Lab13.database.DB_connect import DBConnect
from Lab.Lab13.model.state import Stato

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getYears():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ select distinct year (s.`datetime`) as anno
                        from sighting s 
                        order by year (s.`datetime`) asc """
            cursor.execute(query)
            for row in cursor:
                result.append(row["anno"])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getShapes():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ select distinct (s.shape) as shape
                        from sighting s 
                        order by shape asc 
                        """
            cursor.execute(query)
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
            query = """ select *
                        from state s  
                        """
            cursor.execute(query)
            for row in cursor:
                result.append(Stato(**row))
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
            query = """ select distinct  *
                        from neighbor n
                        where state1 < state2
                        order by state1 
                        """
            cursor.execute(query)
            for row in cursor:
                result.append( (idMap[row["state1"]], idMap[row["state2"]]) )
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getNumAvvistamenti(s, year, shape):
        result = ""
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ select count(*) as peso 
                        from sighting s 
                        where s.state = %s
                        and year (s.`datetime`) = %s
                        and s.shape = %s
                        group by s.state
                                                """
            cursor.execute(query, (s, year, shape))
            for row in cursor:
                result = row["peso"]

            cursor.close()
            cnx.close()
            return result



if __name__ == "__main__":
    dao = DAO()


