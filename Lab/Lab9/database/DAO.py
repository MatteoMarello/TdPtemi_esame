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
