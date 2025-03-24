import flet as ft


def main(page: ft.Page):
   
    page.add(
        ft.Row([
            ft.Container(
                content=ft.Text("Prueba"),
                margin=10,
                padding=10,
                width=300,
                height=150,
                alignment=ft.alignment.center_left,
                bgcolor=ft.Colors.RED_700
            ),
            ft.Container(
                content=ft.CupertinoFilledButton(text="bOTON"),
                margin=10,
                padding=10,
                bgcolor=ft.Colors.GREEN_700
            ),
            ft.Container(
                content=ft.CupertinoFilledButton(text="bOTON"),
                margin=10,
                padding=10,
                bgcolor=ft.Colors.GREEN_700
            ),
            ft.Container(
                content=ft.CupertinoFilledButton(text="bOTON"),
                margin=10,
                padding=10,
                bgcolor=ft.Colors.GREEN_700
            ),
            ft.Container(
                content=ft.CupertinoFilledButton(text="bOTON"),
                margin=10,
                padding=10,
                bgcolor=ft.Colors.GREEN_700
            ),
            ft.Container(
                content=ft.CupertinoFilledButton(text="bOTON"),
                margin=10,
                padding=10,
                bgcolor=ft.Colors.GREEN_700
            ),
            ft.Container(
                content=ft.CupertinoFilledButton(text="bOTON"),
                margin=10,
                padding=10,
                bgcolor=ft.Colors.GREEN_700
            ),
            ft.Container(
                content=ft.CupertinoFilledButton(text="bOTON"),
                margin=10,
                padding=10,
                bgcolor=ft.Colors.GREEN_700
            )
        ],scroll=ft.ScrollMode.ADAPTIVE)
      
    )


ft.app(main)
