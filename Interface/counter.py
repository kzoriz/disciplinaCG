import flet as ft
from tkinter import filedialog


def main(page: ft.Page):
    def get_img(e):
        # page.add(ft.Text("Clicked!"))
        filename = filedialog.askopenfilename()
        print('foto: ', filename)
        print(type(filename))
        img = ft.Image(
            src=f'{filename}',
            width=300,
            height=300,
            fit=ft.ImageFit.CONTAIN,
        )
        page.add(img)

    page.title = "Computação Grafica"
    page.add(
        ft.Row(controls=[
            ft.ElevatedButton(text="Open", on_click=get_img),

        ])
    )
    # page.add()
    page.update()



ft.app(target=main)
