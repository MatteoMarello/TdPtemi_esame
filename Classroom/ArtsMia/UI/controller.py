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
        self._view._btnCompConnessa.disabled = False
        self._view.update_page()


    def handleCompConnessa(self,e):
        self._view._txt_result.controls.clear()
        idAdded = self._view._txtIdOggetto.value
        sizeConnessa = None
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

        self._view._btnCercaPercorso.disabled = False
        # Fill DD
        self._view._ddLun.disabled = False
        myOptsNum=list(range(2, sizeConnessa))
        # la funziona map() associa a un iterable una funzione. Quello che succede è che gli do una lista e una funzione, e il map()
        # applica a tutti gli oggetti della lista la funzione indicata. E mi restituisce in output una lista in cui ha applicato quella
        # funzione a tutti gli oggetti
        myOptsDD = map(lambda x: ft.dropdown.Option(x), myOptsNum)

        self._view._ddLun.options = myOptsDD

        self._view.update_page()

    def handleCercaPercorso(self, e):
        lenght = int(self._view._ddLun.value)
        v0 = self._model.getObjByID(int(self._view._txtIdOggetto.value))
        path, peso = self._model.getBestPath(lenght, v0)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Percorso trovato con peso migliore uguale a {peso}"))

        self._view._txt_result.controls.append(ft.Text(f"Percorso:"))
        for p in path:
            self._view._txt_result.controls.append(ft.Text(f'{p}'))

        self._view.update_page()




