import flet as ft
#Importar las pantallas
from pantalla1 import pantalla1
from pantalla2 import pantalla2
from pantalla3 import pantalla3
from pantalla4 import pantalla4


def main(page: ft.Page):
    page.appbar=ft.AppBar(
        leading=(ft.IconButton(icon=ft.icons.MENU)),
        title=(ft.Text("Navegacion Modular")),
        center_title=True
    )
    #Contenedor para el contenido de las pantallas
    contenido=ft.Container(expand=True)
    
    #funcion para controlas las vistas de cada tab
    def cambiarPantalla(pantalla):
        if pantalla==0:
            contenido.content=pantalla1()
            
        elif pantalla==1:
            contenido.content=pantalla2()
            
        elif pantalla==2:
            contenido.content=pantalla3()
            
        elif pantalla==3:
            contenido.content=pantalla4()     

        page.update()

    #Barra de Navegacion
    barraNavegacion=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(label="Pantalla1",icon=ft.icons.ACCOUNT_BOX_ROUNDED),
            ft.NavigationBarDestination(label="Pantalla2",icon=ft.icons.PAGES),
            ft.NavigationBarDestination(label="Pantalla3", icon=ft.icons.FACE),
            ft.NavigationBarDestination(label="Pantalla4", icon=ft.icons.STACKED_LINE_CHART_OUTLINED)
        ],
        on_change=lambda e: cambiarPantalla(e.control.selected_index),
        

    )
    page.update()
    cambiarPantalla(0)

    
    


    page.add(
      ft.Column(
          [
            contenido,
            barraNavegacion
          ],
          expand=True
      )
    )


ft.app(main)
