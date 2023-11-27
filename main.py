from pydantic import BaseModel
import pandas as pd 
from typing import Optional
from fastapi import FastAPI, Response, Query
from fastapi.responses import HTMLResponse

#http://127.0.0.1:8000 (ruta raiz)

app = FastAPI()
@app.get("/", response_class=HTMLResponse)  # Ruta de la página inicial
def presentacion():
    '''
    Genera una página de presentación HTML para la API del proyecto individual 1 sobre la plataforma Steam.
    
    Returns:
    str: Código HTML que muestra la página de presentación.
    '''
    return '''
    <html>
        <head>
            <title>API Proyecto Individual 1</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 20px;
                    background-image: url('https://cdn.businessinsider.es/sites/navi.axelspringer.es/public/media/image/2021/01/steam-juegos-2203341.jpg?tf=1200x');
                    background-size: cover;
                    color: white;
                    text-shadow: 2px 2px 4px #000000;
                }
                h1 {
                    color: #fff;
                    text-align: center;
                }
                p {
                    color: #fff;
                    text-align: center;
                    font-size: 18px;
                    margin-top: 20px;
                }
                
                a:link {
  color: #265301;
}

a:visited {
  color: #EEF580;
}

a:focus {
  border-bottom: 1px solid;
  background: #bae498;
}

a:hover {
  border-bottom: 1px solid;
  background: #80A8F9;
}

a:active {
  background: #80A8F9;
  color: #F2574D;
}
            </style>
        </head>
        <body>
            <h1>Bienvenidos a mi api para el Proyecto Individual Nº1 del Bootcam Henry (Data Science)</h1>
            <p>Mi nombre es Robertino Garcia , alumno de Henry perteneciente al Cohorte Nº 17 (Full-Time)</p>
            <p><a href="https://github.com/RobertinoS/PI_ML_OPS-Steam" target="_blank">Link del repositorio de GitHub</a></p>
            <p><a href="https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile" target="_blank">Mi perfil de Linkedin</a></p>
        </body>
    </html>
    '''



#-------------------------------------------------------------------------------------------------------   
df_play=pd.read_parquet('data/df_playtime.parquet')
df_useforgenre=pd.read_parquet('data/df_useforgenre.parquet')
df_worst_1=pd.read_parquet('data/df_worst.parquet')
df_senti=pd.read_parquet('data/df_senti.parquet')
df_recom=pd.read_parquet('data/df_recom.parquet')
df_merge_id=pd.read_parquet('data/df_recomendacion.parquet')
#---------------------------------------------------------------------------------------------------------

@app.get('/PlayTimeGenre')
def PlayTimeGenre(genero: str = Query(..., description="Ingrese el género del videojuego. Por ejemplo, un género válido podría ser 'Action'.")):
    # Filtrar por el género especificado
    df_genre = df_play[df_play['genres'] == genero]    
    # Si no hay datos para el género especificado, retorna un mensaje
    if df_genre.empty:
        raise HTTPException(status_code=404, detail=f"No hay datos para el género '{genero}'")   
    # Agrupar por año y calcular las horas jugadas sumando los valores
    grouped = df_genre.groupby('release_anio')['playtime_forever'].sum()    
    # Encontrar el año con más horas jugadas
    max_playtime_year = grouped.idxmax()
    # Retornar el resultado como un diccionario
    return {"Año de lanzamiento con más horas jugadas para Género {}".format(genero): max_playtime_year}
        
@app.get('/UserForGenre')
def UserForGenre(genero: str = Query(..., description="Ingrese el género del videojuego. Por ejemplo, un género válido podría ser 'Action'.")):  
    # Filtrar por el género especificado
    df_genre = df_useforgenre[df_useforgenre['genres'] == genero]  
    # Si no hay datos para el género especificado, retorna un mensaje
    if df_genre.empty:
        return f"No hay datos para el género '{genero}'"    
    # Agrupar por usuario y género y calcular las horas jugadas sumando los valores
    grouped = df_genre.groupby(['user_id'])['playtime_forever'].sum()    
    # Encontrar el usuario con más horas jugadas
    max_playtime_user = grouped.idxmax()        
    # Agrupar por año y calcular las horas jugadas sumando los valores
    grouped_by_year = df_genre.groupby('release_anio')['playtime_forever'].sum()    
    # Crear lista de acumulación de horas jugadas por año
    acumulacion_horas = [{'Año': year, 'Horas': hours} for year, hours in grouped_by_year.items()]    
    # Retornar el resultado como un diccionario
    return {"Usuario con más horas jugadas para Género {}".format(genero): max_playtime_user, "Horas jugadas": acumulacion_horas}

@app.get('/UsersRecommend')
def UsersRecommend( año :int = Query(..., description="Ingrese un año que este en el rango entre el 2010 y 2015")):
     # Filtra el DataFrame df_recom por el año proporcionado y lo guarda en top3_por_año
    top3_por_año = df_recom[df_recom['year'] == año]
    # Inicializa una lista vacía para almacenar los resultados
    resultado = []
    # Itera sobre las filas del DataFrame top3_por_año
    for index, row in top3_por_año.iterrows():
        # Obtiene el puesto, el título y el año de la fila actual
        puesto = row['rank']
        titulo = row['title']
        año = int(row['year'])   
        # Agrega un diccionario a la lista de resultados con la estructura {f"Puesto {puesto}": f"{titulo}"}
        resultado.append({f"Puesto {puesto}": f"{titulo}"})
    # Devuelve la lista de resultados
    return resultado
    
@app.get('/UsersWorstDeveloper')  
def UsersWorstDeveloper( año : int = Query(..., description="Ingrese un año que este en el rango entre el 2011 y 2015")):
    # Filtrar el DataFrame df_developer por el año proporcionado
    developer_por_año = df_worst_1[df_worst_1['year'] == año]
    # Obtener el top 3 de desarrolladoras con juegos MENOS recomendados y sus valores según rank
    developer_top3_worst = developer_por_año.sort_values(by='rank', ascending=True).head(3)
    # Formatear el resultado como lista de diccionarios
    result = [{"Puesto {}: {}".format(rank, developer)} for rank, developer in zip(developer_top3_worst['rank'], developer_top3_worst['developer'])]
    return result
    
@app.get('/sentiment_analysis')    
def sentiment_analysis(empresa_desarrolladora: str= Query(..., description="Ingrese una empresa desarrolladora(developer).Por ejemplo, 'Valve'.")): 
    # Filtra el DataFrame df_senti por la empresa desarrolladora proporcionada y lo guarda en developer_df
    developer_df = df_senti[df_senti['developer'] == empresa_desarrolladora]
    # Crea un diccionario result con la estructura {empresa_desarrolladora: {'Negative': 0, 'Neutral': 0, 'Positive': 0}}
    result = {empresa_desarrolladora: {'Negative': 0, 'Neutral': 0, 'Positive': 0}}
    # Itera sobre las columnas 'sentiment_analysis' y 'reviews_recommend_count' del DataFrame developer_df
    for sentiment, count in zip(developer_df['sentiment_analysis'], developer_df['reviews_recommend_count']):
        # Crea un mapeo entre los valores numéricos de la columna 'sentiment_analysis' y las categorías de sentimiento correspondientes
        sentiment_mapping = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}        
        # Usa el mapeo para obtener la categoría de sentimiento correspondiente al valor numérico
        sentiment_category = sentiment_mapping[sentiment]       
        # Suma la cantidad de reseñas (count) a la categoría de sentimiento correspondiente en el diccionario result
        result[empresa_desarrolladora][sentiment_category] += count
    # Devuelve el diccionario result
    return result
    
@app.get('/recomendacion_juego') 
def recomendacion_juego(id:int= Query(..., description="Ingrese un id de producto.Por ejemplo, '388390'.")):
    # Filtra el DataFrame df_merge_id por el id proporcionado y obtiene el 'model' correspondiente
    model = df_merge_id[df_merge_id['id'] == id]['model'].iloc[0]
    # Inicializa un diccionario vacío para almacenar las recomendaciones
    recomendaciones_dict = {}
    # Si el model tiene elementos, procede a llenar el diccionario de recomendaciones
    if len(model) > 0:
        for i in range(len(model)):
            # Agrega cada elemento del model al diccionario de recomendaciones
            recomendaciones_dict[i + 1] = model[i]
        # Devuelve el diccionario de recomendaciones
        return recomendaciones_dict
    else:
        # Si el model no tiene elementos, devuelve un mensaje de error
        return f"No se encontró un model para el id {id}"
