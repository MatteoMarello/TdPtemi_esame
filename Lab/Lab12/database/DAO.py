from Lab.Lab12.database.DB_connect import DBConnect
from Lab.Lab12.model.retailer import Retailer
from Lab.Lab12.model.connessione import Connessione
class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getCountries():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT Country 
                    FROM go_retailers gr """
        cursor.execute(query)

        for row in cursor:
            result.append(row["Country"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getRetailers():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * 
                    FROM go_retailers gr """
        cursor.execute(query)

        for row in cursor:
            result.append(Retailer(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(year, country, idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT gds2.Retailer_code as r1, gds.Retailer_code as r2, COUNT(DISTINCT gds.Product_number) as peso 
                    from go_daily_sales gds, go_daily_sales gds2, go_retailers gr, go_retailers gr2  
                    WHERE YEAR (gds.`Date`) = %s
                    AND YEAR (gds2. `Date`) = %s
                    AND gr.Retailer_code = gds2.Retailer_code 
                    AND gr2.Retailer_code = gds.Retailer_code
                    and gr2.Country = %s
                    and gr.Country = %s
                    AND gds2.Retailer_code < gds.Retailer_code
                    AND gds2.Product_number = gds.Product_number
                    GROUP BY gds2.Retailer_code, gds.Retailer_code
                    """
        cursor.execute(query, (year, year, country, country))

        for row in cursor:
            result.append(Connessione(idMap[row["r1"]], idMap[row["r2"]], row["peso"]))
        cursor.close()
        conn.close()
        return result



if __name__ == "__main__":
    dao = DAO()

