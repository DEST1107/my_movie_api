from fastapi import FastAPI #importa la clase FastAPI de fastapi

app = FastAPI() #crea una instancia de la clase FastAPI
app.title = 'Mi primera aplicación de películas y análisis de datos'
app.version = '1.0.1'
@app.get('/', tags=['Home'])
def message(): #definiendo una ruta
    return 'Hello World' #devuelve un diccionario


