import mysql.connector as db
import pandas as pd

mydb = db.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql123",
    database = "Cine"
)

def consultarDB_con_Pandas():

    cursor = mydb.cursor()
    SQL_Consulta = "SELECT m.name as 'Movie', m.year AS 'Year', d.last_name AS 'Director',m.ranking as 'Ranking' FROM (movies_directors AS md JOIN movies as m on m.id = md.movie_id)JOIN directors AS d ON d.id = director_id WHERE m.ranking > 8 ORDER BY m.ranking DESC;"

    cursor.execute(SQL_Consulta)
    rows = cursor.fetchall()
    listupla = []
    for row in rows:
        #print(row)
        listupla.append(row)
    #print(listupla)

    df1 = pd.DataFrame(listupla, columns=["Pelicula","Agno","Director","Puntaje"])

    df_loc = df1.loc[0:9, ["Pelicula","Puntaje"]]

    df_iloc = df1.iloc[20:51, 0:4]


    print("\n-------------------- Data Frame Origen desde la Base de datos --------------------------------------\n")
    print(df1)
    print("\n\n-------------------- Primeras 10 filas y las columnas Película y Puntaje (Loc) ---------------------\n")
    print(df_loc)
    print("\n\n-------------------- Tomar las filas 20 a la 50 y todas las columnas (iLoc) ------------------------\n")
    print(df_iloc)
    print("\n")

consultarDB_con_Pandas()