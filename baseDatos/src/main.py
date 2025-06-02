import flet as ft
#Importacion de las solicitudes al servidor http
import requests 

#VARIABLES DE AUTETIFICACION
token='patGPWZYLYQUEgqnD.fcca93cd15b37bc8944d48a58c2bc5a31a5ff8329dcd90f2800b2f3d548dbc03'
idBase='appxEsWXVhSbTo9tS'
nombreTabla='estudiante'
HEADERS={
    "Authorization":f'Bearer {token}',
    "Content-Type":"application/json"
}
urlAirtable=f'https://api.airtable.com/v0/{idBase}/{nombreTabla}'



#Funciones para obtener a los estudiantes
#METODO PARA OBTENER GET
def obtenerEstudinates():
    respuesta=requests.get(urlAirtable,headers=HEADERS)
    if respuesta.status_code==200:
        return respuesta.json()["records"]
    else:
        print("Error al obtner los datos")
        return []

#Agregar datos (insercion)
# METODO PARA INSERTAR POST
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
#NOTA: METODO PARA ELIMINAR ES DELETE
def eliminarDatos(id):
    #url endpoint
    url=f"{urlAirtable}/{id}"
    respuesta=requests.delete(url,headers=HEADERS)
    return respuesta.status_code==200

#funcion para Actulizar los datos
#NOTA METODO PARA ACTULIZAR DATOS ES PATCH
def actualizarDatos(id,nombre,carrera,edad,imagen):
    data={
        "fields":{
            "nombre":nombre,
            "carrera":carrera,
            "edad":edad,
            "imagen":imagen
        }
    }
    url=f"{urlAirtable}/{id}"
    respuesta=requests.patch(url, headers=HEADERS, json=data)
    return respuesta.status_code in [200,201]



#interfaz
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
    #cargado de datos a la lista para eliminacion
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
            page.update()


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

    #campos para editar
    selectorEstudiante=ft.Dropdown(label="Seleccione al estudiante", options=[])
    nombreEditar=ft.TextField(label="nombre: ")
    carreraEditar=ft.TextField(label="carrera")
    edadEditar=ft.TextField(label="edad")
    imagenEditar=ft.TextField(label="imagen")

    #variable para editar 
    estudianteIdEditar=ft.Text(visible=False)

    #cargado de los estudiante para el selector 
    def cargarSelector():
        selectorEstudiante.options.clear()
        registros=obtenerEstudinates()
        for i in registros:
            datos=i["fields"]
            id_ =i["id"]
            selectorEstudiante.options.append(ft.dropdown.Option(f"{datos.get('nombre','')} - {datos.get('id','')}"))
        page.update()
    #Estudiante seleccionado para la actualizacion
    def estudianteSeleccionado(e):
        if not selectorEstudiante.value:
            return
        # Verificar que contiene '|'
        if "|" in selectorEstudiante.value:
            id_, _ = selectorEstudiante.value.split("|", 1)
        else:
            id_ = selectorEstudiante.value  # Por si solo viene el id
        estudianteIdEditar.value = id_
        registros = obtenerEstudinates()
        for reg in registros:
            if reg["id"] == id_:
                datos = reg["fields"]
                nombreEditar.value = datos.get("nombre", "")
                carreraEditar.value = datos.get("carrera", "")
                edadEditar.value = datos.get("edad", "")
                imagenEditar.value = datos.get("imagen", "")
                break
        page.update()

    selectorEstudiante.on_change=estudianteSeleccionado
    



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

   
    cargarSelector()
    page.update()
    
    page.add(
        ft.Column(
            [
                ft.Text("SISTEMA DE ESTUDIANTES",size=30),
                botonMostrar,lista,
                #formulario para enviar datos al servidor
                ft.Divider(),
                ft.Text("Agregado de Estudiantes", size=30),
                nombre,carrera,edad,imagen,
                ft.CupertinoFilledButton("Agregar Estudiante", on_click=guardarDatos),
                resultado,
                ft.Divider(),
                ft.Text("Eliminacion de Datos", size=25),
                ft.Text("Lista de Estudiante"),
                ft.CupertinoButton(text="Lista Estudiante", on_click=cargarDatos()),
                lista_estudiante,
                ft.Divider(),
                ft.Text("Actualizacion de Datos", size=30),
                selectorEstudiante,
                nombreEditar,carreraEditar,edadEditar,imagenEditar,
                ft.CupertinoFilledButton("Actualizar")

            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
        

        
    )


ft.app(main)
