# This program will tell the user how much of each ingredient he needs to make however many servings he wants of a
# simple summer tomato salad
# https://www.simplyrecipes.com/simple-summer-tomato-salad-recipe-5524666

# Variables are declared here
# Variables that end in "vin" describe ingredients that will be used to make the vinaigrette
# Variables that end in "salad" describe ingredients that make up the salad itself
# The quantity of each ingredient is divided by four to account for one serving
servings = 4
desired_servings = int(input("How many servings would you like to make?: "))

rw_vinegar_vin_tbsp = (2/4) * desired_servings
dij_mustard_vin_tsp = (1/4) * desired_servings
honey_vin_tsp = (1/4) * desired_servings
ev_olive_oil_vin_cup = (1/4) * desired_servings

med_red_onion_salad = (0.25/4) * desired_servings
tomatoes_salad_lbs = (2/4) * desired_servings
kosher_salt_salad_tsp = (1/4) * desired_servings
basil_chiffonade_salad_cup = (0.25/4) * desired_servings
mint_chiffonade_salad_tbsp = (2/4) * desired_servings

# The quantity of each ingredient needs to be multiplied by desired_servings
# Quantity of each ingredient to make the vinaigrette
print(f'To make {desired_servings} servings, you will need:\n')

print(f'{rw_vinegar_vin_tbsp:.1f} tablespoons of red wine vinegar for the vinaigrette')
print(f'{dij_mustard_vin_tsp:.1f} teaspoons of dijon mustard for the vinaigrette')
print(f'{honey_vin_tsp:.1f} teaspoons of honey for the vinaigrette')
print(f'{ev_olive_oil_vin_cup:.1f} cups of extra-virgin olive oil for the vinaigrette \n')

# Quantity of each ingredient to make the salad itself
print(f'{med_red_onion_salad:.1f} medium red onions for the salad')
print(f'{tomatoes_salad_lbs:.1f} pounds of fresh sliced tomatoes')
print(f'{kosher_salt_salad_tsp:.1f} teaspoons of kosher salt for the salad')
print(f'{basil_chiffonade_salad_cup:.1f} cups of basil cut chiffonade for the salad')
print(f'{mint_chiffonade_salad_tbsp:.1f} tablespoons of mint cut chiffonade for the salad \n')

# A tip for the user
print("Tip: add ground black pepper to taste")
