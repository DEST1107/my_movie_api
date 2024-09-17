from fastapi import FastAPI, Body #importa la clase FastAPI de la libreria fastapi
from fastapi.responses import HTMLResponse #importa la clase HTMLResponse de la libreria fastapi

app = FastAPI() #estamos creando una instancia de FastAPI
app.title = "Mi aplicación con FastAPI" #asigna el valor de title a la instancia de la clase FastAPI
from movies_list import movies_list
app.version = "0.0.1"



@app.get('/', tags=["Home"]) #definimos una ruta de la clase FastAPI 
def message(): #definimos una funcion de la ruta 
    return HTMLResponse('<h1>Hello World</h1>') #retorna un objeto de la clase HTMLResponse

@app.get('/movies', tags=["Movies"]) #definimos una ruta de la clase FastAPI
def get_movies(): #aqui puse get_movies y estaba solo movies
    return movies_list

@app.get('/movies/{id}' , tags=["Movies"])
def get_movie(id: int):
    for item in movies_list:
        if item["id"] == id:
            return item
    return []

@app.get('/movies/', tags=["Movies"])
def get_movies_by_category(category: str, year: int):
    return [ item for item in movies_list if item ['category'] == category]

@app.post('/movies', tags=['Movies'])
def create_movie(id: int =Body(), title: str =Body(), overview: str =Body(), year: int =Body(), rating: float =Body(), category: str =Body()):
    movies_list.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies_list

@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, title: str =Body(), overview: str =Body(), year: int =Body(), rating: float =Body(), category: str =Body()):
    for item in movies_list:
        if item["id"] == id:
            item['title'] = title,
            item['overview'] = overview,
            item['year'] = year,
            item['rating'] = rating,
            item['category'] = category,
            return movies_list

@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int):
        for item in movies_list:
            if item["id"] == id:
                movies_list.remove(item)
                return movies_list