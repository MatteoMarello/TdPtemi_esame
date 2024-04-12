from Lab.Lab5.database.corso_DAO import CorsoDAO
from Lab.Lab5.database.studente_DAO import StudenteDAO
class Model:
    def __init__(self):
        self._corsoDAO = CorsoDAO()
        self._studenteDAO = StudenteDAO()
        self._corsi = []
        self._studenti = []
        pass

    def getCorsi(self):
        self._corsi = self._corsoDAO.getCorsi()
        return self._corsi

    def getStudenti(self):
        self._studenti = self._studenteDAO.getStudenti()
        return self._studenti

    def getIscrittiCorso(self, codins):
        for corso in self._corsi:
            if corso.codins == codins:
                if corso.studenti is not None:
                    return corso.studenti

                else:
                    corso.studenti = self._corsoDAO.getIscrittiCorso(codins)
                    return corso.studenti

    def getStudente(self, matricola):
        studente = self._studenteDAO.getStudente(matricola)
        return studente

    def getCorsiStudente(self, matricola):
        matricola = int(matricola)
        for studente in self._studenti:
            if studente.matricola == matricola:
                if studente.corsi is not None:
                    return studente.corsi
                else:
                    corsi_Studente = self._studenteDAO.getCorsiStudente(matricola)
                    studente.corsi = corsi_Studente
                    return corsi_Studente
