from Classroom.FlightDelays.database.DB_connect import DBConnect
from Classroom.FlightDelays.model.airport import Airport
from Classroom.FlightDelays.model.connessione import Connessione

class DAO():

    @staticmethod
    def getAllNodes(Nmin, idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT tmp.ID, tmp.IATA_CODE, COUNT(*) as N 
                    from 
                    (SELECT a.ID , a.IATA_CODE , f.AIRLINE_ID, COUNT(*) as n 
                    FROM airports a , flights f 
                    WHERE a.ID = f.ORIGIN_AIRPORT_ID OR a.ID = f.DESTINATION_AIRPORT_ID
                    GROUP BY a.ID , a.IATA_CODE , f.AIRLINE_ID) as tmp 
                    GROUP BY tmp.ID, tmp.IATA_CODE
                    HAVING N >= %s """

        cursor.execute(query, (Nmin,))

        for row in cursor:
            result.append(idMap[row["ID"]])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * from airports"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdgesV1(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID, COUNT(*) as n 
                    FROM extflightdelays.flights f 
                    GROUP BY f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID 
                    ORDER BY f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID """

        cursor.execute(query)

        for row in cursor:
            result.append(Connessione(idMap[row['ORIGIN_AIRPORT_ID']], idMap[row['DESTINATION_AIRPORT_ID']], row['n']))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdgesV2(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT t1.ORIGIN_AIRPORT_ID, t1.DESTINATION_AIRPORT_ID, COALESCE (t1.peso, 0) + COALESCE (t2.peso, 0) as peso
                    FROM (SELECT f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID, COUNT(*) as peso 
                    FROM extflightdelays.flights f 
                    GROUP BY f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID 
                    ORDER BY f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID ) as t1
                    LEFT JOIN 
                    (SELECT f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID, COUNT(*) as peso 
                    FROM extflightdelays.flights f 
                    GROUP BY f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID 
                    ORDER BY f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID ) as t2
                    ON t1.ORIGIN_AIRPORT_ID = t2.DESTINATION_AIRPORT_ID AND t2.ORIGIN_AIRPORT_ID = t1.DESTINATION_AIRPORT_ID
                    WHERE t1.ORIGIN_AIRPORT_ID < t1.DESTINATION_AIRPORT_ID OR t2.ORIGIN_AIRPORT_ID IS NULL """

        cursor.execute(query)

        for row in cursor:
            result.append(Connessione(idMap[row['ORIGIN_AIRPORT_ID']], idMap[row['DESTINATION_AIRPORT_ID']], row['peso']))

        cursor.close()
        conn.close()
        return result