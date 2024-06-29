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
        self._title = ft.Text("TdP 2024 - Esame 23/5/2023", color="orange", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.txtInAnno = ft.TextField(label="Anno", width=300)
        self.txtInSalario = ft.TextField(label="Salario", width=300)
        row1 = ft.Row([self.txtInAnno, self.txtInSalario], alignment=ft.MainAxisAlignment.CENTER)

        self.btnGraph = ft.ElevatedButton(text="Crea Grafo", width=600, on_click=self._controller.handle_graph)
        row2 = ft.Row([self.btnGraph], alignment=ft.MainAxisAlignment.CENTER)

        self.btnGrado = ft.ElevatedButton(text="Grado Massimo", width=200, on_click=self._controller.handleGradoMax)
        self.btnConnesse = ft.ElevatedButton(text="Calcola Connesse", width=200, on_click=self._controller.handleConnesse)
        self.btnDT = ft.ElevatedButton(text="Dream Team", width=200, on_click=self._controller.handleDreamTeam)

        row3 = ft.Row([self.btnGrado, self.btnConnesse, self.btnDT], alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1,row2,row3)


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
