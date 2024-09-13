from fastapi import FastAPI #importa la clase FastAPI de fastapi
from fastapi.responses import HTMLResponse #importa la clase HTMLResponse de fastapi
from movies_list import movies_list

app = FastAPI() #crea una instancia de la clase FastAPI
app.title = 'Mi primera aplicación de películas y análisis de datos'
app.version = '0.0.1'
@app.get('/', tags=['Home'])
def message(): #definiendo una ruta
    return HTMLResponse('<h1>Hola mundo</h1>') #devuelve un objeto HTMLResponse

@app.get('/movies', tags=['Movies'])#definiendo una ruta de la clase fastapi
def movies(): #definiendo una ruta
    return movies_list
@app.get('/movies/{id}', tags=['Movies'])#app get movies id
def get_movie(id:int): #definiendo una ruta
    for item in movies_list:
        if item['id'] == id:
            return item
    return []