from Lab.Lab9.database.DB_connect import DBConnect
from Lab.Lab9.model.airport import Airport

class DAO():

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM airports"
        cursor.execute(query)

        for row in cursor:
            result.append(Airport(row['ID'], row['IATA_CODE'], row['AIRPORT'], row['CITY'], row['STATE'], row['COUNTRY'], row['LATITUDE'], row['LONGITUDE'], row['TIMEZONE_OFFSET']))
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getFlights():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
        select
        f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, AVG(f.DISTANCE) as distanza_media
        from flights f
        group by
        ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID 
        """
        cursor.execute(query)

        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result

if __name__ == "__main__":
    dao = DAO()
    voli = dao.getFlights()
    print(voli)