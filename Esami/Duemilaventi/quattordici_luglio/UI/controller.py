import flet as ft
from Esami.Duemilaventi.quattordici_luglio.model.model import Model
from Esami.Duemilaventi.quattordici_luglio.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.choiceTeam = None


    def fillDD(self):
        teams = self._model.getTeams()
        for t in teams:
            self._view.ddTeam.options.append(ft.dropdown.Option(
                text=t,
                data=t,
                on_click=self.readDDTeam
            ))


    def handleCreaGrafo(self, e):
        self._view.txtOut.controls.clear()
        self._model.buildGraph()
        nN, nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text(f"Grafo correttamente creato!"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici {nN}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi {nE}"))
        self.fillDD()
        self._view.update_page()




    def handleClassifica(self, e):
        self._view.txtOut.controls.clear()
        classificaMigliori, classificaPeggiori = self._model.getClassifiche(self.choiceTeam)
        self._view.txtOut.controls.append(ft.Text("Classifica migliori:"))
        for m in classificaMigliori:
            self._view.txtOut.controls.append(ft.Text(f"{m[0]}({m[1]})"))

        self._view.txtOut.controls.append(ft.Text("\n\n"))

        self._view.txtOut.controls.append(ft.Text("Classifica peggiori:"))
        for p in classificaPeggiori:
            self._view.txtOut.controls.append(ft.Text(f"{p[0]}({p[1]})"))

        self._view.update_page()

    def readDDTeam(self, e):
        if e.control.data is None:
            self.choiceTeam = None
        else:
            self.choiceTeam = e.control.data
