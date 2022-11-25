# Michael Streed
# 11-24-2022
# module 7.2
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "**********",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))
    input("\n\n Press any key to continue...\n")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
else:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM studio")  # selects everything from studio table
    studios = cursor.fetchall()
    print("---printing studio records---")
    for studio in studios:
        print("studio_id : {}\nstudio_name : {}\n".format(studio[0], studio[1], ))

    cursor.execute("SELECT * FROM genre")  # selects everything from genre table
    genres = cursor.fetchall()
    print("---printing genre records---")
    for genre in genres:
        print("genre_id : {}\ngenre_name : {}\n".format(genre[0], genre[1], ))

    cursor.execute("SELECT * from film WHERE film_runtime < 120; ") # selects short films
    short_films = cursor.fetchall()
    print("---printing short films---")
    for film in short_films:
        print("film_name : {}\nruntime : {}\n".format(film[1], film[3]))

    # this will get list of film names ordered by director
    cursor.execute("SELECT film_name, film_director from film order by film_director;")
    directors = cursor.fetchall()
    print("---printing director records in order---")
    for director in directors:
        print("film_name : {}\nfilm_director : {}\n".format(director[0], director[1]))
        # ^^I don't understand why director[2] is out of range ^^
finally:
    db.close()