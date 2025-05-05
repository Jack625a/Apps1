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

#Agregar datos (insercion)
def agregarEstudiantes(nombre,carrera,edad,imagen):
    data={
        "fields":{
            "nombre":nombre,
            "carrera":carrera,
            "edad":edad,
            "imagen":imagen
        }
    }
    respuesta=requests.post(urlAirtable, headers=HEADERS, json=data)
    return respuesta.status_code==200 or respuesta.status_code==201

#funcion para eliminar datos
def eliminarDatos(id):
    #url endpoint
    url=f"{urlAirtable}/{id}"
    respuesta=requests.delete(url,headers=HEADERS)
    return respuesta.status_code==200





def main(page: ft.Page):
    resultado=ft.Text()
    lista_estudiante=ft.ListView(expand=True,padding=10)
     #Funcion para borrar datos
    def borrarEstudiante(id):
        if eliminarDatos(id):
            resultado.value="Estudiante eliminado"
        else:
            resultado.value="Error al eliminar"
        page.update()
    obtenerEstudinates()
    #cargado de datos a la lista
    def cargarDatos():
        lista_estudiante.controls.clear()
        registros=obtenerEstudinates()
        for registro in registros:
            datos=registro["fields"]
            estudianteId=registro["id"]
            tarjeta=ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text(f"Nombre: {datos.get('nombre')}"),
                        ft.Text(f"Carrera: {datos.get('carrera')}"),
                        ft.CupertinoFilledButton(text="Eliminar Estudiante",
                                                 on_click=lambda e, id=estudianteId:borrarEstudiante(id)
                                                )
                    ]),
                    padding=15
                    
                )
            )
            lista_estudiante.controls.append(tarjeta)
            page.update


    def mostrarEstudiantes(evento):
        registros=obtenerEstudinates()
        lista.controls.clear()
        for i in registros:
            datos=i['fields']
            lista.controls.append(
            ft.Text(f"{datos.get('nombre','')} - {datos.get('carrera','')} -{datos.get('edad','')} - url Imagen {datos.get('imagen')}"),
            
            )
        page.update()

    #Componentes
    botonMostrar=ft.CupertinoButton(
        text='Mostrar',
        on_click=mostrarEstudiantes
        )
    lista=ft.Column()

    #campos de entrada 
    nombre=ft.TextField(label="Ingrese su nombre: ")
    carrera=ft.TextField(label="Ingrese su carrera: ")
    edad=ft.TextField(label="Ingrese su edad: ")
    imagen=ft.TextField(label="Ingrese su imagen: ")

    #funcion para guardar los datos en Airtable
    def guardarDatos(e):
        exitoso=agregarEstudiantes(nombre.value,carrera.value,edad.value,imagen.value)
        if exitoso:
            resultado.value="Estudiante agregado correctamente"
            nombre.value=carrera.value=edad.value=imagen.value=""
            obtenerEstudinates()
        else:
            resultado.value="Error al agregar los datos..."
        page.update()

   

    page.add(
        botonMostrar,lista,
        #formulario para enviar datos al servidor
        ft.Divider(),
        ft.Text("Agregado de Estudiantes", size=25),
        nombre,carrera,edad,imagen,
        ft.CupertinoFilledButton("Agregar Estudiante", on_click=guardarDatos),
        resultado,
        ft.Divider(),
        ft.Text("Eliminacion de Datos", size=25),
        ft.Text("Lista de Estudiante"),
        ft.CupertinoButton(text="Lista Estudiante", on_click=cargarDatos()),
        lista_estudiante,


        
    )


ft.app(main)
