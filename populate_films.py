import requests
import json
import sqlite3

############# The db file ##############
db_file = 'filmography.sqlite'
conn = sqlite3.connect(db_file)
cur = conn.cursor()

#cur.execute('CREATE TABLE IF NOT EXISTS Actors (actor_id INTEGER PRIMARY KEY, name TEXT, gender INTEGER, films TEXT, avg_rating INTEGER, fav_genre INTEGER)')
#cur.execute('CREATE TABLE IF NOT EXISTS Films (film_id INTEGER PRIMARY KEY, name TEXT, genres TEXT, rating INTEGER, release_date TEXT)')

#cur.execute('INSERT INTO Actors (actor_id, name, gender) VALUES (?,?,?)', (31, 'Tom Hanks', 2))
#cur.execute('INSERT INTO Actors (actor_id, name, gender) VALUES (?,?,?)', (9780, 'Angela Bassett', 1))
#cur.execute('INSERT INTO Actors (actor_id, name, gender) VALUES (?,?,?)', (18918, 'The Rock', 2))
#conn.commit()
#########################################
key = 'eff108aecbb73d143e06dc125caf045f'
base = 'https://api.themoviedb.org/3/discover/movie?api_key=eff108aecbb73d143e06dc125caf045f&language=en-US&sort_by=vote_average.desc&include_adult=false&include_video=false&page=1&with_cast='
#########################################

def pull_films(info):
    '''
    Takes in a python object created from the JSON response containing an actor's filmography
    and adds the top 10 of those films to the database. Returns a list of the film's ids to be
    added to the films attribute of the actor's tuple in the database.
    '''
    filmography = []
    for film in range(10):
        pos = info["results"][film]
        identity = pos["id"]
        name = pos["original_title"]
        
        int_genres = pos["genre_ids"]
        genres = []
        for genre in int_genres:
            genres.append(str(genre))

        votes = pos["vote_average"]
        date = pos["release_date"]
        cur.execute('INSERT or IGNORE INTO Films (film_id, name, genres, rating, release_date) VALUES (?, ?, ?, ?, ?)', (identity, name, ",".join(genres), votes, date))
        filmography.append(str(identity))
    conn.commit()
    return filmography


def call_actors():
    '''
    Selects all of the actors from the database and adds a list of 10 of their best rated films 
    to their films attribute.
    '''
    cur.execute('SELECT actor_id, name FROM Actors')
    disk = []
    for actor in cur:
        disk.append(actor)

    for actor in disk:
        actor_id = actor[0]
        full_req = base + str(actor_id)
        response = requests.get(full_req)
        cata = json.loads(response.content)
        cur.execute('UPDATE Actors SET films= ? WHERE actor_id= ?', (",".join(pull_films(cata)), actor_id))
        conn.commit()
        

def main():
    call_actors()

if __name__ == "__main__":
    main()