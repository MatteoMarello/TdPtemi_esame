from Classroom.GestoreCorsi.database.corso_dao import CorsoDAO
class Model:

    def __init__(self):
        self.corsi = CorsoDAO.get_all_corsi()

    def get_corsi_periodo(self, pd):
        # Soluzione programmatica --> Va bene solamente se il database è statico!
        result = []
        for corso in self.corsi:
            if corso.pd == int(pd):
                result.append(corso)
        return result

        # Soluzione da DAO
        # return CorsoDAO.get_corsi_periodo(pd)

    def get_studenti_periodo(self, pd):
        # Soluzione con Join da SQL
        # matricole = CorsoDAO.get_studenti_periodo(pd)
        # return len(matricole)

        # Soluzione con mappa relazioni
        matricole = set()
        for corso in self.corsi:
            if corso.pd == int(pd):
                matricole_corso = corso.get_studenti()
                if matricole_corso is None:
                    corso.studenti = CorsoDAO.get_studenti_singolo_corso(corso.codins)
                    matricole_corso = corso.studenti

                matricole = matricole.union(matricole_corso)

        return len(matricole)

