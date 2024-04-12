import flet as ft

from Lab.Lab5.model.model import Model
from Lab.Lab5.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def aggiungiCorsi(self, dd: ft.Dropdown):
        corsi = self._model.getCorsi()
        for corso in corsi:
            dd.options.append(ft.dropdown.Option(text=corso.__str__(), key=corso.codins))
        return

    def handleCercaIscritti(self, e):
        if self._view._dd.value is None:
            self._view.create_alert("Seleziona prima un corso!")
        else:
            self._view._lv.controls.clear()
            codins = self._view._dd.value
            iscrittiCorso = self._model.getIscrittiCorso(codins)
            self._view._lv.controls.append(ft.Text(f'Ci sono {len(iscrittiCorso)} iscritti al corso!'))
            for iscritto in iscrittiCorso:
                self._view._lv.controls.append(ft.Text(f'{iscritto.__str__()}'))
                self._view.update_page()


    def handleCercaStudente(self, e):
        if self._view._textFieldMatricola.value == "":
            self._view.create_alert("Devi inserire una matricola!")
        else:
            self._view._textFieldNome.value = ""
            self._view._textFieldCognome.value = ""
            matricola = self._view._textFieldMatricola.value
            studente = self._model.getStudente(matricola)
            if studente:
                self._view._textFieldNome.value = studente['nome']
                self._view._textFieldCognome.value = studente['cognome']
                self._view.update_page()
            else:
                self._view.create_alert("Non è presente alcun studente con questa matricola!")

    def handleCercaCorsi(self, e):
        if self._view._textFieldMatricola.value == "":
            self._view.create_alert("Devi inserire una matricola!")
        else:
            matricola = self._view._textFieldMatricola.value
            studente = self._model.getStudente(matricola)
            if not studente:
                self._view.create_alert("Non è presente alcun studente con questa matricola!")
            else:
                self._model.getStudenti()
                self._view._lv.controls.clear()
                corsiStudente = self._model.getCorsiStudente(matricola)
                self._view._lv.controls.append(ft.Text(f'Lo studente {studente['nome']} {studente['cognome']} risulta iscritto a {len(corsiStudente)} corsi!'))
                for corso in corsiStudente:
                    self._view._lv.controls.append(ft.Text(corso.__str__()))

                self._view.update_page()




    def handeIscrizione(self, e):
        pass

