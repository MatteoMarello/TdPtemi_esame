from Classroom.Anagrammi.database.DB_connect import DBConnect


class DAO():
    @staticmethod
    def getWordsFromDictionary():
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore connessione")
            return
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT nome FROM parola """
            cursor.execute(query)
            words=[]
            rows = cursor.fetchall()
            for word in rows:
                words.append(word['nome'])

            cursor.close()
            cnx.close()
            return words


if __name__ == "__main__":
    dao = DAO()
    words = dao.getWordsFromDictionary()
    print(words)