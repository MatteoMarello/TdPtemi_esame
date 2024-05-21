import flet as ft
from Lab.Lab11.UI.view import View
from Lab.Lab11.model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        pass


    def handle_graph(self, e):
        pass



    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
