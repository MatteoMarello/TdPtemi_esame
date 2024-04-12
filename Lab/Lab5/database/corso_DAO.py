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


if __name__ == "__main__":
    corso_dao = CorsoDAO()
    iscritti = corso_dao.getIscrittiCorso("01KSUPG")
    for iscritto in iscritti:
        print(iscritto.__str__())