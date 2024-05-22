import flet as ft
from Classroom.FlightDelays.model.model import Model
from Classroom.FlightDelays.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self, e):
        pass

    def handleConnessi(self, e):
        pass

    def handleCercaItinerario(self, e):
        pass


