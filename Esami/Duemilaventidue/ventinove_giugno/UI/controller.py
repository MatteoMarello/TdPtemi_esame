import time

import flet as ft
from Esami.Duemilaventidue.ventinove_giugno.model.model import Model
from Esami.Duemilaventidue.ventinove_giugno.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDD(self):
        albums = self._model.getAlbums()
        albums.sort(key=lambda a: a.Title)
        for a in albums:
            self._view.ddA1.options.append(ft.dropdown.Option(
                data=a,
                text=a,
                on_click=self.readDDA1
            ))
            self._view.ddA2.options.append(ft.dropdown.Option(
                data=a,
                text=a,
                on_click=self.readDDA2
            ))


    def handleGrafo(self, e):
        self._view.txtOut.controls.clear()
        try :
            n = int(self._view.txtInNCanzoni.value)
        except ValueError:
            self._view.txtOut.controls.append(ft.Text("Devi inserire un numero!"))
            self._view.update_page()
            return

        self._model.buildGraph(n)
        nN, nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text("Grafo correttamente creato!"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {nE}"))
        self.fillDD()
        self._view.update_page()



    def handleStampaAdiacenze(self, e):
        self._view.txtOut.controls.clear()
        adiacenze = self._model.getAdiacenze(self.chosenA1)
        for a in adiacenze:
            self._view.txtOut.controls.append(ft.Text(F"{a[0]} -- Bilancio: {a[1]}"))

        self._view.update_page()


    def handlePercorso(self, e):
        self._view.txtOut.controls.clear()
        x = int(self._view.txtInSoglia.value)
        if not self._model.has_path(self.chosenA1, self.chosenA2):
            self._view.txtOut.controls.append(ft.Text(f"Non esiste un percorso fra {self.chosenA1} e {self.chosenA2}!"))
            self._view.update_page()
            return

        start_time = time.time()
        percorso = self._model.getPercorso(self.chosenA1, self.chosenA2, x)
        print(percorso)
        self._view.txtOut.controls.append(ft.Text(f"Elapsed time: {time.time() - start_time} secondi"))

        for p in percorso:
            self._view.txtOut.controls.append(ft.Text(F"{p[0]} --> {p[1]}. Costo: {p[2]}"))

        self._view.update_page()


    def readDDA1(self, e):
        if e.control.data is None:
            self.chosenA1 = None
        else:
            self.chosenA1 = e.control.data

    def readDDA2(self, e):
        if e.control.data is None:
            self.chosenA2 = None
        else:
            self.chosenA2 = e.control.data
