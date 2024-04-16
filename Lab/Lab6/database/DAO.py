from Lab.Lab6.database.DB_connect import DBConnect
from Lab.Lab6.model.retailer import Retailer
class DAO():

    @staticmethod
    def getYears():
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore connessione")
            return
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT YEAR(Date) as year FROM go_daily_sales ORDER BY year ASC """
            cursor.execute(query)
            years = set()
            rows = cursor.fetchall()
            for year in rows:
                years.add(year['year'])

            cursor.close()
            cnx.close()
            return years


    @staticmethod
    def getBrands():
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore connessione")
            return
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT Product_brand FROM go_products """
            cursor.execute(query)
            brands = set()
            rows = cursor.fetchall()
            for brand in rows:
                brands.add(brand['Product_brand'])

            cursor.close()
            cnx.close()
            return brands

    @staticmethod
    def getRetailers():
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore connessione")
            return
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT * FROM go_retailers"""
            cursor.execute(query)
            retailers = []
            rows = cursor.fetchall()
            for retailer in rows:
                retailers.append(Retailer(retailer['Retailer_code'], retailer['Retailer_name'], retailer['Type'], retailer['Country']))

            cursor.close()
            cnx.close()
            return retailers


    @staticmethod
    def getTopVendite(anno, brand, codice_retailer):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore connessione")
            return
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT gds.`Date` as Data , gds.Unit_sale_price * gds.Quantity as Ricavo, gds.Retailer_code as Retailer, gds.Product_number as Prodotto
                        FROM go_daily_sales gds, go_products gp  
                        WHERE gp.Product_number = gds.Product_number 
                        AND YEAR (gds.`Date`) = COALESCE (%s, YEAR(gds.`Date`)) 
                        AND gp.Product_brand = COALESCE (%s, gp.Product_brand) 
                        AND gds.Retailer_code = COALESCE (%s, gds.Retailer_code)
                        ORDER BY (gds.Unit_sale_price*gds.Quantity) DESC"""
            cursor.execute(query, (anno, brand, codice_retailer))
            res = []
            rows = cursor.fetchmany(5)
            for row in rows:
                res.append(row)

            random = cursor.fetchall()
            cursor.close()
            cnx.close()
            return res




if __name__ == "__main__":
    vendite = DAO.getTopVendite(2017, None, None)
    for vendita in vendite:
        print(vendita)
