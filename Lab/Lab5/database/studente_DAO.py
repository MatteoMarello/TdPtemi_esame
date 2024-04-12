# Add whatever it is needed to interface with the DB Table studente

from Lab.Lab5.database.DB_connect import (get_connection)
from Lab.Lab5.model.studente import Studente
from Lab.Lab5.model.corso import Corso

class StudenteDAO:
    def __init__(self):
        pass

    def getStudenti(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM studente"""
        cursor.execute(query)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(Studente(row['matricola'], row['nome'], row['cognome'], row['CDS']))

        cursor.close()
        cnx.close()

        return result

    def getStudente(self, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM studente WHERE matricola = %s"""
        cursor.execute(query, (matricola,))
        result = cursor.fetchone()

        cursor.close()
        cnx.close()

        return result


    def getCorsiStudente(self, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM iscrizione, corso WHERE matricola = %s AND iscrizione.codins = corso.codins"""
        cursor.execute(query, (matricola,))
        result = cursor.fetchall()
        list = []
        for row in result:
            list.append(Corso(row['codins'], row['crediti'], row['nome'], row['pd']))

        cursor.close()
        cnx.close()
        return list


if __name__ == "__main__":
    studente_dao = StudenteDAO()
    lista_corsi = studente_dao.getCorsiStudente(190635)
    for corso in lista_corsi:
        print(corso)

    studenti = studente_dao.getStudenti()
    for studente in studenti:
        print(studente)
