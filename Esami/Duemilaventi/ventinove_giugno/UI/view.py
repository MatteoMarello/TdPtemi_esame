import flet as ft

class View():
    def __init__(self, page: ft.Page):
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
        self._title = ft.Text("TdP 2024 - Esame 29/6/2020", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.ddyear = ft.Dropdown(label="Anno", width=400)
        self.ddyear.options.append(ft.dropdown.Option("2004"))
        self.ddyear.options.append(ft.dropdown.Option("2005"))
        self.ddyear.options.append(ft.dropdown.Option("2006"))
        self.btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo", width=200, on_click=self._controller.handleCreaGrafo)
        row1 = ft.Row([self.ddyear, self.btnCreaGrafo], alignment=ft.MainAxisAlignment.CENTER)

        self.ddRegisti = ft.Dropdown(label="Regista", width=400)
        self.btnRegistiAdiacenti = ft.ElevatedButton(text="Registi Adiacenti", width=200, on_click=self._controller.handleRegistiAdiacenti)
        row2 = ft.Row([self.ddRegisti, self.btnRegistiAdiacenti], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1, row2)

        self.txtInAttoriCond = ft.TextField(label="Attori Condivisi", width=400)
        self.btnCercaRegistiAffini = ft.ElevatedButton(text="Cerca Registi Affini", width=200, on_click=self._controller.handleCercaRegisti)
        row3 = ft.Row([self.txtInAttoriCond, self.btnCercaRegistiAffini], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row3)

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
