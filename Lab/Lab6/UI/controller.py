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
        self._view.lv.controls.clear()
        anno = self._view.dd_anno.value
        if anno == "Nessun filtro":
            anno = None

        brand = self._view.dd_brand.value
        if brand == "Nessun filtro":
            brand = None

        codice_retailer = self._view.dd_retailer.value
        if codice_retailer == "Nessun filtro":
            codice_retailer = None

        topVendite = self._model.getTopVendite(anno, brand, codice_retailer)
        if not topVendite:
            self._view.lv.controls.append(ft.Text(f'Non risultano vendite di prodotti del brand {brand} dal retailer {self.retailer.nome}'))
        for vendita in topVendite:
            self._view.lv.controls.append(ft.Text(f'Data: {vendita['Data']}; Ricavo: {vendita['Ricavo']}; Retailer: {vendita['Retailer']}; Prodotto: {vendita['Prodotto']}\n'))

        self._view.update_page()

    def handleAnalizzaVendite(self,e):
        self._view.lv.controls.clear()
        anno = self._view.dd_anno.value
        if anno == "Nessun filtro":
            anno = None

        brand = self._view.dd_brand.value
        if brand == "Nessun filtro":
            brand = None

        codice_retailer = self._view.dd_retailer.value
        if codice_retailer == "Nessun filtro":
            codice_retailer = None

        analisiVendite = self._model.getAnalisiVendite(anno,brand,codice_retailer)
        if analisiVendite['numero_vendite'] == 0:
            analisiVendite['ricavi_totali'] = 0

        self._view.lv.controls.append(ft.Text(f'Statistiche vendite:\n', color="red", size=20))
        self._view.lv.controls.append(ft.Text(f'Giro d\'affari: {analisiVendite.get('ricavi_totali')}\n'))
        self._view.lv.controls.append(ft.Text(f'Numero vendite: {analisiVendite.get('numero_vendite')}\n'))
        self._view.lv.controls.append(ft.Text(f'Numero retailers coinvolti: {analisiVendite.get('numero_retailers')}\n'))
        self._view.lv.controls.append(ft.Text(f'Numero prodotti coinvolti: {analisiVendite.get('numero_prodotti')}\n'))

        self._view.update_page()



    def readRetailer(self, e):
        self.retailer = e.control.data
