from Lab.Lab10.database.DB_connect import DBConnect
from Lab.Lab10.model.country import Country

class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM country"
        cursor.execute(query)

        for row in cursor:
            result.append(Country(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getCountriesExisting(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "select state1no from contiguity c where `year` <= %s order by state1ab ASC"
        cursor.execute(query, (anno,))

        for row in cursor:
            if row['state1no'] not in result:
                result.append(row['state1no'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getContiguitiesExisting(anno):
        conn = DBConnect.get_connection()

        result = set()

        cursor = conn.cursor(dictionary=True)
        query = "select state1no, state2no from contiguity c where `year` <= %s and c.conttype = 1"
        cursor.execute(query, (anno,))

        for row in cursor:
            result.add((row['state1no'], row['state2no']))

        cursor.close()
        conn.close()
        return result


if __name__ == "__main__":
    dao = DAO()
    countries = dao.getAllCountries()
    for country in countries:
        print(country)

    countriesExisting = dao.getCountriesExisting(1980)
    for element in countriesExisting:
        print(element)