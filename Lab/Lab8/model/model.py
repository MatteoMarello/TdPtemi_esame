import copy

from Lab.Lab8.database.DAO import DAO
from Lab.Lab8.model.nerc import Nerc
from Lab.Lab8.model.powerOutages import Event

class Model:
    def __init__(self):
        self._solBest = []
        self._utentiMax = 0
        self._listNerc = None
        self._listEvents = None
        self.loadNerc()

    def worstCase(self, nerc, maxY, maxH):
        self._listEvents = DAO.getAllEvents(nerc)
        self._solBest = []
        self._utentiMax = 0
        self.ricorsione([], maxY, maxH, self._listEvents)
        ore_disservizio = self.calcolaOreDisservizio(self._solBest)

        return self._solBest, self._utentiMax, ore_disservizio


    def ricorsione(self, parziale, maxY, maxH, lista_eventi):
        if len(lista_eventi) == 0:
            print(parziale)
            utenti_disservizio = self.calcolaUtentiConDisservizio(parziale)
            if utenti_disservizio > self._utentiMax:
                print("NEW BEST SOL!")
                self._utentiMax = utenti_disservizio
                self._solBest = copy.deepcopy(parziale)

        else:
            for evento in lista_eventi:
                parziale.append(evento)
                copy_list = copy.deepcopy(lista_eventi)
                lista_eventi_nuova = self.getNuovaListaEventi(parziale, copy_list, maxH, maxY)
                self.ricorsione(parziale,maxY,maxH, lista_eventi_nuova)
                parziale.pop()


    def getNuovaListaEventi(self, parziale, lista_eventi_esistente, maxH, maxY):
        lista_eventi_nuova = []
        for evento in lista_eventi_esistente:
            if evento not in parziale:
                lista_eventi_nuova.append(evento)

        oreDisservizio = self.calcolaOreDisservizio(parziale)
        lista_copy = copy.deepcopy(lista_eventi_nuova)
        annoMinLista = self.calcolaAnnoMin(parziale)
        annoMaxLista = self.calcolaAnnoMax(parziale)
        for evento in lista_copy:
            annoMin = evento.date_event_began.year
            annoMax = evento.date_event_finished.year
            if abs(annoMaxLista - annoMin) > maxY or abs(annoMax-annoMinLista) > maxY:
                lista_eventi_nuova.remove(evento)
                continue

            differenza = evento.date_event_finished - evento.date_event_began
            differenza_seconds = differenza.total_seconds()
            differenza_ore = differenza_seconds / 3600
            if oreDisservizio + differenza_ore > maxH:
                lista_eventi_nuova.remove(evento)

        return lista_eventi_nuova

    def calcolaOreDisservizio(self, parziale: list[Event]):
        oreDisservizio = 0
        for evento in parziale:
            differenza = evento.date_event_finished - evento.date_event_began
            differenza_seconds = differenza.total_seconds()
            differenza_ore = differenza_seconds / 3600
            oreDisservizio += differenza_ore

        return oreDisservizio

    def calcolaUtentiConDisservizio(self, lista_eventi: list[Event]):
        num_utenti = 0
        for evento in lista_eventi:
            num_utenti+=evento.customers_affected
        return num_utenti

    def soddisfaVincoli(self, parziale: list[Event], maxY, maxH):
        annoMin= 100000
        annoMax = 0
        for event in parziale:
            if event.date_event_began.year < annoMin:
                annoMin = event.date_event_began.year
            if event.date_event_finished.year > annoMax:
                annoMax = event.date_event_finished.year

        if abs(annoMax - annoMin) > maxY:
            return False

        oreDisservizio = self.calcolaOreDisservizio(parziale)
        if oreDisservizio > maxH:
            return False

        return True

    def calcolaAnnoMin(self, lista: list[Event]):
        annoMin = 10000
        for evento in lista:
            if evento.date_event_began.year < annoMin:
                annoMin = evento.date_event_began.year
        return annoMin

    def calcolaAnnoMax(self, lista: list[Event]):
        annoMax = 0
        for evento in lista:
            if evento.date_event_finished.year > annoMax:
                annoMax = evento.date_event_finished.year
        return annoMax


    def loadEvents(self, nerc):
        self._listEvents = DAO.getAllEvents(nerc)

    def loadNerc(self):
        self._listNerc = DAO.getAllNerc()


    @property
    def listNerc(self):
        return self._listNerc


if __name__ == "__main__":
    model = Model()
    nerc = Nerc(1, "ERCOT")
    list_events=DAO.getAllEvents(nerc)

    lista_eventi, utenti, ore_disservizio = model.worstCase(nerc, 4, 200)
    for evento in lista_eventi:
        print(evento)
    print(f'utenti disservizio {utenti}')
    print(f'ore disservizio {ore_disservizio}')