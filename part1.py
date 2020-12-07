import requests
from bs4 import BeautifulSoup
import requests
import json
import os
import sqlite3

API_KEY = "58a16777781e3378851826f5f021d7d7"

def get_actors():
    url = "https://www.imdb.com/list/ls022928819/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    actors_name_list = []
    actors = soup.find_all("h3", class_="lister-item-header")
    for i in range(100):
        name = actors[i].find("a")
        actor_name = name.text.strip()
        actors_name_list.append(actor_name)
    actors_popularity = []
    populars = soup.find_all("span", class_="lister-item-index")
    for popular in populars:
        actors_popularity.append(popular.text)
    imdb_actors = []
    for i in range(len(actors_name_list)):
        imdb_actors.append([actors_popularity[i], actors_name_list[i]])
    return imdb_actors


def setUp_imdb_Database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


def create_imdb_actors_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Actors_Popularity (popularity_rank INTEGER PRIMARY KEY, actor_name STRING)")
    conn.commit()


def add_imdb_actors_data(cur, conn, count):
    list1 = get_actors()
    cur.execute("INSERT INTO Actors_Popularity (popularity_rank, actor_name) VALUES (?, ?)", (list1[count][0], list1[count][1]))
    conn.commit()


def build_imdb_table(cur, conn):
    create_imdb_actors_table(cur, conn)
    cur.execute("SELECT COUNT(*) FROM Actors_Popularity")
    data_present = cur.fetchone()
    count = data_present[0]
    if count < 100:
        for i in range(25):
            add_imdb_actors_data(cur, conn, count)
            count+=1


def get_total_actors_list():
    list1 = get_actors()
    actors_name_list = []
    for list_item in list1:
        if ' ' in list_item[1]:
            name = list_item[1].replace(' ', '%20')
        else:
            name = list_item[1]
        actors_name_list.append(name)
    return actors_name_list


def get_actors_data(actor_name):
    base_url = "https://api.themoviedb.org/3/search/person?api_key="
    url = base_url + API_KEY + "&query=" + actor_name
    r = requests.get(url)
    dict = json.loads(r.text)
    actor_data = dict["results"][0]
    actor_id = actor_data["id"]
    actor_name = actor_data["name"]
    actor_films = ""
    actor_details = [actor_id, actor_name, actor_films]
    return actor_details


def create_actors_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Actors (actor_id INTEGER PRIMARY KEY, actor_name STRING, actor_films STRING)")
    conn.commit()


def add_actor_data(cur, conn, count):
    list1 = get_total_actors_list()
    actor_details = get_actors_data(list1[count])
    cur.execute("INSERT INTO Actors (actor_id , actor_name, actor_films) VALUES (?, ?, ?)", (actor_details[0], actor_details[1], actor_details[2]))
    conn.commit()


def build_actors_table(cur, conn):
    create_actors_table(cur, conn)
    cur.execute("SELECT COUNT(*) FROM Actors")
    data_present = cur.fetchone()
    count = data_present[0]
    if count < 100:
        for i in range(25):
            add_actor_data(cur, conn, count)
            count+= 1


def main():
    cur, conn = setUp_imdb_Database("Popular_Actors.db")
    build_imdb_table(cur, conn)
    build_actors_table(cur, conn)

if __name__ == "__main__":
    main()