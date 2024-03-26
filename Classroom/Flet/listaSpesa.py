import flet as ft
def main(page: ft.Page):
    # Row 1
    def addCheckbox(e):
        strToAdd = txtIn.value
        txtIn.value = ""
        if strToAdd == "":
            return

        page.add(ft.Checkbox(label=strToAdd, value=False))

    txtIn = ft.TextField(label="Aggiungi un elemento")
    btnAdd = ft.ElevatedButton(text="Add", on_click=addCheckbox)
    row1 = ft.Row([txtIn, btnAdd], alignment=ft.MainAxisAlignment.CENTER)

    page.add(row1)

ft.app(target=main)