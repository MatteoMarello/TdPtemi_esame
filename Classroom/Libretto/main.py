import flet as ft
from view import View
from controller import Controller


def main(page: ft.Page):
    v = View(page)  # Il view è l'unico che conosce la pagina e che quindi potrà modificarla
    c = Controller(v)  # Il controllore è l'unico che conosce il modello
    v.setController(c)
    v.caricaInterfaccia()


ft.app(target=main)