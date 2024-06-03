import warnings

import flet as ft
from Classroom.Baseball.model.model import Model
from Classroom.Baseball.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.selectedTeam = None

    def handleDDYearSelection(self, e):
        teams = self._model.getTeamsOfYear(self._view._ddAnno.value)
        self._view._txtOutSquadre.controls.clear()
        self._view._txtOutSquadre.controls.append(ft.Text(f"Ho trovato {len(teams)} squadre che hanno giocato nell'anno {self._view._ddAnno.value}"))
        for t in teams:
            self._view._txtOutSquadre.controls.append(ft.Text(f'{t.teamCode}'))
            self._view._ddSquadra.options.append(ft.dropdown.Option(
                data=t,
                on_click= self.readDDTeam,
                text=t.teamCode,
            ))

        self._view.update_page()

    def handleCreaGrafo(self, e):
        if self._view._ddAnno.value is None:
            self._view._txt_result.controls.append(ft.Text("Devi selezionare un anno dal menu."))
            return

        self._model.buildGraph(self._view._ddAnno.value)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato!"))
        n, a = self._model.getGraphDetails()
        self._view._txt_result.controls.append(ft.Text(f"Il grafo è costituito da {n} nodi e {a} archi"))
        self._view.update_page()

    def handleDettagli(self, e):
        v0 = self.selectedTeam
        vicini = self._model.getSortedNeighbors(v0)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Stampo i vicini di {v0} con relativo peso dell'arco"))
        for v in vicini:
            self._view._txt_result.controls.append(ft.Text(f"{v[1]} - {v[0]}"))
        self._view.update_page()

    def handlePercorso(self, e):
        self._view._txt_result.controls.clear()
        if self.selectedTeam is None:
            warnings.warn("Squadra non selezionata!")
            self._view._txt_result.controls.append(ft.Text(f'Squadra non selezionata!'))

        else:
            path = self._model.getPercorso(self.selectedTeam)
            self._view._txt_result.controls.append(ft.Text("Percorso trovato!"))
            for p in path:
                self._view._txt_result.controls.append(ft.Text(f"{p[0]} -- {p[1]}"))

        self._view.update_page()

    def fillDDYear(self):
        years = self._model.getYears()
        yearsDD = map(lambda x: ft.dropdown.Option(x), years)
        """
        yearsDD = []
        for y in years:
            yearsDD.append(ft.dropdown.Option(y))
        """
        self._view._ddAnno.options = yearsDD
        self._view.update_page()

    def readDDTeam(self, e):
        if e.control.data is None:
            self.selectedTeam = None
        else:
            self.selectedTeam = e.control.data
