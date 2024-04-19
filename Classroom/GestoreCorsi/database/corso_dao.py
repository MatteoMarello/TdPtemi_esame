import mysql.connector
from Classroom.GestoreCorsi.database.DB_connect import DBConnect
from Classroom.GestoreCorsi.model.corso import Corso
from Classroom.GestoreCorsi.model.studente import Studente
class CorsoDAO:

    @staticmethod
    def get_corsi_periodo(pd):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connessione")
            return
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * FROM corso WHERE pd = %s"""
            cursor.execute(query, (pd,))
            for row in cursor:
                result.append(Corso(row['codins'], row['crediti'], row['nome'], row['pd']))

            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def get_studenti_periodo(pd):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore connessione")
            return
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT i.matricola FROM corso c, iscrizione i WHERE c.codins = i.codins AND c.pd = %s"""
            cursor.execute(query, (pd,))
            rows = cursor.fetchall()

            cursor.close()
            cnx.close()
            return rows


    @staticmethod
    def get_all_corsi():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connessione")
            return
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * FROM corso"""
            cursor.execute(query)
            for row in cursor:
                result.append(Corso(row['codins'], row['crediti'], row['nome'], row['pd']))

            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def get_studenti_singolo_corso(codins):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * FROM iscrizione, studente WHERE iscrizione.codins = %s AND studente.matricola = iscrizione.matricola ORDER BY iscrizione.matricola"""
            cursor.execute(query, (codins,))
            rows = cursor.fetchall()
            for row in rows:
                result.append(Studente(row['matricola'], row['cognome'], row['nome'], row['CDS']))

            cursor.close()
            cnx.close()
            return result


if __name__ == "__main__":
    studenti_corso = CorsoDAO.get_studenti_singolo_corso("01PDYPG")
    print(len(studenti_corso))