import flet as ft


def main(page: ft.Page):
    #APPBAR PARA IOS
    #page.appbar=ft.CupertinoAppBar(
     #   leading=ft.IconButton(icon=ft.icons.MENU,on_click=lambda evento: page.open(navegacionLateral)) ,
      #  middle=ft.Text("Mi aplicacion"),
        #bgcolor=ft.colors.RED
    #)
    #APP BAR ANDROID
    page.appbar=ft.AppBar(
        leading=ft.IconButton(icon=ft.icons.MENU),
        title=ft.Text("AppBar Android"),
        center_title=True,
        bgcolor=ft.Colors.AMBER_300,
    )

    navegacionLateral=ft.NavigationDrawer(
        controls=[
            ft.Container(height=15),
            ft.NavigationDrawerDestination(
                label="Inicio",
                icon=ft.Icons.HOME,
            ),
            ft.NavigationDrawerDestination(
                label="Productos",
                icon=ft.Icons.STORE
            ),
            ft.NavigationDrawerDestination(
                label="Servicios",
                icon=ft.Icons.SETTINGS_PHONE_ROUNDED
            ),
        ],
    )

    navegacion3=ft.NavigationRail(
        selected_index=0,
        min_width=60,
        min_extended_width=300,
        group_alignment=-0.5,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.HOME_MAX_ROUNDED,
                label="Inicio",
                indicator_color=ft.colors.BLUE_ACCENT
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.PASSWORD,
                label="Productos"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.FACE_3,
                label="Servicios"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.CABLE,
                label="Ajustes"
            )
        ],
        leading=ft.Image(src='https://images.squarespace-cdn.com/content/v1/6788d438405dc03eabea6c99/1737020479975-V3ZE94TGRALPK7D15TNY/image-asset.png',width=40),
        on_change=lambda evento: print("Seleccion de pantalla ",evento.control.selected_index),

        
        )
    
    page.add(
        #   Agregar un contenedor
        #fila row horizontal
        #columna column vertical
        ft.Row([
            #navegacionLateral,
            navegacion3,
            ft.VerticalDivider(width=1,color=ft.colors.AMBER_400),
            ft.Column(
                [
                    ft.Text("Pantalla")
                ]
            )

        ],
        
        expand=True
        )
    )


ft.app(main)
