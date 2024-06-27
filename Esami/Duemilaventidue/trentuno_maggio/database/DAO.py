from Esami.Duemilaventidue.trentuno_maggio.database.DB_connect import DBConnect
from Esami.Duemilaventidue.trentuno_maggio.model.city import City
class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getProviders():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                   SELECT DISTINCT Provider 
                    FROM nyc_wifi_hotspot_locations nwhl 
                    order by Provider 
                                                """
            cursor.execute(query)
            for row in cursor:
                result.append(row["Provider"])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getCities(provider):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                   SELECT nwhl.City, AVG(nwhl.Latitude) as latitude, AVG(nwhl.Longitude) as longitude 
                    FROM nyc_wifi_hotspot_locations nwhl 
                    WHERE Provider = %s  
                    GROUP BY nwhl.City         """
            cursor.execute(query, (provider,))
            for row in cursor:
                result.append(City(**row))
            cursor.close()
            cnx.close()
            return result

