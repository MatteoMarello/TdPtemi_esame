from Lab.Lab7.database.meteo_dao import MeteoDao
class Model:
    def __init__(self):
        self._situazioni = MeteoDao.get_all_situazioni()

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




if __name__ == "__main__":
    model = Model()
    dict_umidita = model.getUmiditaMedia(2)
    print(dict_umidita)
