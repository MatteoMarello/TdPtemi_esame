from Classroom.Baseball.database.DB_connect import DBConnect
from Classroom.Baseball.model.team import Team

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT `year` 
                    FROM teams t 
                    WHERE `year` >= 1985
                    ORDER BY `year` DESC """

        cursor.execute(query)

        for row in cursor:
            result.append(row['year'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getTeamsOfYear(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT *
                    FROM teams t 
                    WHERE `year` = %s"""

        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Team(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getSalaryOfTeams(year, idMap):
        conn = DBConnect.get_connection()

        result = {}

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT t.teamCode , t.ID, SUM( s.salary ) as totSalary
                    FROM salaries s , teams t , appearances a 
                    WHERE s.`year` = t.`year` AND t.`year` = a.`year` 
                    AND a.`year` = %s
                    AND t.ID = a.teamID AND a.playerID = s.playerID 
                    GROUP BY t.teamCode, t.ID """

        cursor.execute(query, (year,))

        for row in cursor:
            result[idMap[row["ID"]]] = row["totSalary"]

        cursor.close()
        conn.close()
        return result

