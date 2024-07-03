from Esami.Duemilaventitre.trenta_maggio.database.DB_connect import DBConnect
from Esami.Duemilaventitre.trenta_maggio.model.retailer import Retailer

class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getNations():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT DISTINCT Country 
FROM go_retailers gr 
order by Country 
                                                """
            cursor.execute(query)
            for row in cursor:
                result.append(row["Country"])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getRetailers(nazione):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT *
FROM go_retailers gr 
WHERE Country = %s 
                                                """
            cursor.execute(query, (nazione,))
            for row in cursor:
                result.append(Retailer(**row))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getEdges(anno,nazione,m, idMap):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT gds.Retailer_code as r1, gds2.Retailer_code as r2, COUNT(DISTINCT gds2.Product_number) as peso 
FROM go_daily_sales gds , go_retailers gr , go_daily_sales gds2 , go_retailers gr2 
WHERE gds.Retailer_code = gr.Retailer_code AND gr.Country = %s 
AND gds2.Retailer_code = gr2.Retailer_code AND gr2.Country = %s 
AND YEAR (gds2.`Date`) = %s AND YEAR (gds.`Date`) = %s
AND gds2.Product_number = gds.Product_number
AND gds.Retailer_code < gds2.Retailer_code
GROUP BY gds.Retailer_code, gds2.Retailer_code
HAVING peso >= %s
                                                """
            cursor.execute(query, (nazione,nazione, anno, anno, m))
            for row in cursor:
                r1 = idMap[row["r1"]]
                r2 = idMap[row["r2"]]
                result.append((r1,r2,row["peso"]))
            cursor.close()
            cnx.close()
            return result


