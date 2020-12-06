import requests
from bs4 import BeautifulSoup
import requests
import json
import os
import sqlite3

API_KEY = "58a16777781e3378851826f5f021d7d7"

def get_actors(count_start):
    url = "https://www.imdb.com/list/ls022928819/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    actors_list = []
    actors = soup.find_all("h3", class_="lister-item-header")
    count_end = count_start + 25
    for i in range(count_start, count_end):
        name = actors[i].find("a")
        actor_name = name.text.strip()
        actors_list.append(actor_name)
    return actors_list

def get_total_actors_list():
    count = 0
    actors_name_list = []
    for i in range(4):
        list1 = get_actors(count)
        for list_item in list1:
            if ' ' in list_item:
                name = list_item.replace(' ', '%20')
            else:
                name = list_item
            actors_name_list.append(name)
        count+=25
    return actors_name_list

def get_actors_data(actor_name):
    base_url = "https://api.themoviedb.org/3/search/person?api_key="
    url = base_url + API_KEY + "&query=" + actor_name
    r = requests.get(url)
    dict = json.loads(r.text)
    actor_data = dict["results"][0]
    actor_id = actor_data["id"]
    actor_name = actor_data["name"]
    actor_gender = actor_data["gender"]
    actor_films = actor_data["known_for"]
    actor_films_id = []
    for i in range(len(actor_films)):
        actor_films_id.append(actor_films[i]["id"])
    actor_films_id1 = ""
    actor_avg_rating = ""
    actor_fav_genre = ""
    actor_details = [actor_id, actor_name, actor_gender, actor_films_id1, actor_avg_rating, actor_fav_genre]
    return actor_details

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def create_actors_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Actors (actor_id INTEGER PRIMARY KEY, actor_name STRING, actor_gender INTEGER,"
                " actor_films STRING, actor_avg_rating STRING, actor_fav_genre STRING)")
    conn.commit()

def add_data(cur, conn, count):
    list1 = get_total_actors_list()
    actor_details = get_actors_data(list1[count])
    cur.execute("INSERT INTO Actors (actor_id , actor_name, actor_gender, actor_films, actor_avg_rating, actor_fav_genre)"
                " VALUES (?, ?, ?, ?, ?, ?)", (actor_details[0], actor_details[1], actor_details[2], actor_details[3], actor_details[4], actor_details[5]))
    conn.commit()

def build_database(cur, conn):
    create_actors_table(cur, conn)
    count = 0
    for i in range(4):
        for j in range(25):
            add_data(cur, conn, count)
            count+=1


def main():
    list1 = get_total_actors_list()
    print(list1)
    get_actors_data("Will%20Smith")
    cur, conn = setUpDatabase("popular_actors1.db")
    build_database(cur, conn)

if __name__ == "__main__":
    main()