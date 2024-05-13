from Classroom.ArtsMia.database.DB_connect import DBConnect
from Classroom.ArtsMia.model.artObject import ArtObject
from Classroom.ArtsMia.model.connessioni import Connessione
class DAO():

    def __init__(self):
        pass

    @staticmethod
    def getAllObjects():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * FROM objects o"""
            cursor.execute(query)
            for row in cursor:
                # Dato che row è un dizionario, posso fare l'unpack di tutti i valori del dizionario con **row per creare
                # direttamente l'oggetto ArtObject con i propri attributi senza dover fare row['object_id'], row['continent'] ecc.
                # questo funziona solo se le chiavi del dizionario sono IDENTICHE agli della classe di cui sto creando gli oggetti.
                result.append(ArtObject(**row))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getAllConnessioni(idMap):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT eo1.object_id as o1, eo2.object_id as o2, COUNT(*) as peso 
                        FROM exhibition_objects eo1, exhibition_objects eo2  
                        WHERE eo1.exhibition_id = eo2.exhibition_id 
                        AND eo1.object_id < eo2.object_id
                        GROUP BY eo1.object_id, eo2.object_id
                        ORDER BY peso DESC 
                    """
            cursor.execute(query)
            for row in cursor:
                result.append(Connessione(idMap[row['o1']], idMap[row['o2']], row['peso']))
            cursor.close()
            cnx.close()
        return result

    def getPesoArco(self, v1: ArtObject, v2: ArtObject):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT count(*)
                        FROM
                        exhibition_objects eo1, exhibition_objects eo2
                        WHERE eo1.exhibition_id = eo2.exhibition_id
                        AND eo1.object_id < eo2.object_id
                        AND eo1.object_id = %s AND eo2.object_id = %s
            """
            cursor.execute(query, (v1.object_id, v2.object_id))
            for row in cursor:
                result.append(row)
            cursor.close()
            cnx.close()
        return result



if __name__ == "__main__":
    dao = DAO()
    res = dao.getAllObjects()
    print(len(res))

