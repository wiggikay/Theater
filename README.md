# Theater
Repository for SI 206 project.

Task list:

 ---- PART 1 ----

1. Parse various lists on IMDB's website with Beautiful Soup in order to create a list of relevant actors and actresses. This list will be used to make queries to themoviedb API. Output the results to a JSON formatted text file like so:

       {
           "actors": [
               actor1,
               actor2,
               actor3,
               ...
           ]
       }

2. Use the list of actors and actresses from step 1 to query themoviedb API using the Search People method. Add the actors to a table in the sqlite database. Each tuple should have the following attributes: actor_id, name, gender, films, avg_rating, fav_genre. actor_id is the primary key, gender is the gender code provided by themoviedb, films is a list of film ids associated with the actor, avg_rating is the average rating of their films which will be calculated later, and fav_genre is the genre of film that the actor works in most often which will also be calculated later. Leave avg_imdb and fav_genre blank for now.

---- PART 2 ----

3. Populate the films attribute of each actor and the films relation table. Use the discover method to find the top 10 films that each actor has been in based on popularity. Sorting can be done through an API request. For example: 
    /discover/movie?with_cast=500&sort_by=vote_average.desc

4. Add the film ids to the actor's film attribute in a comma seperated list as a string. Add the films themselves to a new relation in the database. The film relation should have the following attributes: film_id, name, genres, rating, release_date. film_id is the primary key, genres is a list of the genre_ids provided by themoviedb. 

5. Transfer the gender and genre ids from themoviedatabase to our local sqlite db.

--- PART 3 --- 

6. Calculate some stuff. This is post data collection so I'll worry about it later.



    
