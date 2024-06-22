import flet as ft
from Esami.Duemilaventi.tre_giugno.model.model import Model
from Esami.Duemilaventi.tre_giugno.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDD(self):
        pass


    def handleCreaGrafo(self, e):
        self._view.txtOut.controls.clear()
        avgGoals = float(self._view.txtInGoal.value)
        self._model.buildGraph(avgGoals)
        nN, nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text("Grafo correttamente creato!"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {nE}"))
        self._view.update_page()


    def handleToplPlayer(self, e):
        self._view.txtOut.controls.clear()
        topPlayer, listBeatenPlayers = self._model.getTopPlayer()

        self._view.txtOut.controls.append(ft.Text(F"Top Player: {topPlayer}"))
        self._view.txtOut.controls.append(ft.Text("Avversari battuti:"))
        for p in listBeatenPlayers:
            self._view.txtOut.controls.append(ft.Text(F"{p[0]} | {p[1]}"))

        self._view.update_page()



    def handleDreamTeam(self, e):
        self._view.txtOut.controls.clear()
        k = int(self._view.txtInGiocatori.value)
        dreamTeam, gradoTit = self._model.getDreamTeam(k)
        self._view.txtOut.controls.append(ft.Text(f"Grado di titolarità: {gradoTit}"))
        self._view.txtOut.controls.append(ft.Text("DREAM TEAM:"))
        for p in dreamTeam:
            self._view.txtOut.controls.append(ft.Text(f"{p}"))

        self._view.update_page()


