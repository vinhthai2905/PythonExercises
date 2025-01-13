# Unpack siblings and parents from family_members
sisters = ('Lisa', 'Rochelle', 'Mitchell')
brothers = ('Keith', 'Ellis', 'Nick')
siblings = sisters.__add__(brothers)
family_members = list(siblings)
family_members.extend(['Father', 'Mother'])
family_members = tuple(family_members)
print(family_members)

# Unpacking
*siblings, father, mother = family_members
print('Siblings:', siblings)
print('Father:', father)
print('Mother:', mother)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Lemonade', 'Apple', 'Pineapple', 'Grapes')
vegetables = ('Carrot', 'Avocado', 'Lettuce', 'Pear', 'Garlic')
animal_products = ('Cow Milk', 'Cheese', 'Steak', 'Chicken Thigh')
food_stuff_tp = fruits.__add__(vegetables).__add__(animal_products)

print(food_stuff_tp)
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_list = list(food_stuff_tp)
middle_index = len(food_stuff_list) // 2

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
sliced_food_stuff = food_stuff_list[middle_index:middle_index + 1]
print(sliced_food_stuff)

# Slice out the first three items and the last three items from food_staff_lt list
sliced_food_stuff = food_stuff_list[:3].__add__(food_stuff_list[10:])
print(sliced_food_stuff)
# Delete the food_staff_tp tuple completely

# Check if an item exists in tuple
item = input('Specify the item you wanna check: ')
if item in food_stuff_tp:
    print('It is exist.')
else:
    print('Not exist.')


# Check if 'Estonia' is a nordic country
#
# Check if 'Iceland' is a nordic country