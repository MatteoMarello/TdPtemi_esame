import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None


    def load_interface(self):
        # title
        self._title = ft.Text("TdP 2024 - Esame 30/5/23", color="yellow", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.ddNazione = ft.Dropdown(label="Nazione", width=200)
        self._controller.fillDDNazioni()
        self.ddAnno = ft.Dropdown(label="Anno", width=200)
        self.ddAnno.options.append(ft.dropdown.Option("2015"))
        self.ddAnno.options.append(ft.dropdown.Option("2016"))
        self.ddAnno.options.append(ft.dropdown.Option("2017"))
        self.ddAnno.options.append(ft.dropdown.Option("2018"))
        self.txtInProd = ft.TextField(label="N. Prodotti", width=200)
        self.btnGrafo = ft.ElevatedButton(text="Crea Grafo", width=200, on_click=self._controller.handle_graph)
        row1 = ft.Row([self.ddNazione, self.ddAnno, self.txtInProd, self.btnGrafo], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1)

        self.ddRivenditore = ft.Dropdown(label="Rivenditore", width=200)
        self.btnAnalizza = ft.ElevatedButton(text="Analizza Componente", width=200, on_click=self._controller.handleAnalizza)

        row2=ft.Row([self.ddRivenditore, self.btnAnalizza], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)


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
