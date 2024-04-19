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
        matricole = CorsoDAO.get_studenti_periodo(pd)
        return len(matricole)



    def get_studenti_corso(self, codins):
        for corso in self.corsi:
            if corso.codins == codins:
                if corso.studenti is None:
                    corso.studenti = CorsoDAO.get_studenti_singolo_corso(codins)
                    return corso.studenti
                else:
                    return corso.studenti



    def getDettagliCorso(self, codiceCorso):
        dettagli = {}
        for corso in self.corsi:
            if corso.codins == codiceCorso:
                if corso.studenti is None:
                    corso.studenti = CorsoDAO.get_studenti_singolo_corso(codiceCorso)

                for studente in corso.studenti:

                    if dettagli.get(studente.CDS) is None:
                        dettagli[studente.CDS] = 1
                    else:
                        dettagli[studente.CDS] += 1

        return dettagli


