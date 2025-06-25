from Esami.Duemilaventidue.diciotto_gennaio.database.DB_connect import DBConnect
from Esami.Duemilaventidue.diciotto_gennaio.model.location import Location


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getProvider():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select distinct nwhl.Provider
from `nyc-hotspots`.nyc_wifi_hotspot_locations nwhl 
order by nwhl.Provider asc """

        cursor.execute(query,)

        results = []
        for row in cursor:
            results.append(row["Provider"])

        cursor.close()
        cnx.close()
        return results

    @staticmethod
    def getNodi(providernome):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select distinct nwhl.Location , nwhl.OBJECTID, AVG(nwhl.Latitude) as Latitude,  AVG(nwhl.Longitude) as Longitude
from `nyc-hotspots`.nyc_wifi_hotspot_locations nwhl 
where nwhl.Provider =%s
group by Location
order by nwhl.Location"""

        cursor.execute(query,(providernome,))

        results = []
        for row in cursor:
            results.append(Location(row["Location"], row["OBJECTID"], row["Latitude"], row["Longitude"]))

        cursor.close()
        cnx.close()
        return results

