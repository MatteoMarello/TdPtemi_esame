from Esami.Genes.trenta_giugno.database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getLocalizzazioni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT Localization 
FROM classification 
order by Localization  
                        """
            cursor.execute(query)
            for row in cursor:
                result.append(row["Localization"])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getEdges():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT c.Localization as l1, c2.Localization as l2
FROM interactions i, classification c , classification c2 
WHERE i.GeneID1 = c2.GeneID and i.GeneID2 = c.GeneID
and c.Localization != c2.Localization
                            """
            cursor.execute(query)
            for row in cursor:
                result.append((row["l1"], row["l2"]))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getEdgeWeight(l1, l2):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT COUNT(DISTINCT i.`Type`) as peso
FROM interactions i, classification c , classification c2 
WHERE i.GeneID1 = c2.GeneID and i.GeneID2 = c.GeneID
and ((c.Localization = %s and c2.Localization = %s) or (c.Localization = %s and c2.Localization=%s)) 

                            """
            cursor.execute(query, (l1,l2,l2,l1))
            for row in cursor:
                result.append(row["peso"])
            cursor.close()
            cnx.close()
            if not result:
                return 0
            else:
                return result[0]