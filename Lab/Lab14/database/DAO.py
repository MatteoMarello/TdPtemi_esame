from Lab.Lab14.database.DB_connect import DBConnect


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
    def getEdgeWeight(c1,c2):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ select sum(b1.Expression_Corr) as peso
                        from (select distinctrow g.Chromosome as c1, g2.Chromosome as c2, i.Expression_Corr  
                        from interactions i, genes g , genes g2 
                        where i.GeneID1 = g.GeneID 
                        and i.GeneID2 = g2.GeneID 
                        and g.Chromosome = %s
                        and g2.Chromosome = %s) as b1
                        group by b1.c1, b1.c2

                        """
            cursor.execute(query, (c1,c2))
            for row in cursor:
                result.append(row["peso"])
            cursor.close()
            cnx.close()
            return result


if __name__ == "__main__":
    dao = DAO()
    crom = dao.getCromosomi()
    print(crom)

    res = dao.getEdgeWeight(5,11)
    print(res[0])
