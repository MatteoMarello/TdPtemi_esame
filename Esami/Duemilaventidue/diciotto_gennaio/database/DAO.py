from Esami.Duemilaventidue.diciotto_gennaio.database.DB_connect import DBConnect
from Esami.Duemilaventidue.diciotto_gennaio.model.location import Location

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
                SELECT DISTINCT nwhl.Provider 
                FROM nyc_wifi_hotspot_locations nwhl 
                order by nwhl.Provider 
                                                """
            cursor.execute(query)
            for row in cursor:
                result.append(row["Provider"])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getLocations(provider):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT Location , AVG(Latitude) as Latitude, AVG(Longitude) as Longitude
                FROM nyc_wifi_hotspot_locations nwhl 
                WHERE Provider = %s
                group by Location
                                                """
            cursor.execute(query, (provider, ))
            for row in cursor:
                result.append(Location(**row))
            cursor.close()
            cnx.close()
            return result
