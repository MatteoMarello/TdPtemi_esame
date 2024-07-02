import time

import flet as ft
from Esami.Ufo.undici_giugno.model.model import Model
from Esami.Ufo.undici_giugno.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDDAnni(self):
        self._anniWithAvvistamenti = self._model.getAnniWithAvvistamenti()
        for a in self._anniWithAvvistamenti:
            self._view.ddAnno.options.append(ft.dropdown.Option(a))


    def handleAvvistamenti(self, e):
        self._view.txtOut.controls.clear()
        anno = self._view.ddAnno.value
        if anno is None:
            self._view.txtOut.controls.append(ft.Text("Devi selezionare un anno!"))
            self._view.update_page()
            return

        anno = anno[1:5]
        self._model.buildGraph(anno)
        nN, nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text("Grafo correttamente creato!"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di nodi: {nN}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {nE}"))
        stati = self._model.getStati()
        for s in stati:
            self._view.ddStato.options.append(ft.dropdown.Option(
                text=s,
                data=s,
                on_click=self.readDDStato
            ))
        self._view.btnAnalizza.disabled = False
        self._view.btnSequenza.disabled = False
        self._view.update_page()

    def readDDStato(self, e):
        if e.control.data is None:
            self._chosenState = None
        else:
            self._chosenState = e.control.data


    def handleAnalizza(self, e):
        self._view.txtOut.controls.clear()
        if self._chosenState is None:
            self._view.txtOut.controls.append(ft.Text("Devi selezionare uno stato!"))
            self._view.update_page()
            return

        pred = self._model.getPredecessors(self._chosenState)
        succ = self._model.getSuccessors(self._chosenState)
        self._view.txtOut.controls.append(ft.Text(f"Gli stati predecessori di {self._chosenState} sono: {pred}"))

        self._view.txtOut.controls.append(ft.Text(f"Gli stati successori di {self._chosenState} sono: {succ}"))

        nodiRaggiungibili = self._model.getStatiRaggiungibili(self._chosenState)
        self._view.txtOut.controls.append(ft.Text(f"Ci sono {len(nodiRaggiungibili)} stati raggiungibili da {self._chosenState}"))
        self._view.txtOut.controls.append(ft.Text(f"Gli stati raggiungibili da {self._chosenState} sono: {nodiRaggiungibili}"))

        self._view.update_page()



    def handleSequenza(self, e):
        self._view.txtOut.controls.clear()
        if self._chosenState is None:
            self._view.txtOut.controls.append(ft.Text("Devi selezionare prima uno stato"))

        start_time = time.time()
        seq = self._model.getSequenza(self._chosenState)
        end_time = time.time()
        self._view.txtOut.controls.append(ft.Text(F"Elapsed time: {end_time-start_time}"))
        for s in seq:
            self._view.txtOut.controls.append(ft.Text(f"{s}"))

        self._view.update_page()