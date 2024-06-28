from Esami.Duemilaventitre.ventiquattro_gennaio.database.DB_connect import DBConnect
from Esami.Duemilaventitre.ventiquattro_gennaio.model.metodo import Metodo
from Esami.Duemilaventitre.ventiquattro_gennaio.model.product import Product
class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getMethods():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT * 
                FROM go_methods gm 
                order by Order_method_type ASC 

                                                """
            cursor.execute(query)
            for row in cursor:
                result.append(Metodo(**row))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getAllProducts():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT *
                FROM go_products gp 

                                                """
            cursor.execute(query)
            for row in cursor:
                result.append(Product(**row))
            cursor.close()
            cnx.close()
            return result



    @staticmethod
    def getNodes(anno, metodo, idMap):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT gp.Product_number, SUM(gds.Unit_sale_price * gds.Quantity) as ricaviTotali
                FROM go_daily_sales gds, go_products gp 
                WHERE gp.Product_number = gds.Product_number 
                and gds.Order_method_code = %s
                and YEAR (gds.`Date`) = %s
                GROUP BY gp.Product_number

                                                """
            cursor.execute(query, (metodo, anno))
            for row in cursor:
                p = idMap[row["Product_number"]]
                p.ricaviTotali = row["ricaviTotali"]
                result.append(p)
            cursor.close()
            cnx.close()
            return result

