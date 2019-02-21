#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  for k in recipe.keys():
    if k not in ingredients.keys():
      return 0
    else:
      batch = {k : v // recipe[k] for k, v in ingredients.items() if k in recipe}
  return min(batch.values())
   


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))