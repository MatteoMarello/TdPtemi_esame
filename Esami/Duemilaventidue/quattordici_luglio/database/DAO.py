from Esami.Duemilaventidue.quattordici_luglio.database.DB_connect import DBConnect
from Esami.Duemilaventidue.quattordici_luglio.model.nta import NTA
class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getBorghi():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT DISTINCT nwhl.Borough 
                FROM nyc_wifi_hotspot_locations nwhl 
                order by Borough ASC 

                                                """
            cursor.execute(query)
            for row in cursor:
                result.append(row["Borough"])
            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def getNodes(borgo):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT NTACode, COUNT(DISTINCT SSID) as nSSID 
                FROM nyc_wifi_hotspot_locations nwhl 
                WHERE Borough = %s 
                GROUP BY NTACode
                ORDER BY NTACode ASC 
                                                """
            cursor.execute(query, (borgo,))
            for row in cursor:
                result.append(NTA(**row))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getSSID(ntaCode):
        cnx = DBConnect.get_connection()
        result = set()
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT DISTINCT SSID
                from nyc_wifi_hotspot_locations nwhl 
                WHERE nwhl.NTACode = %s 
                                                """
            cursor.execute(query, (ntaCode,))
            for row in cursor:
                result.add(row["SSID"])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getSSIDV2(ntaCode, ntaCode2):
        cnx = DBConnect.get_connection()
        result = set()
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT DISTINCT SSID
                from nyc_wifi_hotspot_locations nwhl 
                WHERE nwhl.NTACode = %s
                UNION 
                SELECT DISTINCT SSID
                from nyc_wifi_hotspot_locations nwhl 
                WHERE nwhl.NTACode = %s       """
            cursor.execute(query, (ntaCode, ntaCode2))
            for row in cursor:
                result.add(row["SSID"])
            cursor.close()
            cnx.close()
            return result