# Proyecto Individual Nº1
## Acerca de mí
Mi nombre es Robertino Garcia, alumno de la cohorte Nº17 del Bootcamp de Henry. Me apasiona el análisis de datos y el aprendizaje automático, y este proyecto es una muestra de las habilidades y conocimientos que he adquirido durante mi formación.

## Descripción
Este proyecto se centra en la extracción, transformación y carga (ETL) de una base de datos específica, seguido de un análisis exploratorio de datos (EDA). Además, se implementan varias funciones relacionadas con la base de datos y se desarrolla una función de recomendación utilizando técnicas de aprendizaje automático. 

Una parte crucial de este proyecto es el despliegue exitoso de estas funciones en Render. Esto permite probar las funciones en un entorno de producción y garantizar que funcionen correctamente cuando se accede a ellas a través de la API. La verificación de las funciones se realiza en FastAPI para asegurar su correcto funcionamiento.

## Contenido
### Base de Datos

La base de datos consta de 3 archivos .json que inicialmente tuvieron que ser desanidados para poder ser leídos en Python. Posteriormente, se realizó un proceso de limpieza de ETL y se extrajeron conclusiones de la misma en el EDA
1. **ETL de las bases de datos**: Se realiza un proceso de ETL para extraer datos de la fuente original, transformarlos según las necesidades del proyecto y cargarlos en una base de datos adecuada para su posterior análisis.

2. **Análisis exploratorio de datos (EDA)**: Se realiza un EDA en la base de datos para entender las características y distribuciones de los datos, identificar posibles problemas y descubrir patrones y relaciones.

### Funciones
**Funciones de la base de datos**: Se implementan varias funciones para interactuar con la base de datos, permitiendo consultas y manipulaciones eficientes de los datos.
Las funciones implementadas en este proyecto son las siguientes:

1. `PlayTimeGenre(genero: str)`: Devuelve el año con más horas jugadas para el género dado.

2. `UserForGenre(genero: str)`: Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

3. `UsersRecommend(año: int)`: Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado.

4. `UsersWorstDeveloper(año: int)`: Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado.

5. `sentiment_analysis(empresa desarrolladora: str)`: Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.

### Modelo de Aprendizaje Automático
Este proyecto también incluye la implementación de un modelo de aprendizaje automático para un sistema de recomendación. Se ofrecen dos propuestas de trabajo para este sistema de recomendación:

 **Relación ítem-ítem**: En este enfoque, el modelo toma un ítem (en este caso, un juego) y, en base a qué tan similar es ese ítem al resto, recomienda ítems similares. Para ello, se aplica la similitud del coseno. El input es un juego y el output es una lista de juegos recomendados. La función correspondiente en la API sería:

 1. `def recomendacion_juego( id de producto )`: Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

## Modo en que desempeñe mis habilidades como Data Science y Data Engineer
Para este proyecto realice una serie de pasos sitemicos comenzando con inicialmente con un pronceso de ETL (extracción, transformación y carga) para cada base de datos proporcionada, seguido con la realizacion del EDA (análisis de datos exploratorio) de cada base de datos ya limpios previamente. Luego una vez teniendo los datos en forma correcta , comence a extraer de las bases de datos la informacion requerida por funcion para poder cumplir con el requerimiento de las mismas. Por ultimo al momento de realizar el modelo de recomendacion procedi inicialmente a extraer los datos necesarios para el mismo , luego realice los siguientes pasos para cumplir con la funcion pedida:

1. `Preparación de los datos`: Converti los nombres de los desarrolladores de juegos en listas de números. Cada juego se representa como una lista, donde cada número representa una palabra en el nombre del desarrollador.

2. `Cálculo de similitud`: Calcule cuán similares son los juegos entre sí basándome en sus listas de números. Cuanto más similares sean las listas, más similares serán los juegos.

3. `Generación de recomendaciones`: Para un juego dado, busca los juegos más similares y los sugiere como recomendaciones.

4. `Despliegue del modelo`: Una vez entrenado, el modelo de recomendación se pone en línea para que pueda ser utilizado a través de una API.

### Link para ingresar a la pagina de FastApi
https://pi-ml-steam-acyb.onrender.com

### Link del video explicativo sobre el funcionamiento de la Api 
https://www.youtube.com/watch?v=3T_RugUpJDo

### Stack Tecnologico Utilizado:
Pandas, Scikit-learn, Matplotlib, Seaborn, NumPy, Render, FastAPI, GitHub, Git, Markdown, Python, Visual Studio Code
