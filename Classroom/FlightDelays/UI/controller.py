import flet as ft
from Classroom.FlightDelays.model.model import Model
from Classroom.FlightDelays.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._choiceAeroportoP = None
        self._choiceAeroportoA = None

    def handleAnalizza(self, e):
        self._view._txt_result.controls.clear()
        nMinStr = self._view._txtInNumC.value
        try:
            nMin = int(nMinStr)
            self._model.buildGraph(nMin)
            self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato!"))
            self._view._txt_result.controls.append(ft.Text(f"Numero di nodi: {self._model.getNumNodi()}"))
            self._view._txt_result.controls.append(ft.Text(f"Numero di archi: {self._model.getNumArchi()}"))

        except ValueError:
            self._view._txt_result.controls.append(ft.Text("Il valore inserito nel campo nMin non è un intero!"))

        self.fillDD()
        self._view.update_page()


    def handleConnessi(self, e):
        self._view._txt_result.controls.clear()
        # con handleConnessi voglio stampare l'elenco degli aeroporti adiacenti a quello selezionato (come aeroporto di partenza)
        # in ordine decrescente di numero totali di voli
        v0 = self._choiceAeroportoP
        if v0 is None:
            self._view._txt_result.controls.append(ft.Text("Selezionare un aeroporto di partenza!"))
            self._view.update_page()
            return

        vicini = self._model.getSortedVicini(v0)
        self._view._txt_result.controls.append(ft.Text(f"Ecco i vicini di {v0}"))
        for v in vicini:
            self._view._txt_result.controls.append(ft.Text(f"Peso: {v[1]} - {v[0]}"))

        self._view.update_page()


    def handleCercaItinerario(self, e):
        pass

    def fillDD(self):
        allNodes = self._model.getAllNodes()
        for n in allNodes:
            self._view._ddAeroportoP.options.append(ft.dropdown.Option(
                data=n,
                on_click=self.readDDAeroportoP,
                text=n.AIRPORT
            ))
            self._view._ddAeroportoA.options.append(ft.dropdown.Option(
                data=n,
                on_click=self.readDDAeroportoA,
                text=n.AIRPORT
            ))

    def readDDAeroportoP(self, e):
        if e.control.data is None:
            self._choiceAeroportoP = None
        else:
            self._choiceAeroportoP = e.control.data

    def readDDAeroportoA(self, e):
        if e.control.data is None:
            self._choiceAeroportoA = None
        else:
            self._choiceAeroportoA = e.control.data

