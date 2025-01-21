countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# Use map to create a new list by changing each country to uppercase in the countries list
uppercase_countries = list(map(lambda country: country.upper(), countries))
print(uppercase_countries)

# Use map to create a new list by changing each number to its square in the numbers list
square_number_list = list(map(lambda x: x *x, numbers))
print(square_number_list)

# Use map to change each name to uppercase in the names list
# Use filter to filter out countries containing 'land'.
land_countries_list = list(filter(lambda x: str(x).__contains__('land'), countries))
print(land_countries_list)

# Use filter to filter out countries having exactly six characters.
six_characters_countries_list = list(filter(lambda country: len(str(country)) == 6, countries))
print(six_characters_countries_list)

# Use filter to filter out countries containing six letters and more in the country list.
characters_countries_list = list(filter(lambda country: len(str(country)) >= 6, countries))
print(characters_countries_list)

# Use filter to filter out countries starting with an 'E'
e_start_countries = list(filter(lambda country: str(country).find('E') == 0, countries))
print(e_start_countries)



# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
# Use reduce to sum all the numbers in the numbers list.
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.