import flet as ft

from UI.controller import Controller
from UI.view import View
from modello.voto import Libretto

def main(page: ft.Page):
    v = View(page)
    l = Libretto()
    c = Controller(v, l)
    v.setController(c)
    v.caricaInterfaccia()

ft.app(target=main)