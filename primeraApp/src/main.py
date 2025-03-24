#Importacion de flet
import flet as ft

def main(page: ft.Page):

    def irFlet(e):
        page.launch_url('flet.dev')
        page.update()

    videos=["https://user-images.githubusercontent.com/28951144/229373695-22f88f13-d18f-4288-9bf1-c3e078d83722.mp4","https://user-images.githubusercontent.com/28951144/229373695-22f88f13-d18f-4288-9bf1-c3e078d83722.mp4"]
    
    page.add(
        ft.Text(value="Primera Aplicacion",color=ft.colors.RED_700, size=30, weight=ft.FontWeight.BOLD),
        ft.Button(text="Boton 1"),
        ft.CupertinoFilledButton(text="Boton Cupertino",icon=ft.icons.FACE),
        ft.FilledButton(text="Boton filled",bgcolor=ft.colors.CYAN_700, color=ft.colors.BLACK),
        ft.OutlinedButton(text="Boton con borde"),
        ft.FloatingActionButton(icon=ft.icons.ADD),
        ft.IconButton(icon=ft.icons.TIKTOK),
        ft.TextField(keyboard_type=ft.KeyboardType.EMAIL, max_length=8),
        ft.TextField(password=True, can_reveal_password=True, width=200),
        ft.Checkbox(label="Opcion 1"),
        ft.CupertinoCheckbox(label="Opcion2"),
        ft.Chip(label=ft.Text(value="Prueba"),leading=ft.Icon(ft.icons.CAR_CRASH),on_click=irFlet, bgcolor=ft.Colors.INDIGO_600,selected_color=ft.Colors.WHITE,),
        ft.Chip(label=ft.Text(value="Prueba2"),leading=ft.Icon(ft.icons.ASSESSMENT_OUTLINED)),
        ft.Chip(label=ft.Text(value="Prueba3"),leading=ft.Icon(ft.icons.ADD)),
        ft.Image(src="https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvqtqh3l2m2hdobmdcqol.png",width=100,border_radius=ft.BorderRadius(10,10,10,10)),
        ft.Video([videos],volume=100,autoplay=True,show_controls=True,expand=True,width=300,height=300)



      
    )


ft.app(main)
