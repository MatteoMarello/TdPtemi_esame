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
        self._title = ft.Text("TdP 2024 - Esame 2020-06-10", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls

        self.ddGenere = ft.Dropdown(label="Genere", width=300)
        self._controller.fillDDGenere()
        self.btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handleCreaGrafo, width=200)

        row1 = ft.Row(controls=[self.ddGenere, self.btnCreaGrafo], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1)

        self.ddAttore = ft.Dropdown(label="Attore", width=300)
        self.btnAttoriSimili = ft.ElevatedButton(text="Attori Simili", on_click=self._controller.handleAttoriSimili, width=200, disabled=True)

        row2 = ft.Row([self.ddAttore, self.btnAttoriSimili], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)

        self.txtInGG = ft.TextField(label="Giorni (n)", width=300)
        self.btnSimulazione = ft.ElevatedButton(text="Simulazione", width=200, on_click=self._controller.handleSimulazione, disabled=True)
        row3 = ft.Row([self.txtInGG, self.btnSimulazione], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row3)



        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=5, padding=5, auto_scroll=False)

        self._page.add(self.txt_result)
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
