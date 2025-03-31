import flet as ft


def main(page: ft.Page):
    #page.title("Navegacion")
    page.navigation_bar=ft.CupertinoNavigationBar(
        bgcolor=ft.Colors.GREEN_700,
        #inactive_color=ft.Colors.YELLOW_700,
        #active_color=ft.Colors.RED_500,
        destinations=[
            ft.NavigationBarDestination(
                label="Inicio",
                icon=ft.Icons.HOME,
            ),
            ft.NavigationBarDestination(
                label="Productos",
                icon=ft.Icons.STORE
            ),
            ft.NavigationBarDestination(
                label="Ajustes",
                icon=ft.Icons.ACCESS_ALARM_OUTLINED
            ),
            ft.NavigationBarDestination(
                label="Perfil",
                icon=ft.Icons.ACCOUNT_TREE
            )
        ]
    )

    drawer=ft.NavigationDrawer(
        controls=[
            ft.Container(height=15),
            ft.NavigationDrawerDestination(
                label="Inicio",
                icon=ft.Icons.HOME_MAX_SHARP
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                label="Servicios",
                icon=ft.Icons.ACCOUNT_BALANCE_ROUNDED
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                label="Opcion",
                icon=ft.Icons.MENU
            ),
        ],
    )
   
    page.add(
        ft.CupertinoFilledButton(text="mostrar", on_click=lambda e:page.open(drawer)),
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
