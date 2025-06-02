import flet as ft
#Importacion de las dependencias
import requests
import firebase
import pyrebase
import webbrowser

#PASO 1. CONFIGURAR LAS CREDENCIALES DE FIREBASE
firebaseConfig = {
 
}

#PASO 2. INICIALIZAR FIREBASE
firebaseIniciar=pyrebase.initialize_app(firebaseConfig)
autentificacion=firebaseIniciar.auth()


def main(page: ft.Page):
    resultado=ft.Text(value="")

    #Paso 3. Conectar firebase con la interfaz
    #FUNCION PARA UTILIZAR GOOGLE
    def loginGoogle(e):
        resultado.value=("Iniciando Sesión...",e)
        page.update()
        #URL DE COMUNICACION CON FIREBASE
        urlAuth=(f"https://aplicacionesiiautentificacion.web.app")

        #Abrir el navegador
        webbrowser.open(urlAuth)



    
    # DE LA INTERFAZ
    page.add(
        ft.Text("Iniciar Sesión con Google"),
        ft.CupertinoFilledButton(
            "Iniciar Sesión con Google",
            on_click=loginGoogle),
        resultado
       
    )



ft.app(main)


