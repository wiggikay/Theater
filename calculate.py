import json
import sqlite3
import math


############# The db file ##############
db_file = 'Popular_Actors.db'
conn = sqlite3.connect(db_file)
cur = conn.cursor()
#######################################

#cur.execute('ALTER TABLE Actors ADD film_avg INTEGER')
#conn.commit()

def get_all_actors():
    cur.execute('SELECT actor_name FROM Actors')
    disk = []
    for actor in cur:
        disk.append(actor[0])
    return disk

def avg_actor_films(films, name):
    rating_list = []
    for film in films:
        cur.execute('SELECT rating FROM Films WHERE film_id=?', (int(film),))
        rating_list.append(int(cur.fetchone()[0]))
    ########
    total = 0
    for rating in rating_list:
        total += rating
    avg = total/len(rating_list)
    cur.execute('UPDATE Actors SET film_avg=? WHERE actor_name=?',(avg, name))
    conn.commit()

#Read the Actors table. Get the average rating for each film. Use join to determine 
# if they should be in the top or bottom half. Calculate the average for each group
def average_films():
    disk = get_all_actors()
    for actor in disk:
        cur.execute('SELECT actor_films, actor_name FROM Actors WHERE actor_name=?', (actor,))
        code_list = cur.fetchone()[0].split(',')
        avg_actor_films(code_list, actor)

###############################################################################

def select_actors():
    cur.execute('SELECT actor_name FROM Actors_Popularity ORDER BY popularity_rank ASC')
    disk = []
    for actor in cur:
        disk.append(actor[0])
    return disk

def split_pop():
    cur.execute('SELECT COUNT (DISTINCT actor_name) FROM Actors_Popularity')
    total = cur.fetchone()[0]
    top_num = math.floor(total/2)
    return top_num

def group_avg(group):
    overall_total = 0
    for actor in group:
        cur.execute('SELECT actor_id FROM Actors WHERE actor_name=?',(actor,))
        identify = cur.fetchone()[0]
        cur.execute('SELECT film_avg FROM Actors_Popularity INNER JOIN Actors on Actors.actor_name = Actors_Popularity.actor_name WHERE actor_id=?', (identify,))
        overall_total += cur.fetchone()[0]
        overall_total = round(overall_total, 4)
    overall_avg = overall_total/len(group)
    return overall_avg


def rank_avg():
    top_num = split_pop()
    disk = select_actors()
    top_group = disk[:top_num]
    bottom_group = disk[top_num:]
    top_avg = group_avg(top_group)
    bottom_avg = group_avg(bottom_group)
    print(bottom_avg)
    return (top_avg, bottom_avg)



          

def main():
    #average_films()
    rank_avg()
    
    


if __name__ == "__main__":
    main()



