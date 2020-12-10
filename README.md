# Theater
Repository for SI 206 project.

Report

--- Goals & Achieved Goals ---

Originally our project was going to be about calculating the country with the best cusine for certain dietary needs but the website that we were going to use to scrape data from used iframe in way that kept us from scraping it. Our new goal is to calculate the average ratings of the top 10 best films for each actor in IMDB's best male Actors of the 2010's and determine whether the top best 50 best actors were really in better films than the bottom 50 or if the ranks were somehat determined on other factors like real-life personability or politics. We also wanted to find out the genre distribution of the best films of the top 100 Actors to determine what type of film was most popular. We planned on scraping IMDB for the list of the best actors of the 2010's (https://www.imdb.com/list/ls045044639/) and their rank and then using The Movie Database API to find their top 10 highest rated films. We wanted to make a histogram and a scatter plot to show the distribution of of ratings and pie chart to show the distribution of genres. Despite the rough start with our original plan we were able to meet all the goals of our current plan.

--- Problems we faced --- 

As I mentioned before we were unable to go through with our original plan because of issues with using Beautiful Soup on an iframe site. We also had a bit of trouble with modeling the database in best way because we weren't always sure which attributes we would need to make the calculations effieciently and answer our questions. Sometimes we needed to go into the database and add attributes to a table or remake the table to remove certain attributes. Through trial and error we figured out exactly which attributes we needed in which tables.

--- calculations from the data in the database ---

The name of the file containing the calculations from the data in the database is: calculation_results.txt

--- The visualizations ---

The scatter plot is the img file scatterplot
The histogram is the img file histogram
The pie chart is the img file piechart

--- Instructions for running the code ---

Step 1:







Step 2:

Step two is use the Popular_Actors.db Actors table to create a new table called Films that list the top 10 highest rated films from all of the actors and put the ids of those films in the actor_name attribute of the actor. Run populate_films.py to create and populate the Films table with the top 10 films for 25 of the actors listed in Actors table who's films haven't already been recorded.

Part 3:

--Visualization 1 (Scatterplot)


 -- Visualization 2 (Histogram)
Run calculate.py to populate the film_avg attribute of the Actor's table, create a histogram of the average film ratings for the top and bottom half of the top 100 list, and output a JSON formatted txt file called calculation_results.txt with the calculation results. The histogram shows that both sides of the rank have similar distribution but the top 10 are more distributed in the < 8.5 range. Overall, the top 50 actors do have, on average, films that are ranked higher, so there is a strong correlation between the two.

 -- Visualization 3 (Pie chart)

