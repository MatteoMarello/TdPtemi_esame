import time

import flet as ft
from Esami.Duemilaventidue.quattordici_settembre.model.model import Model
from Esami.Duemilaventidue.quattordici_settembre.UI.view import View
class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleCreaGrafo(self, e):
        self._view.txt_result.controls.clear()
        d = int(self._view._txtInDurata.value)
        dms = d * 60 * 1000
        self._model.buildGraph(dms)
        nN, nE = self._model.getGraphDetails()
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {nE}"))
        self.fillDDAlbum()
        self._view.update_page()


    def fillDDAlbum(self):
        albums = self._model.getAlbums()
        albums.sort(key=lambda x: x.Title)
        for a in albums:
            self._view._ddAlbum.options.append(ft.dropdown.Option(
                data=a,
                text=a,
                on_click=self.readAlbumDD
            ))

    def readAlbumDD(self, e):
        if e.control.data is None:
            self.chosenAlbum = None
        else:
            self.chosenAlbum = e.control.data

    def handleAnalisiComp(self, e):
        dim , durata = self._model.getConnCompInfo(self.chosenAlbum)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"La dimensione della componente connessa contenente {self.chosenAlbum} è {dim}. La durata totale degli album che ne fanno parte è {durata} minuti"))
        self._view.update_page()

    def handleGetSetAlbum(self, e):
        self._view.txt_result.controls.clear()
        dTOT = int(self._view._txtInSoglia.value)
        dTOTms = dTOT * 60 * 1000
        start_time = time.time()
        setAlbum, durata = self._model.getSetAlbum(self.chosenAlbum, dTOTms)
        self._view.txt_result.controls.append(ft.Text(f"Elapsed time: {time.time() - start_time} secondi."))
        self._view.txt_result.controls.append(ft.Text(f"Il set di album trovato ha durata {durata} minuti"))
        for a in setAlbum:
            self._view.txt_result.controls.append(ft.Text(f"{a}"))
        self._view.update_page()
