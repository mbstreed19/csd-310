# Michael Streed
# 11-26-2022
# module 8.2
import mysql.connector
from mysql.connector import errorcode

# making needed variables
config = {
    "user" : "movies_user",
    "password" : "popcorn",
    "host" : "127.0.0.1",
    "database" : "movies",
    "raise_on_warnings" : True
}
db = mysql.connector.connect(**config)
cursor = db.cursor()
title = "DISPLAYING FILMS"

def show_films(cursor, title):
    cursor.execute("""select film_name as Name, film_director as Director, genre_name as genre,
        studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id
        INNER JOIN studio ON film.studio_id=studio.studio_id;""")
    print(cursor)
    films = cursor.fetchall()
    print("\n -- {} --".format(title))
    for film in films:
       # print(film) # this is for testing
        print("Film name : {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2],film[3]))


# First run of the function
show_films(cursor,title)

# Second run of function
cursor.execute("insert into film values (4, 'Star Wars', 1977, 105, 'George Lucas', 1, 3);")
title = "DISPLAYING FILMS AFTER INSERT"
show_films(cursor,title)

# Third run of the function
cursor.execute("update film set genre_id = 1 where film_name = 'Alien';")
title = "DISPLAYING FILMS AFTER UPDATE- Changed Alien to horror"
show_films(cursor,title)

# Last run of the function
cursor.execute("delete from film where film_name = 'Gladiator';")
title = "DISPLAYING FILMS AFTER DELETE"
show_films(cursor,title)