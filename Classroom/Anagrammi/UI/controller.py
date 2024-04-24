import flet as ft
from Classroom.Anagrammi.UI.view import View
from Classroom.Anagrammi.model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def calcola_anagrammi(self, e):
        self._view.lst_wrong.controls.clear()
        self._view.lst_correct.controls.clear()
        parola = self._view.txt_word.value
        anagrammi_parola = self._model.calcola_anagrammi(parola)
        anagrammi_corretti = set()
        anagrammi_errati = set()
        for word in anagrammi_parola:
            if word in self._model.parole_dizionario:
                anagrammi_corretti.add(word)
            else:
                anagrammi_errati.add(word)

        if anagrammi_corretti:
            for parola_corretta in anagrammi_corretti:
                self._view.lst_correct.controls.append(ft.Text(parola_corretta))
        else:
            self._view.lst_correct.controls.append(ft.Text("Non sono presenti anagrammi corretti della parola indicata"))

        if anagrammi_errati:
            for parola_errata in anagrammi_errati:
                self._view.lst_wrong.controls.append(ft.Text(parola_errata))
        else:
            self._view.lst_correct.controls.append(ft.Text("Non sono presenti anagrammi errati della parola indicata"))


        self._view.update_page()

    def reset(self, e):
        self._view.lst_wrong.controls.clear()
        self._view.lst_wrong.controls.append(ft.Text("----"))
        self._view.lst_correct.controls.clear()
        self._view.lst_correct.controls.append(ft.Text("----"))
        self._view.txt_word.value = ""
        self._view.update_page()
