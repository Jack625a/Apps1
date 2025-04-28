import flet as ft
#Importacion de las solicitudes al servidor http
import requests

#VARIABLES DE AUTETIFICACION
token=''
idBase=''
nombreTabla='estudiante'
HEADERS={
    "Authorization":f'Bearer {token}',
    "Content-Type":"application/json"
}
urlAirtable=f'https://api.airtable.com/v0/{idBase}/{nombreTabla}'



#Funciones para obtener a los estudiantes
def obtenerEstudinates():
    respuesta=requests.get(urlAirtable,headers=HEADERS)
    if respuesta.status_code==200:
        return respuesta.json()["records"]
    else:
        print("Error al obtner los datos")
        return []

def main(page: ft.Page):

    def mostrarEstudiantes(evento):
        registros=obtenerEstudinates()
        lista.controls.clear()
        for i in registros:
            datos=i['fields']
            lista.controls.append(
            ft.Text(f"{datos.get('nombre','')} - {datos.get('carrera','')} -{datos.get('edad','')} ")   
            )
        page.update()

    #Componentes
    botonMostrar=ft.CupertinoButton(
        text='Mostrar',
        on_click=mostrarEstudiantes
        )
    lista=ft.Column()


  
    page.add(
        botonMostrar,lista
        
    )


ft.app(main)
