import flet as ft


def main(page: ft.Page):
    page.floating_action_button=ft.FloatingActionButton(
        icon=ft.Icons.AD_UNITS,
        
    )
    page.floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_DOCKED
    
    page.appbar=ft.AppBar(
        leading=ft.IconButton(icon=ft.icons.MENU),
        title=ft.Text("Barra Flotante"),
        center_title=True,
        bgcolor=ft.Colors.GREEN_ACCENT_200
    )
    page.bottom_appbar=ft.BottomAppBar(
        bgcolor=ft.Colors.AMBER_700,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.PHONELINK_LOCK_ROUNDED,icon_color=ft.Colors.WHITE),
                ft.IconButton(icon=ft.Icons.FACE,icon_color=ft.Colors.WHITE),
                ft.IconButton(icon=ft.Icons.G_MOBILEDATA_OUTLINED,icon_color=ft.Colors.WHITE),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.Icons.RADIO,icon_color=ft.Colors.WHITE),
                ft.IconButton(icon=ft.Icons.GPS_FIXED_OUTLINED,icon_color=ft.Colors.WHITE),
                ft.IconButton(icon=ft.Icons.CARD_TRAVEL,icon_color=ft.Colors.WHITE),

                
            ]
        )
    )
    page.add(
       ft.Text("App")
    )


ft.app(main)
