import mysql.connector as db
import mysql

mydb = db.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql123",
    database = "Cine"
)

def consultarDB1():
    
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

    
def consultarDB2():

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


def consultarDB3():

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


def solicitar_accion():
    print("Ingrese una opcion:\n") 
    print("=> [1] Lista de los directores que tienen más de 3 películas")
    print("\n=> [2] Ranking de actores y cantidad de películas")
    print("\n=> [3] Ranking de películas con puntaje mayor a 8")
    print("\n=> [0] Salir")
    
    seleccion = input("\nIndique su elección (0, 1, 2, 3): ")
    while seleccion not in "0123":
        seleccion = input("\n==> Elección no válida <==\nIndique su elección (0, 1, 2, 3): ")
    seleccion = int(seleccion)
    return seleccion

def main():
    
    try:
        salir = False
        print("\n********** ¡Bienvenid@! **********")
        while not salir:
            accion = solicitar_accion()
            if accion == 1:
                consultarDB1()  
            elif accion == 2:
                consultarDB2()
            elif accion == 3:
                consultarDB3()
            elif accion == 0:
                salir = True
                print("\n********** ¡Adiós! **********\n")
            else:
                print("\n==> Elección no válida <==")

    except mysql.connector.IntegrityError as error:
            print("\n=> ID ya existe en DB, favor revisar datos a ingresar!\n")
    
        

if __name__ == "__main__":
    main()