import flet as ft
from time import sleep

def main(page: ft.Page): # main riceve sempre in input page: ft.Page
    txtIn = ft.Text(value="Buongiorno TdP 2024!", color="red")
    page.controls.append(txtIn)
    page.update()

    # Oppure, per aggiungere del testo in maniera più veloce posso scrivere direttamente:
    page.add(ft.Text(value="Quest'anno in Python!"))

    """
    for i in range(1,101 ):
        txtOut.value = "Counter: " + str(i)
        txtOut.update()
        sleep(1)
    """
    def handleButton(e): # Tutti i metodi che vengono chiamati dalle interfacce grafiche ricevono in input un evento e! Quando clicco un bottone genero un evento che viene passato come ingresso al metodo!
        lv.controls.append(ft.Text("Tasto Cliccato!"))
        lv.update()

    txt1 = ft.Text(value="Colonna 1", color="red")
    txt2 = ft.Text(value="Colonna 2", color="blue")
    btn = ft.ElevatedButton(text="Premi qui!", on_click=handleButton)

    row = ft.Row([txt1,txt2,btn])
    txtOut = ft.Text(value="", color="green", size=24)

    page.add(row,txtOut)

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    page.add(lv)


ft.app(target=main, view=ft.AppView.FLET_APP)