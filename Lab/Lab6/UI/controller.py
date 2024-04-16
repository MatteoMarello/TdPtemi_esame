import flet as ft
from Lab.Lab6.UI.view import View

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view: View = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.retailer = None

    def loadYears(self, dd: ft.Dropdown):
        years = self._model.getYears()
        for year in years:
            dd.options.append(ft.dropdown.Option(year))

    def loadBrands(self, dd: ft.Dropdown):
        brands = self._model.getBrands()
        for brand in brands:
            dd.options.append(ft.dropdown.Option(brand))

    def loadRetailers(self, dd:ft.Dropdown):
        retailers = self._model.getRetailers()
        for retailer in retailers:
            dd.options.append(ft.dropdown.Option(key=retailer.codice, text=retailer.nome, data=retailer, on_click = self.readRetailer))


    def handleTopVendite(self, e):
        anno = self._view.dd_anno.value
        if anno == "" or anno == "Nessun filtro":
            anno = None

        brand = self._view.dd_brand.value
        if brand == "" or brand == "Nessun filtro":
            brand = None

        codice_retailer = self._view.dd_retailer.value
        if codice_retailer == "" or codice_retailer == "Nessun filtro":
            codice_retailer = None

        topVendite = self._model.getTopVendite(anno, brand, codice_retailer)
        for vendita in topVendite:
            print(vendita)

    def handleAnalizzaVendite(self,e):
        pass

    def readRetailer(self, e):
        self.retailer = e.control.data
