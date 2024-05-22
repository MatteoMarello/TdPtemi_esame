from Classroom.FlightDelays.database.DB_connect import DBConnect
from Classroom.FlightDelays.model.airport import Airport


class DAO():

    @staticmethod
    def getAllNodes(Nmin):
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
            result.append(row)

        cursor.close()
        conn.close()
        return result