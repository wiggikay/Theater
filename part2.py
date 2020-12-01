import re
import os
import requests
import json


def load_dishes(dish_file):
    '''
    Takes in a txt file with JSON formatted data and resturns a dictionary object.
    '''
    with open(dish_file, 'r') as fp:
        dishes = json.load(fp)
    return dishes

def dump_dishes(dish_json):
    '''
    Takes in a JSON formatted dictionary object and dumps the data into a txt file.
    '''
    with open("fresh_ingredients", 'w') as fp:
        json.dump(dish_json,fp, indent=4)

def get_ingredients(desc):
    '''
    Makes a call to the Spoonacular API for the ingredients in a given dish description.
    Returns a list of the ingredients from the Spoonacular API that include an image in the
    ingredient dictionary object because those are the ones that are more accurate.
    '''
    ext = "https://api.spoonacular.com/recipes/queries/analyze?apiKey=27c95464aaa4421ca473cb092d3abc4c&q="
    request = ext + desc
    response = requests.get(request)

    ingredients = []
    pull = json.loads(response.content)
    for item in pull["ingredients"]:
        if "image" in item:
            ingredients.append(item["name"])
    return ingredients


def target_ingreds(dish_json):
    '''
    Takes in a dictionary obj of dishes from different nations (as shown in PART 1 step 2 of the README)
    and adds a list of ingredients (as shown in PART 2 step 5)
    '''
    for nation in dish_json:
        for pos in range(0, len(dish_json[nation])):
            dish_obj = dish_json[nation][pos]
            dish_obj["ingredients"] = get_ingredients(dish_obj["description"])
    dump_dishes(dish_json)


def main():
    dishes = load_dishes("carbs.txt")
    target_ingreds(dishes)


if __name__ == "__main__":
    main()