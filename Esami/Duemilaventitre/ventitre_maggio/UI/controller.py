import flet as ft
from Esami.Duemilaventitre.ventitre_maggio.model.model import Model
from Esami.Duemilaventitre.ventitre_maggio.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handle_graph(self, e):
        self._view.txtOut.controls.clear()
        anniDisponibili = self._model.getAnni()
        strAnno = self._view.txtInAnno.value
        strSalario = self._view.txtInSalario.value
        try:
            anno = int(strAnno)
            salario = int(strSalario)

        except ValueError:
            self._view.txtOut.controls.append(ft.Text("L'anno e il salario devono essere dei numeri interi!"))
            self._view.update_page()
            return

        if anno not in anniDisponibili:
            self._view.txtOut.controls.append(ft.Text("L'anno inserito non è disponibile!"))
            self._view.update_page()
            return

        salarioM = 1000000 * salario
        self._model.buildGraph(anno, salarioM)
        nN, nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text("Grafo correttamente creato!"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txtOut.controls.append(ft.Text(F"Numero di archi {nE}"))
        self._view.update_page()

    def handleGradoMax(self, e):
        self._view.txtOut.controls.clear()
        playerGradoMax = self._model.getPlayerGradoMax()
        self._view.txtOut.controls.append(ft.Text(f"Il giocatore di grado massimo è {playerGradoMax[0]}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi incidenti: {playerGradoMax[1]}"))
        self._view.update_page()


    def handleConnesse(self, e):
        self._view.txtOut.controls.clear()
        nConnComp = self._model.getNConnComp()
        self._view.txtOut.controls.append(ft.Text(f"Il grafo ha {nConnComp} componenti connesse."))
        self._view.update_page()


    def handleDreamTeam(self, e):
        dreamTeam, salary = self._model.getDreamTeam()
        self._view.txtOut.controls.clear()
        self._view.txtOut.controls.append(ft.Text(f"Il Dream Team ha un costo di {salary} milioni di dollari."))
        for p in dreamTeam:
            self._view.txtOut.controls.append(ft.Text(F"{p}"))
        self._view.update_page()