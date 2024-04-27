import copy

from Lab.Lab7.database.meteo_dao import MeteoDao
from Lab.Lab7.model.situazione import Situazione
class Model:
    def __init__(self):
        self._situazioni = MeteoDao.get_all_situazioni()
        self._sequenzaOttimale = []
        self._costoOttimale = 1000000

    def getUmiditaMedia(self, mese):
        cittas = ["Torino", "Milano", "Genova"]
        dict_umidita = {}
        for citta in cittas:
            dict_umidita[citta] = self.calcolaUmiditaMedia(mese, citta)

        return dict_umidita


    def calcolaUmiditaMedia(self, mese, citta):
        sum = 0
        cnt = 0
        for situazione in self._situazioni:
            if (situazione.data.month == mese and situazione.localita == citta):
                sum += situazione.umidita
                cnt+=1

        return round(sum/cnt, 4)


    def getSequenza(self, mese):
        self._sequenzaOttimale = []
        self._costoOttimale = 1000000
        situazioni_mese_corrente = []
        for situazione in self._situazioni:
            if situazione.data.month == mese:
                situazioni_mese_corrente.append(situazione)

        self.ricorsione([], situazioni_mese_corrente)

        return self._sequenzaOttimale, self._costoOttimale


    def ricorsione(self, parziale, situazioni_mese_corrente):
        if len(parziale) == 15:
            costo = self.controlloCosto(parziale)
            if costo < self._costoOttimale:
                self._costoOttimale = costo
                self._sequenzaOttimale = copy.deepcopy(parziale)
        else:
            for situazione in situazioni_mese_corrente:
                parziale.append(situazione)
                if self.soddisfa_vincoli(parziale):
                    print(parziale)
                    self.ricorsione(parziale, situazioni_mese_corrente)
                parziale.pop()



    def controlloCosto(self, lista_situazioni: list[Situazione]):
        costo = 0
        for i in range(len(lista_situazioni)):
            costo += lista_situazioni[i].umidita
            if i>0 and lista_situazioni[i].localita != lista_situazioni[i-1].localita:
                costo+=100
        return costo

    def soddisfa_vincoli(self, parziale):
        if len(parziale) == 0:
            return True

        ultima_situazione = parziale[-1]
        if len(parziale) != ultima_situazione.data.day:
            return False

        cntTorino = 0
        cntMilano = 0
        cntGenova = 0
        giorni_consecutivi = {"Genova": 0, "Milano": 0, "Torino": 0}
        for situazione in parziale:
            if situazione.localita == "Torino":
                giorni_consecutivi["Torino"] += 1
                giorni_consecutivi["Milano"] = 0
                giorni_consecutivi["Genova"] = 0
                cntTorino+=1
            elif situazione.localita == "Milano":
                giorni_consecutivi["Torino"] = 0
                giorni_consecutivi["Milano"] += 1
                giorni_consecutivi["Genova"] = 0
                cntMilano+=1
            else:
                giorni_consecutivi["Torino"] = 0
                giorni_consecutivi["Milano"] = 0
                giorni_consecutivi["Genova"] += 1
                cntGenova+=1

        if cntMilano > 6 or cntGenova > 6 or cntTorino > 6:
            return False

        if giorni_consecutivi["Torino"] < 3 and giorni_consecutivi["Torino"] > 0:
            if ultima_situazione.localita != "Torino":
                return False

        if giorni_consecutivi["Milano"] < 3 and giorni_consecutivi["Milano"] > 0:
            if ultima_situazione.localita != "Milano":
                return False

        if giorni_consecutivi["Genova"] < 3 and giorni_consecutivi["Genova"] > 0:
            if ultima_situazione.localita != "Genova":
                return False

        return True



if __name__ == "__main__":
    model = Model()
    situazioni = model.getSequenza(2)
    for situazione in situazioni:
        print(situazione)
