import flet as ft
from Lab.Lab10.UI.view import View
from Lab.Lab10.model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._dd.options.clear()
        self._view._txt_result.controls.clear()
        anno = self._view._txtAnno.value
        try:
            intAnno = int(anno)
            if intAnno < 1816 or intAnno > 2006:
                self._view._txt_result.controls.append(ft.Text(f'Devi inserire un anno compreso tra il 1816 e il 2006.'))
            else:
                self._model.creaGrafo(intAnno)
                self._view._txt_result.controls.append(ft.Text('Grafo correttamente creato!'))
                numConnComp = self._model.getNumConnectedComp()
                self._view._txt_result.controls.append(ft.Text(f'Il grafo ha {numConnComp} componenti connesse.'))
                dettagliNodi = self._model.calcolaDettagliNodi()
                self._view._txt_result.controls.append(ft.Text('Di seguito il dettaglio sui nodi:'))
                for dettaglio in dettagliNodi:
                    self._view._txt_result.controls.append(ft.Text(f'{dettaglio[0]} -- {dettaglio[1]} vicini'))

                self._view._dd.disabled = False
                self._view._btnStatiRagg.disabled = False
                countries = self._model.getCountries()
                for country in countries:
                    self._view._dd.options.append(ft.dropdown.Option(text=country.StateNme,
                                                         data=country,
                                                         on_click=self.readDDCountry))

        except ValueError:
            self._view._txt_result.controls.append(ft.Text(f'Devi inserire un numero valido!'))

        self._view.update_page()

    def handleStatiRaggiungibili(self, e):
        self._view._txt_result.controls.clear()
        if self._countryDD is None:
            self._view._txt_result.controls.append(ft.Text(f'Devi prima selezionare uno stato dal menù a tendina!'))
            self._view.update_page()
            return
        else:
            statiRaggiungibili = self._model.getNodiRaggiungibiliIterativo(self._countryDD)
            for country in statiRaggiungibili:
                self._view._txt_result.controls.append(ft.Text(country))

        self._view.update_page()

    def readDDCountry(self, e):
        if e.control.data is None:
            self._countryDD = None
        else:
            self._countryDD = e.control.data