import mysql.connector as db
import mysql
import csv
import time

mydb = db.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql123",
    database = "Cine"
)

def insertar_registro_Actors():
    with open ('data/actors.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        filas = []
        first = next(readCSV) 
        for row in readCSV:
            #print('fila a agregar:')
            #print(row)
            filas.append(tuple([int(row[0]), row[1], row[2]]))

    cursor = mydb.cursor()
    SQLCrear_Registro = 'INSERT INTO actors (id, first_name, last_name) VALUES (%s, %s, %s)'

    cursor.executemany(SQLCrear_Registro, filas)
    mydb.commit()
    #print("\n=> Registro ingresado correctamente en la tabla actors.\n")



def insertar_registro_Directors():
    with open ('data/directors.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        filas = []
        first = next(readCSV) 
        for row in readCSV:
            #print('fila a agregar:')
            #print(row)
            filas.append(tuple([int(row[0]), row[1], row[2]]))

    cursor = mydb.cursor()
    SQLCrear_Registro = 'INSERT INTO directors (id, first_name, last_name) VALUES (%s, %s, %s)'

    cursor.executemany(SQLCrear_Registro, filas)
    mydb.commit()
    #print("\n=> Registro ingresado correctamente en la tabla directors.\n")



def insertar_registro_Movies():
    with open ('data/movies.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        filas = []
        first = next(readCSV) 
        for row in readCSV:
            #print('fila a agregar:')
            #print(row)
            if row[3] == 'NULL':
                row[3] = '0.0'
                #print (row)
                filas.append(tuple([int(row[0]), row[1], int(row[2]), float(row[3])]))
            else:
                filas.append(tuple([int(row[0]), row[1], int(row[2]), float(row[3])]))
        cursor = mydb.cursor()
        SQLCrear_Registro = 'INSERT INTO movies (id, name, year, ranking) VALUES (%s, %s, %s, %s)'
        cursor.executemany(SQLCrear_Registro, filas)
        mydb.commit()

    #print("\n=> Registro ingresado correctamente en la tabla movies.\n")


def insertar_registro_movies_actors():
    with open ('data/movies_actors.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        filas = []
        first = next(readCSV) 
        for row in readCSV:
            #print('fila a agregar:')
            #print(row)
            filas.append(tuple([int(row[0]), int(row[1]), row[2]]))

    cursor = mydb.cursor()
    SQLCrear_Registro = 'INSERT INTO movies_actors (actor_id, movie_id, role) VALUES (%s, %s, %s)'

    cursor.executemany(SQLCrear_Registro, filas)
    mydb.commit()
    #print("\n=> Registro ingresado correctamente en la tabla movies_actors.\n")


def insertar_registro_movies_directors():
    with open ('data/movies_directors.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        filas = []
        first = next(readCSV) 
        for row in readCSV:
            #print('fila a agregar:')
            #print(row)
            filas.append(tuple([int(row[0]), int(row[1])]))

    cursor = mydb.cursor()
    SQLCrear_Registro = 'INSERT INTO movies_directors (director_id, movie_id) VALUES (%s, %s)'

    cursor.executemany(SQLCrear_Registro, filas)
    mydb.commit()
    #print("\n=> Registro ingresado correctamente en la tabla movies_actors.\n")


def main():
    
    try:
        print("\n==> Enviando los datos... Un momento por favor...<==\n")
        insertar_registro_Actors()
        insertar_registro_Directors()
        insertar_registro_Movies()
        insertar_registro_movies_actors()
        insertar_registro_movies_directors()
        time.sleep(5)
        print("=> Registro ingresado correctamente en la base de datos.\n")

    except mysql.connector.IntegrityError as error:
            print("\n=> ID ya existe en DB, favor revisar datos a ingresar!\n")
    
        

if __name__ == "__main__":
    main()