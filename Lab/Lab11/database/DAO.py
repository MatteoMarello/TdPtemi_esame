from Lab.Lab11.database.DB_connect import DBConnect
from Lab.Lab11.model.product import Product

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getColors():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct gp.Product_color 
                from go_products gp """
        cursor.execute(query)

        for row in cursor:
            result.append(row["Product_color"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getProducts():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select * 
                from go_products gp """
        cursor.execute(query)

        for row in cursor:
            result.append(Product(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdgeWeight(anno, codiceProd1, codiceProd2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """ select count(distinct gds2.`Date`) as peso 
                    from go_daily_sales gds, go_daily_sales gds2
                    where year (gds2.`Date`) = %s
                    and gds2.`Date` = gds.`Date`
                    and gds2.Retailer_code = gds.Retailer_code
                    and gds2.Product_number = %s
                    and gds.Product_number = %s"""

        cursor.execute(query,(anno,codiceProd1, codiceProd2))
        for row in cursor:
            res = row[0]

        cursor.close()
        conn.close()
        return res



if __name__ == "__main__":
    dao = DAO()
