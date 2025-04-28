import flet as ft
#importacion de sqlite3
import sqlite3

#Paso1. Crear la base de datos/ Conexion de la base de datos
conexion=sqlite3.connect("basedatos.db")
acceso=conexion.cursor()

#Paso2. Crear una tabla
acceso.execute("""CREATE TABLE IF NOT EXISTS productos(
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               nombre TEXT NOT NULL,
               precio INTEGER,
               cantidad INTEGER,
               imagen TEXT NOT NULL) 
               """)

#PASO3. EJECUTAR LA CONSULTA SQL
conexion.commit()




def pantalla3():
    return ft.Column(
        controls=[
            ft.Text("Pantalla 3")
        ]

    )