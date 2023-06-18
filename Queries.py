import mysql.connector as db
import mysql
import time

mydb = db.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql123",
    database = "Cine"
)

def consultarDB():
    
    print("\n==> Lista de los directores que tienen más de 3 películas\n")
    print("  ----------------------------------------------------------------------")
    cursor = mydb.cursor()
    SQL_Consulta = "SELECT d.last_name, d.first_name, COUNT(movie_id) AS 'How Many' FROM movies_directors AS md JOIN directors AS d ON d.id = md.director_id GROUP by d.last_name, d.first_name HAVING COUNT(movie_id) >3 ORDER BY COUNT(movie_id) DESC;"

    cursor.execute(SQL_Consulta)
    rows = cursor.fetchall()
    print("  | {:<25} | {:<25} | {:<10} | ".format('d.last_name','d.first_name','Cantidad'))
    print("  ----------------------------------------------------------------------")
    for row in rows:
        print("  | {:<25} | {:<25} | {:<10} | ".format( row[0], row[1], row[2]))
    print("  ----------------------------------------------------------------------\n")

    
    
    print("\n==> Ranking de actores y cantidad de películas\n")
    print("  ----------------------------------------------------------------------")
    cursor = mydb.cursor()
    SQL_Consulta = "SELECT a.last_name, a.first_name, COUNT(movie_id) FROM actors AS a JOIN movies_actors as ma on ma.actor_id = a.id GROUP BY a.last_name, a.first_name ORDER BY a.last_name, a.first_name;"

    cursor.execute(SQL_Consulta)
    rows = cursor.fetchall()
    print("  | {:<25} | {:<25} | {:<10} | ".format('a.last_name','a.first_name','Cantidad'))
    print("  ----------------------------------------------------------------------")
    for row in rows:
        print("  | {:<25} | {:<25} | {:<10} | ".format( row[0], row[1], row[2]))
    print("  ----------------------------------------------------------------------\n")




    print("\n==> Lista de películas, el año, su director y el puntaje (ranking) solo para las películas con ranking mayor a 8\n")
    print("  -------------------------------------------------------------------------------------------------")
    cursor = mydb.cursor()
    SQL_Consulta = "SELECT m.name as 'Movie', m.year AS 'Year', d.last_name AS 'Director',m.ranking as 'Ranking' FROM (movies_directors AS md JOIN movies as m on m.id = md.movie_id)JOIN directors AS d ON d.id = director_id WHERE m.ranking > 8 ORDER BY m.ranking DESC;"

    cursor.execute(SQL_Consulta)
    rows = cursor.fetchall()
    print("  | {:<50} | {:<7}  | {:<20} | {:<7} | ".format('Peliculas', 'Año', 'Director', 'Ranking'))
    print("  -------------------------------------------------------------------------------------------------")
    for row in rows:
        print("  | {:<50} | {:<7} | {:<20} | {:<7} | ".format( row[0], row[1], row[2], row[3]))
    print("  -------------------------------------------------------------------------------------------------\n")


consultarDB()