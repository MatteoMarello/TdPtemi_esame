import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None


    def load_interface(self):
        # title
        self._title = ft.Text("TdP 2024 - Lab12: Prova tema d'esame", color="blue", size=24)
        self._page.controls.append(self._title)

        self.ddGenere = ft.Dropdown(label="Genere", width=300)
        self._controller.fillDDGeneri()
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo", width=200, on_click=self._controller.handleGrafo)
        row1=ft.Row([self.ddGenere, self._btnCreaGrafo], alignment=ft.MainAxisAlignment.CENTER)

        self.btnDeltaMax = ft.ElevatedButton(text="Delta Massimo", width=200, on_click=self._controller.handleDeltaMax)
        row2=ft.Row([self.btnDeltaMax], alignment=ft.MainAxisAlignment.CENTER)

        self.ddCanzoni = ft.Dropdown(label="Canzone", width=300)
        self.btnLista = ft.ElevatedButton(text="Crea Lista", width=200, on_click=self._controller.handleLista)

        row3 = ft.Row([self.ddCanzoni, self.btnLista], alignment=ft.MainAxisAlignment.CENTER)

        self.txtInMemoria = ft.TextField(label="Memoria", width=200)
        row4 = ft.Row([self.txtInMemoria], alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1,row2,row3,row4)


        self.txtOut = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txtOut)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
