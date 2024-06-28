import flet as ft
from Esami.Duemilaventitre.trenta_giugno.model.model import Model
from Esami.Duemilaventitre.trenta_giugno.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDDTeams(self):
        teams = self._model.getTeams()
        for t in teams:
            self._view.ddSquadra.options.append(ft.dropdown.Option(t))


    def handle_graph(self, e):
        self._view.txtOut.controls.clear()
        team = self._view.ddSquadra.value
        if team is None:
            self._view.txtOut.controls.append(ft.Text("Devi selezionare una squadra!"))
            self._view.update_page()
            return

        self._model.buildGraph(team)
        nN,nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {nE}"))
        self.fillDDAnni()
        self._view.update_page()


    def fillDDAnni(self):
        anni = self._model.getAnni()
        for a in anni:
            self._view.ddAnno.options.append(ft.dropdown.Option(a))

    def handleDettagli(self, e):
        self._view.txtOut.controls.clear()
        anno = int(self._view.ddAnno.value)
        if anno is None:
            self._view.txtOut.controls.append(ft.Text("Devi selezionare un anno dal menù a tendina!"))
            self._view.update_page()
            return

        anniAdiacenti = self._model.getAnniAdiacenti(anno)
        self._view.txtOut.controls.append(ft.Text(f"Gli anni adiacenti all'anno {anno} sono:"))
        for a in anniAdiacenti:
            self._view.txtOut.controls.append(ft.Text(F"{a[0]} --> Peso arco: {a[1]}"))

        self._view.update_page()
