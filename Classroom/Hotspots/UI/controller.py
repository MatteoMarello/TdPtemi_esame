import flet as ft
from Classroom.Hotspots.model.model import Model
from Classroom.Hotspots.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        self._view.txt_result.controls.clear()
        provider = self._view._ddProvider.value
        if provider is None:
            print("Seleziona un provider")
            self._view.txt_result.controls.append(ft.Text("Seleziona un provider"))
            self._view.update_page()
            return

        soglia = self._view._txtInDistanza.value
        if soglia == "":
            self._view.txt_result.controls.append(ft.Text("Distanza non inserita"))
            self._view.update_page()
            return

        try:
            sogliaFloat = float(soglia)

        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Distanza deve essere un float"))
            self._view.update_page()
            return

        self._model.buildGraph(provider, sogliaFloat)
        nN, nE = self._model.getGraphDetails()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {nN}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {nE}"))
        self.fillDDTarget()
        self._view.update_page()

    def handleAnalizzaGrafo(self, e):
        self._view.txt_result.controls.clear()
        nN, nE = self._model.getGraphDetails()
        if nN == 0 and nE:
            self._view.txt_result.controls.append(ft.Text("Attenzione grafo vuoto!"))
            self._view.update_page()
            return

        lista = self._model.getNodesMostVicini()
        self._view.txt_result.controls.append(ft.Text("Nodi con più vicini"))
        for l in lista:
            self._view.txt_result.controls.append(ft.Text(f"{l[0]} -- {l[1]}"))

        self._view.update_page()

    def handleCalcolaPercorso(self, e):
        target = self._choiceLocation
        self._view.txt_result.controls.clear()
        if target is None:
            self._view.controls.append(ft.Text("Seleziona un target."))
            self._view.update_page()
            return

        substring = self._view._txtInString.value
        if substring == "":
            self._view.txt_result.controls.append(ft.Text("Attenzione, stringa non inserita!"))
            self._view.update_page()
            return

        path, source = self._model.getCammino(target, substring)
        if path == []:
            self._view.txt_result.controls.append(ft.Text(f"Non ho trovato un cammino fra {source} e {target}"))
            self._view.update_page()
            return

        self._view.controls.append(ft.Text(f"Ho trovato un cammino fra {source} e {target}:"))
        for p in path:
            self._view.txt_result.controls.append(ft.Text(f"{p}"))
        self._view.update_page()


    def fillDDProvider(self):
        providers = self._model.getAllProviders()
        providers.sort()
        # Modo 1
        """
        for p in providers:
            self._view._ddProvider.options.append(ft.dropdown.Option(p))
        """
        # Modo 2
        providersDD = map(lambda x: ft.dropdown.Option(x), providers)
        self._view._ddProvider.options.extend(providersDD)


        self._view.update_page()

    def fillDDTarget(self):
        locations = self._model.getAllLocations()
        locationsDD = map(lambda x: ft.dropdown.Option(data=x, text=x.Location, on_click=self.readChoiceLocation), locations)
        self._view._ddTarget.options.extend(locationsDD)

    def readChoiceLocation(self, e):
        if e.control.data is None:
            self._choiceLocation = None
        else:
            self._choiceLocation = e.control.data