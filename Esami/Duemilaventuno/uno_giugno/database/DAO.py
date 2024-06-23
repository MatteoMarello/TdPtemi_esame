from Esami.Duemilaventuno.uno_giugno.database.DB_connect import DBConnect
from Esami.Duemilaventuno.uno_giugno.model.gene import Gene

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getEssentialGenes():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT g.GeneID
                        FROM genes g 
                        WHERE g.Essential = 'Essential' 
                        """
            cursor.execute(query)
            for row in cursor:
                result.append(row["GeneID"])
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
            query = """SELECT DISTINCT i.GeneID1, i.GeneID2
                        FROM interactions i , genes g , genes g2 
                        WHERE i.GeneID1 != i.GeneID2 
                        and g2.GeneID = i.GeneID2 
                        AND g.GeneID = i.GeneID1 
                        and g2.Essential = 'Essential' 
                        and g.Essential = 'Essential'  
                                                """
            cursor.execute(query)
            for row in cursor:
                result.append((row["GeneID1"], row["GeneID2"]))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getEdgeWeight(g1, g2):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT i.Expression_Corr , g.Chromosome as c1, g2.Chromosome as c2
                    FROM interactions i, genes g , genes g2 
                    WHERE i.GeneID1 = %s and i.GeneID2 = %s
                    AND i.GeneID1 = g.GeneID and g2.GeneID = i.GeneID2 
                                                """
            cursor.execute(query, (g1,g2))
            for row in cursor:
                result.append((row["Expression_Corr"], row['c1'], row['c2']))
            cursor.close()
            cnx.close()
            return result
