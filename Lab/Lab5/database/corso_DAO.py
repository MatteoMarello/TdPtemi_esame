# Add whatever it is needed to interface with the DB Table corso

from Lab.Lab5.database.DB_connect import get_connection

from Lab.Lab5.model.corso import Corso
from Lab.Lab5.model.studente import Studente

class CorsoDAO:
    def __init__(self):
        pass

    def getCorsi(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM corso"""
        cursor.execute(query)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(Corso(row['codins'], row['crediti'], row['nome'], row['pd']))

        cursor.close()
        cnx.close()

        return result


    def getIscrittiCorso(self, codins):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM studente, iscrizione WHERE iscrizione.matricola = studente.matricola AND iscrizione.codins = %s ORDER BY studente.nome ASC"""
        cursor.execute(query, (codins,))
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(Studente(row['matricola'], row['nome'], row['cognome'], row['CDS']))

        cursor.close()
        cnx.close()
        return result

    def getCorso(self, codins):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM corso WHERE codins = %s"""
        cursor.execute(query, (codins,))
        result = cursor.fetchone()

        cursor.close()
        cnx.close()

        return result

    def getIscrittoCorso(self, codins, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM iscrizione WHERE codins = %s AND matricola = %s"""
        cursor.execute(query, (codins,matricola))
        result = cursor.fetchone()

        cursor.close()
        cnx.close()

        return result


    def iscrizione(self, codins, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """INSERT INTO iscrizione (codins, matricola) VALUES (%s,%s)"""
        cursor.execute(query, (codins,matricola))
        try:
            cnx.commit()
            cursor.close()
            cnx.close()
            return True

        except:
            cnx.rollback()
            cursor.close()
            cnx.close()
            return False




if __name__ == "__main__":
    corso_dao = CorsoDAO()
    iscritti = corso_dao.getIscrittiCorso("01KSUPG")
    for iscritto in iscritti:
        print(iscritto.__str__())