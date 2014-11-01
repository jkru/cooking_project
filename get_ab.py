import requests
import time

def list_of_recipes():
    recipes = []
    open_file = open("recipe_html.lst", 'r')

    for recipe in open_file:
        recipes.append(recipe)
    return recipes


def make_recipe_names(recipes):
    recipe_names = []
    for recipe in recipes:
        recipe = recipe.replace("alton-brown/", " ").replace(".html", " ").split()
        recipe_names.append(recipe[1])
    return recipe_names

def get_recipe_page(recipe_names,recipes):
#    for i, recipe_name in enumerate(recipe_names):
    for i in range(8,108):
        open_file =  open("ab/"+recipe_names[i], 'w')
        current_recipe =  recipes[i].decode("latin-1")

        r = requests.get(current_recipe)
        open_file.write(r.text)
        open_file.close()
        time.sleep(30)

def main():

    recipes = list_of_recipes()
    recipe_names = make_recipe_names(recipes)
    get_recipe_page(recipe_names, recipes)

if __name__=="__main__":
    main()

