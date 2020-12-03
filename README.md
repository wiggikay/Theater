# Utensil
Repository for SI 206 project.

Task list:

 ---- PART 1 ----
 1. Create a list of nations to pull dishes from (make sure each nation has a list of at list 50 top dishes on tasteatlas)
    and create a database in this directory to store a table of nation names and id numbers. The id numbers will
    be used later in the table containing dish information.
 2. Parse each Top 50 (or Top 100 up to 50) list for dish names and descriptions.
        - First create a list of urls, one for each Top 50 page.
        - Use Beautiful Soup to parse each page in the url list and extract the dish name,
        and description (optional: also grab the associated image url). Put each
        dish into a dictionary object. Put each dictionary object into a list as the value of a key
        named after the nation of each dish. This is an example:
        
        {
            "Jamaica": [
                {
                    "dish" : "Jamaican Spiced Bun",
                    "description" : "Spiced bun is a tender Jamaican sweet bread studded with fruits such as cranberries and raisins. It is characterized by its dark brown color. The spices used in this sweet bread are typically nutmeg, vanilla, cinnamon, and rose water. Although Jamaican spiced bun is consumed year-round, it is a staple during the Easter season, when it is traditionally paired with hard cheese.",
                    "image" : "https://cdn.tasteatlas.com/images/dishes/69168393d141411ea353bd6ed69f9ccb.jpg?w=905&h=510"
                }
            ]
        }
    
3. Dump all the JSON formatted nation data into a .txt file in this same directory

    ---- PART 2 ----
4. Use the Spoonacular API to create a list of ingredients for each dish from their descriptions.
    This can be done using Spoonacular's (GET) 'Analyze a Recipe Search Query' method or the (POST)'Detect food in Text' method.
5. Update the .txt file to include the ingredients for each dish in a list like so:

        {
            "Jamaica": [
                {
                    "dish" : "Jamaican Spiced Bun",
                    "description" : "Spiced bun is a tender Jamaican sweet bread studded with fruits such as cranberries and raisins. It is characterized by its dark brown color. The spices used in this sweet bread are typically nutmeg, vanilla, cinnamon, and rose water. Although Jamaican spiced bun is consumed year-round, it is a staple during the Easter season, when it is traditionally paired with hard cheese.",
                    "image" : "https://cdn.tasteatlas.com/images/dishes/69168393d141411ea353bd6ed69f9ccb.jpg?w=905&h=510"
                    "ingredients": [
                        'nutmeg', 
                        'vanilla', 
                        'cinnamon',
                        'rose water',
                        'cranberries',
                        'rasins'
                    ]
                }
            ]
        }

     This step is important because considering how dishes are described on the website and how the API decides 
    to parse ingredients it may be a good idea to look over the API response and compare them to the dish descriptions
    to make sure they're similar before things get added to the database. For example, the Jamaican Spiced Bun description
    says that it's often paired with hard cheese. It doesn't contain cheese, but the API might assume that it is an ingredient when
    use the description in a GET/POST request. This isn't super common but it is an edge case to consider because it would affect our
    results. IMPORTANT: The best way to avoid the issue of incorrect ingredients is to only consider text from the first paragraph 
    of the description because typically alternate ingredients and food pairings appear in later paragraphs.
    6. Put all of the dishes into the SQLite database stored in this directory (in a seperate table). The attribute names would be nation id, dish, description, 
    image, ingredients, and diet. Ingredients will be a string of comma seperated ingredients and diet will also be string.

    ---- Part 3 ----

6. Fill out the diet attribute for each dish. We'll most likely need to use Edamam's API for this. The Edamam API can do this in two steps. 
    - Step one is using the Nutrition Analysis API to get the diet labels and health labels of each food item mentioned in the ingredient list made in PART 2. We should make sure that we're aware of any ingredient queries that get rejected by Edamam's API (because we may be able to fix that and missing certain ingredients could make our data crappy). Use caching so you don't have to make the same requests over and over again. The resulting health and diet labels should go into a JSON formatted txt file as follows:
    
            {
            "red apple": {
                "healthLabels": [
                    "FAT_FREE",
                    "LOW_FAT_ABS",
                    "LOW_POTASSIUM",
                    "KIDNEY_FRIENDLY",
                    "VEGAN",
                    "VEGETARIAN",
                    "PESCATARIAN",
                    "PALEO",
                    "SPECIFIC_CARBS",
                    "DAIRY_FREE",
                    "GLUTEN_FREE",
                    "WHEAT_FREE",
                    "EGG_FREE",
                    "MILK_FREE",
                    "PEANUT_FREE",
                    "TREE_NUT_FREE",
                    "SOY_FREE",
                    "FISH_FREE",
                    "SHELLFISH_FREE",
                    "PORK_FREE",
                    "RED_MEAT_FREE",
                    "ALCOHOL_FREE",
                    "NO_OIL_ADDED",
                    "NO_SUGAR_ADDED",
                    "KOSHER"
                ],
                "dietLabels": [
                    "LOW_FAT",
                    "LOW_SODIUM"
                ]
            }
          }
    - Step two is cross referencing the diet and health labels of each ingredient in each list in order to add the appropriate health and diet labels to their SQLite entry. For example, if a dish has three ingredients, we'll give it the VEGAN label if each of it's ingredients has the VEGAN label.
    
    It's best if each of us does one step in part 3 because it's a lot of work. The documentation for this is here. https://developer.edamam.com/food-database-api-docs

    ---- Part 4 ----
7. Calculate things from the data. Honestly after part 3 this should be a cake walk.
    
