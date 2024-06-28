import flet as ft
from Esami.Duemilaventitre.ventiquattro_gennaio.model.model import Model
from Esami.Duemilaventitre.ventiquattro_gennaio.UI.view import View
from decimal import Decimal

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDDAnno(self):
        self._view.ddAnno.options.append(ft.dropdown.Option("2015"))
        self._view.ddAnno.options.append(ft.dropdown.Option("2016"))
        self._view.ddAnno.options.append(ft.dropdown.Option("2017"))
        self._view.ddAnno.options.append(ft.dropdown.Option("2018"))


    def fillDDMethods(self):
        methods = self._model.getMethods()
        for m in methods:
            self._view.ddMetodo.options.append(ft.dropdown.Option(
                data=m,
                text=m,
                on_click=self.readChosenMethod
            ))


    def readChosenMethod(self, e):
        if e.control.data is None:
            self.chosenMethod = None
        else:
            self.chosenMethod = e.control.data


    def handle_graph(self, e):
        anno = int(self._view.ddAnno.value)
        metodo = self.chosenMethod.Order_method_code
        txtS = Decimal(self._view.txtInS.value)
        self._view.txtOut.controls.clear()

        if anno is None or metodo is None or txtS == "":
            self._view.txtOut.controls.append(ft.Text("Devi selezionare tutti i campi per poter creare il grafo!"))
            self._view.update_page()
            return

        self._model.buildGraph(anno, metodo, txtS)
        nN, nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici {nN}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi {nE}"))
        self._view.update_page()



    def handleProdottiRedditizi(self, e):
        self._view.txtOut.controls.clear()
        products = self._model.getProdottiRedditizi()
        for p in products:
            self._view.txtOut.controls.append(ft.Text(f"Prodotto: {p[0]}. Archi entranti: {p[1]}. Ricavi totali: {p[0].ricaviTotali}"))

        self._view.update_page()

    def handle_path(self, e):
        self._view.txtOut.controls.clear()
        percorso = self._model.getPercorso()
        for p in percorso:
            self._view.txtOut.controls.append(ft.Text(f"{p} --> Ricavi totali: {p.ricaviTotali}"))

        self._view.update_page()
