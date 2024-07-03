from Esami.Genes.undici_giugno.database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getCromosomi():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ select distinct Chromosome 
                        from genes g 
                        where Chromosome != 0
                        """
            cursor.execute(query)
            for row in cursor:
                result.append(row['Chromosome'])
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
            query = """ SELECT DISTINCT g.Chromosome as c1 , g2.Chromosome as c2
                        FROM genes g , interactions i , genes g2 
                        WHERE g.GeneID = i.GeneID1 AND g2.GeneID = i.GeneID2
                        AND g.Chromosome != 0 AND g2.Chromosome != 0 and g.Chromosome != g2.Chromosome 
                        """
            cursor.execute(query)
            for row in cursor:
                result.append((row['c1'], row["c2"]))
            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def getEdgeWeight(c1,c2):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT SUM(t1.Expression_Corr) as peso 
                        FROM 
                        (SELECT DISTINCT g.Chromosome as c1, g2.Chromosome as c2, i.Expression_Corr 
                        FROM genes g , interactions i , genes g2 
                        WHERE g.GeneID = i.GeneID1 AND g2.GeneID = i.GeneID2
                        AND g.Chromosome = %s and g2.Chromosome = %s) as t1
                        """
            cursor.execute(query, (c1,c2))
            for row in cursor:
                result.append(row["peso"])
            cursor.close()
            cnx.close()
            if result:
                return result[0]
            else:
                return 0

