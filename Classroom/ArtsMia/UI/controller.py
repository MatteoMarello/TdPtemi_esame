import flet as ft
from Classroom.ArtsMia.model.model import Model
from Classroom.ArtsMia.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._view._txt_result.controls.clear()
        self._model.creaGrafo()
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato!"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodes()} nodi."))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumEdges()} archi."))
        self._view.update_page()

    def handleCompConnessa(self,e):
        self._view._txt_result.controls.clear()
        idAdded = self._view._txtIdOggetto.value
        try:
            intId = int(idAdded)
            if self._model.checkExistence(intId):
                self._view._txt_result.controls.append(ft.Text(f"L'oggetto {intId} è presente nel grafo!"))
                sizeConnessa = self._model.getConnessa(intId)
                self._view._txt_result.controls.append(ft.Text(f"La componente connessa che contiene {intId} ha dimensione {sizeConnessa}"))
            else:
                self._view._txt_result.controls.append(ft.Text(f"L'oggetto {intId} NON è presente nel grafo!"))
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Il valore inserito non è un intero!"))

        self._view.update_page()




